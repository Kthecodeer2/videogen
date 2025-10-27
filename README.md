# Video Generation APIs

This project contains implementations for various video generation APIs.

## Files

- **openai_video.py** - OpenAI video generation API
- **runway_video.py** - Runway Gen-4 API
- **google_veo_video.py** - Google Veo 3.1 API
- **luma_video.py** - Luma Dream Machine API
- **meta_video.py** - Meta Movie Gen API
- **bytedance_video.py** - ByteDance Seedance API

## Setup

1. Install dependencies:
```bash
pip install openai python-dotenv requests google-genai
```

2. Create a `.env` file with your API keys:
```
OPENAI_API_KEY=your_key_here
RUNWAY_API_KEY=your_key_here
GOOGLE_API_KEY=your_key_here
LUMA_API_KEY=your_key_here
META_API_KEY=your_key_here
BYTEDANCE_API_KEY=your_key_here
```

## Usage

Each file can be run independently or imported as a module.

### OpenAI
```python
from openai_video import generate_video_openai

video = generate_video_openai("A calico cat playing a piano on stage")
print(f"Video ID: {video.id}")
```

### Runway
```python
from runway_video import generate_video_runway

video = generate_video_runway(
    "A serene landscape with mountains and a river at sunset",
    turbo=True
)
```

### Google Veo
```python
from google_veo_video import generate_video_veo

video = generate_video_veo(
    "A bustling city street during a rainy night",
    aspect_ratio='16:9',
    duration=8
)
```

### Luma
```python
from luma_video import generate_video_luma

video = generate_video_luma(
    "A futuristic cityscape with flying cars",
    extensions=['motion_blur', 'color_grading']
)
```

### Meta
```python
from meta_video import generate_video_meta

video = generate_video_meta(
    "A dramatic scene of a spaceship entering a wormhole",
    duration=16
)
```

### ByteDance
```python
from bytedance_video import generate_video_bytedance

video = generate_video_bytedance(
    "A cartoon character dancing in a park",
    motion_style='natural'
)
```

## API Status

**Note**: Some APIs (Luma, Meta, ByteDance) may not have public API access yet or may require special access. Please check the official documentation for each service for the most up-to-date information on API availability and access.

