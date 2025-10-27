from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def generate_video_openai(prompt: str):
    """Generate video using OpenAI API"""
    client = OpenAI()
    video = client.videos.create(prompt=prompt)
    return video

if __name__ == "__main__":
    video = generate_video_openai("A calico cat playing a piano on stage")
    print(f"Video ID: {video.id}")

