# Forest Adventure Game

A text-based adventure game with image generation, where you explore a magical forest and make choices that affect your journey's outcome.

## Features

- Choice-based gameplay with branching narratives
- Dynamic image generation based on your story choices
- Score tracking based on your decisions
- Different endings depending on your path and score

## Setup

1. Install Python 3.7+ and pip
2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

## Running Locally

1. Start the Flask backend:
   ```
   python -m flask --app api/index.py run
   ```
2. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## Deployment on Vercel

This application is configured to be deployed on Vercel:

1. Fork/clone this repository
2. Connect to Vercel
3. Deploy

## How to Play

1. Read the situation text and look at the image
2. Choose one of the options presented
3. Each choice affects your score and leads to different story paths
4. Reach one of several possible endings based on your choices

## Technical Details

- Frontend: HTML, CSS, JavaScript
- Backend: Python Flask
- Image Generation: Pollinations.ai API

## Development

To modify the game:
- Edit `api/index.py` to change the story nodes and game logic
- Edit files in the `public` directory to change the frontend appearance and behavior 