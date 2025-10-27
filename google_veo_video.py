from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()

def generate_video_veo(prompt: str, reference_images: list = None, aspect_ratio: str = '16:9', duration: int = 8):
    """
    Generate video using Google Veo 3.1 API
    
    Args:
        prompt: Text description of the video to generate
        reference_images: Optional list of reference image URLs
        aspect_ratio: Video aspect ratio (default: '16:9')
        duration: Video duration in seconds (default: 8)
    
    Returns:
        Video object with URI and metadata
    """
    api_key = os.getenv('GOOGLE_API_KEY')
    
    if not api_key:
        raise ValueError("GOOGLE_API_KEY environment variable not set")
    
    client = genai.Client(api_key=api_key)
    
    config = types.GenerateVideosConfig(
        aspect_ratio=aspect_ratio,
        duration=duration
    )
    
    if reference_images:
        config.reference_images = reference_images
    
    operation = client.models.generate_videos(
        model='veo-3.1-generate-preview',
        prompt=prompt,
        config=config
    )
    
    operation = operation.result()
    video = operation.generated_videos[0].video
    
    return video

if __name__ == "__main__":
    video = generate_video_veo("A bustling city street during a rainy night")
    print(f"Generated video URI: {video.uri}")

