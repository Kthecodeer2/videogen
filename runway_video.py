import requests
import os
from dotenv import load_dotenv

load_dotenv()

def generate_video_runway(prompt: str, turbo: bool = True, reference_image: str = None):
    """
    Generate video using Runway Gen-4 API
    
    Args:
        prompt: Text description of the video to generate
        turbo: Use Gen-4 Turbo for faster generation
        reference_image: Optional URL to a reference image
    
    Returns:
        dict: Response with video information
    """
    api_key = os.getenv('RUNWAY_API_KEY')
    
    if not api_key:
        raise ValueError("RUNWAY_API_KEY environment variable not set")
    
    url = 'https://api.runwayml.com/v1/gen-4/generate'
    
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    data = {
        'prompt': prompt,
        'options': {
            'turbo': turbo,
        }
    }
    
    if reference_image:
        data['options']['image_reference'] = reference_image
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f'Error: {response.status_code}, {response.text}')

if __name__ == "__main__":
    video = generate_video_runway("A serene landscape with mountains and a river at sunset")
    print(f"Video response: {video}")

