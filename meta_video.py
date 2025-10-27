import requests
import os
from dotenv import load_dotenv

load_dotenv()

def generate_video_meta(prompt: str, duration: int = 16):
    """
    Generate video with audio using Meta Movie Gen API
    
    Args:
        prompt: Text description of the video to generate
        duration: Duration in seconds (up to 16 seconds)
    
    Returns:
        dict: Response with video information
    """
    api_key = os.getenv('META_API_KEY')
    
    if not api_key:
        raise ValueError("META_API_KEY environment variable not set")
    
    url = 'https://api.meta.com/v1/movie-gen/generate'
    
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    data = {
        'prompt': prompt,
        'duration': min(duration, 16)  # Cap at 16 seconds
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f'Error: {response.status_code}, {response.text}')

if __name__ == "__main__":
    video = generate_video_meta("A dramatic scene of a spaceship entering a wormhole")
    print(f"Video response: {video}")

