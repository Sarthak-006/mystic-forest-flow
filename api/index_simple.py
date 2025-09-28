from flask import Flask, request, jsonify, send_from_directory
import requests
import hashlib
import os
import time
from flask_cors import CORS
import traceback

app = Flask(__name__)
CORS(app)

# Simple story nodes for testing
story_nodes = {
    "start": {
        "situation": "You find yourself in a mysterious forest. The path ahead splits in two directions. What do you do?",
        "prompt": "Fantasy forest with two paths, mysterious, ethereal light, detailed",
        "seed": 12345,
        "choices": [
            {
                "text": "Take the path that leads deeper into the forest",
                "next_node": "deep_forest",
                "score_modifier": 1,
                "tag": "curious"
            },
            {
                "text": "Follow the path that seems to lead to a clearing",
                "next_node": "clearing",
                "score_modifier": 0,
                "tag": "cautious"
            }
        ]
    },
    "deep_forest": {
        "situation": "You venture deeper into the forest. The trees grow taller and the light dims. You hear strange sounds ahead.",
        "prompt": "Dark fantasy forest, tall ancient trees, mysterious sounds, atmospheric",
        "seed": 23456,
        "choices": [
            {
                "text": "Investigate the strange sounds",
                "next_node": "end_brave",
                "score_modifier": 2,
                "tag": "brave"
            },
            {
                "text": "Find a way around the sounds",
                "next_node": "end_cautious",
                "score_modifier": 1,
                "tag": "cautious"
            }
        ]
    },
    "clearing": {
        "situation": "You reach a beautiful clearing with a crystal-clear pond. The water seems to shimmer with magic.",
        "prompt": "Magical forest clearing, crystal pond, shimmering water, peaceful",
        "seed": 34567,
        "choices": [
            {
                "text": "Drink from the magical pond",
                "next_node": "end_magic",
                "score_modifier": 3,
                "tag": "magical"
            },
            {
                "text": "Observe the pond from a distance",
                "next_node": "end_wise",
                "score_modifier": 2,
                "tag": "wise"
            }
        ]
    },
    "end_brave": {
        "situation": "You bravely investigate and discover a hidden treasure! Your courage has been rewarded.",
        "prompt": "Fantasy treasure chest, golden light, heroic discovery",
        "seed": 45678,
        "is_end": True,
        "ending_category": "Brave Explorer",
        "choices": []
    },
    "end_cautious": {
        "situation": "You wisely avoid the danger and find a safe path home. Your caution served you well.",
        "prompt": "Safe forest path, peaceful return, wise choice",
        "seed": 56789,
        "is_end": True,
        "ending_category": "Cautious Traveler",
        "choices": []
    },
    "end_magic": {
        "situation": "The magical water grants you special powers! You have become a forest guardian.",
        "prompt": "Magical transformation, forest guardian, mystical powers",
        "seed": 67890,
        "is_end": True,
        "ending_category": "Forest Guardian",
        "choices": []
    },
    "end_wise": {
        "situation": "Your wisdom leads you to discover ancient knowledge. You have become a forest sage.",
        "prompt": "Ancient knowledge, forest sage, wisdom, mystical books",
        "seed": 78901,
        "is_end": True,
        "ending_category": "Forest Sage",
        "choices": []
    }
}

# User sessions storage
user_sessions = {}

# Constants
POLLINATIONS_BASE_URL = "https://image.pollinations.ai/prompt/"

def reset_game_state(session_id=None):
    """Reset the game state for a new game"""
    return {
        "current_node_id": "start",
        "score": 0,
        "path_history": ["start"],
        "sentiment_tally": {"start": 0},
        "choice_history": []
    }

def get_node_details(node_id):
    """Get details for a specific story node"""
    return story_nodes.get(node_id, {})

# Routes
@app.route('/')
def serve_index():
    try:
        return send_from_directory('public', 'index.html')
    except:
        try:
            return send_from_directory('../public', 'index.html')
        except:
            return """
            <!DOCTYPE html>
            <html>
            <head>
                <title>Mystic Forest Flow</title>
            </head>
            <body>
                <h1>Mystic Forest Flow</h1>
                <p>API is working! <a href="/api/test">Test API</a></p>
            </body>
            </html>
            """

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy", "message": "Mystic Forest Flow API is running"})

@app.route('/api/test')
def test_api():
    return jsonify({
        "message": "API is working", 
        "timestamp": time.time(),
        "story_nodes_count": len(story_nodes),
        "user_sessions_count": len(user_sessions)
    })

@app.route('/api/state', methods=['GET'])
def get_current_state():
    try:
        # Get user's session ID from cookies or create a new one
        session_id = request.cookies.get('session_id')
        if not session_id:
            import secrets
            session_id = hashlib.md5(f"{time.time()}-{secrets.token_hex(8)}".encode()).hexdigest()
        
        # Get or create the user's game state
        if session_id in user_sessions and 'state' in user_sessions[session_id]:
            game_state = user_sessions[session_id]['state']
        else:
            game_state = reset_game_state(session_id)
            user_sessions[session_id] = {'state': game_state}
        
        current_node_id = game_state["current_node_id"]
        node_details = get_node_details(current_node_id)
        
        if not node_details:
            return jsonify({"error": "Invalid node"}), 400
        
        # Generate image URL
        prompt = node_details.get("prompt", "fantasy forest")
        encoded_prompt = requests.utils.quote(prompt)
        image_url = f"{POLLINATIONS_BASE_URL}{encoded_prompt}"
        
        # Get choices
        choices = node_details.get("choices", [])
        
        # Get score
        score = game_state.get("score", 0)
        
        # Prepare response
        response_data = {
            "situation": node_details.get("situation", ""),
            "is_end": node_details.get("is_end", False),
            "ending_category": node_details.get("ending_category", ""),
            "choices": choices,
            "image_url": image_url,
            "current_score": score,
            "score": score
        }
        
        # Create response with cookie
        from flask import make_response
        response = make_response(jsonify(response_data))
        response.set_cookie('session_id', session_id, max_age=86400*30)  # 30 days
        return response
        
    except Exception as e:
        print(f"Error in get_current_state: {str(e)}")
        traceback.print_exc()
        return jsonify({"error": f"Server error: {str(e)}"}), 500

@app.route('/api/choice', methods=['POST'])
def make_choice():
    try:
        data = request.json
        choice_index = data.get('choice_index')
        
        # Get session ID
        session_id = request.cookies.get('session_id')
        if not session_id:
            return jsonify({"error": "No session found"}), 400
        
        if session_id not in user_sessions:
            return jsonify({"error": "Invalid session"}), 400
        
        game_state = user_sessions[session_id]['state']
        current_node_id = game_state["current_node_id"]
        node_details = get_node_details(current_node_id)
        
        if not node_details or choice_index >= len(node_details.get("choices", [])):
            return jsonify({"error": "Invalid choice"}), 400
        
        choice = node_details["choices"][choice_index]
        
        # Update game state
        game_state["current_node_id"] = choice["next_node"]
        game_state["score"] += choice.get("score_modifier", 0)
        game_state["path_history"].append(choice["next_node"])
        game_state["choice_history"].append(choice["text"])
        
        # Update sentiment tally
        tag = choice.get("tag", "neutral")
        if tag not in game_state["sentiment_tally"]:
            game_state["sentiment_tally"][tag] = 0
        game_state["sentiment_tally"][tag] += 1
        
        return jsonify({"success": True, "message": "Choice processed"})
        
    except Exception as e:
        print(f"Error in make_choice: {str(e)}")
        traceback.print_exc()
        return jsonify({"error": f"Server error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
