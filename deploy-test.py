#!/usr/bin/env python3
"""
Test script to verify the deployment is working
"""
import requests
import json
import time

def test_deployment():
    # Test both local and production URLs
    urls = [
        "http://127.0.0.1:5000",  # Local
        "https://mystic-forest-flow.vercel.app"  # Production
    ]
    
    for base_url in urls:
        print(f"\nTesting: {base_url}")
        print("=" * 50)
        
        # Test 1: Health check
        try:
            response = requests.get(f"{base_url}/health", timeout=10)
            print(f"+ Health check: {response.status_code}")
            if response.status_code == 200:
                print(f"  Response: {response.json()}")
            else:
                print(f"  Error: {response.text}")
        except Exception as e:
            print(f"- Health check failed: {e}")
            continue
        
        # Test 2: API test endpoint
        try:
            response = requests.get(f"{base_url}/api/test", timeout=10)
            print(f"+ API test: {response.status_code}")
            if response.status_code == 200:
                data = response.json()
                print(f"  Message: {data.get('message')}")
                print(f"  Story nodes: {data.get('story_nodes_count')}")
                print(f"  User sessions: {data.get('user_sessions_count')}")
            else:
                print(f"  Error: {response.text}")
        except Exception as e:
            print(f"- API test failed: {e}")
            continue
        
        # Test 3: Main state endpoint
        try:
            response = requests.get(f"{base_url}/api/state", timeout=15)
            print(f"+ State endpoint: {response.status_code}")
            if response.status_code == 200:
                data = response.json()
                print(f"  Situation: {data.get('situation', 'N/A')[:50]}...")
                print(f"  Choices: {len(data.get('choices', []))}")
                print(f"  Image URL: {data.get('image_url', 'N/A')[:50]}...")
                print(f"  Score: {data.get('score', 'N/A')}")
            else:
                print(f"  Error: {response.text}")
        except Exception as e:
            print(f"- State endpoint failed: {e}")
            continue
        
        print("+ All tests passed for this URL!")

if __name__ == "__main__":
    print("Testing Mystic Forest Flow deployment...")
    test_deployment()
