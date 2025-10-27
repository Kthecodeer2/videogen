import requests
import os
from dotenv import load_dotenv

load_dotenv()

def generate_video_bytedance(prompt: str, character_reference: str = None, motion_style: str = 'natural'):
    """
    Generate video using ByteDance Seedance API
    
    Args:
        prompt: Text description of the video to generate
        character_reference: Optional URL to a character reference image
        motion_style: Motion style ('natural', 'dramatic', 'subtle')
    
    Returns:
        dict: Response with video information
    """
    api_key = os.getenv('BYTEDANCE_API_KEY')
    
    if not api_key:
        raise ValueError("BYTEDANCE_API_KEY environment variable not set")
    
    url = 'https://api.bytedance.com/v1/seedance/generate'
    
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    data = {
        'prompt': prompt,
        'motion_style': motion_style
    }
    
    if character_reference:
        data['character_reference'] = character_reference
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f'Error: {response.status_code}, {response.text}')

if __name__ == "__main__":
    video = generate_video_bytedance("A cartoon character dancing in a park")
    print(f"Video response: {video}")

