import requests
import os
from dotenv import load_dotenv

load_dotenv()

def generate_video_luma(prompt: str, keyframes: list = None, extensions: list = None):
    """
    Generate video using Luma Dream Machine API
    
    Args:
        prompt: Text description of the video to generate
        keyframes: Optional list of keyframe objects with 'time' and 'description'
        extensions: Optional list of extension names
    
    Returns:
        dict: Response with video information
    """
    api_key = os.getenv('LUMA_API_KEY')
    
    if not api_key:
        raise ValueError("LUMA_API_KEY environment variable not set")
    
    url = 'https://api.luma.ai/v1/dream-machine/generate'
    
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    data = {
        'prompt': prompt
    }
    
    if keyframes:
        data['keyframes'] = keyframes
    
    if extensions:
        data['extensions'] = extensions
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f'Error: {response.status_code}, {response.text}')

if __name__ == "__main__":
    video = generate_video_luma(
        "A futuristic cityscape with flying cars",
        extensions=['motion_blur', 'color_grading']
    )
    print(f"Video response: {video}")

