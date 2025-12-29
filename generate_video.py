#!/usr/bin/env python3
"""
Automated Faceless Video Generator
Generates TikTok/YouTube Shorts style videos from text content
"""

import os
import json
from pathlib import Path
from moviepy.editor import *
from moviepy.video.fx import resize
import requests
from datetime import datetime
import random

class VideoGenerator:
    def __init__(self, config_path="config.json"):
        with open(config_path, 'r') as f:
            self.config = json.load(f)
        
        self.output_dir = Path(self.config['output_directory'])
        self.output_dir.mkdir(exist_ok=True)
        
        self.temp_dir = Path("temp")
        self.temp_dir.mkdir(exist_ok=True)
    
    def generate_voiceover(self, text, output_path):
        """Generate AI voiceover from text"""
        # Using OpenAI TTS (replace with your API key or use alternative)
        # Alternative: Use elevenlabs, google TTS, or edge-tts (free)
        
        api_key = self.config.get('openai_api_key', '')
        
        if api_key:
            # OpenAI TTS
            import openai
            openai.api_key = api_key
            
            response = openai.audio.speech.create(
                model="tts-1",
                voice=self.config.get('voice', 'onyx'),
                input=text
            )
            response.stream_to_file(output_path)
        else:
            # Free alternative: edge-tts
            import edge_tts
            import asyncio
            
            async def _generate():
                communicate = edge_tts.Communicate(text, "en-US-ChristopherNeural")
                await communicate.save(output_path)
            
            asyncio.run(_generate())
        
        return output_path
    
    def get_stock_footage(self, keyword, duration=10):
        """Download stock footage from Pexels (free)"""
        api_key = self.config.get('pexels_api_key', '')
        
        if not api_key:
            # Use placeholder or local footage
            return self.create_background_clip(duration)
        
        url = "https://api.pexels.com/videos/search"
        headers = {"Authorization": api_key}
        params = {
            "query": keyword,
            "per_page": 15,
            "orientation": "portrait"
        }
        
        response = requests.get(url, headers=headers, params=params)
        videos = response.json().get('videos', [])
        
        if videos:
            video = random.choice(videos)
            video_file = video['video_files'][0]
            video_url = video_file['link']
            
            # Download video
            temp_path = self.temp_dir / f"stock_{keyword}_{datetime.now().timestamp()}.mp4"
            video_content = requests.get(video_url).content
            with open(temp_path, 'wb') as f:
                f.write(video_content)
            
            return str(temp_path)
        
        return self.create_background_clip(duration)
    
    def create_background_clip(self, duration):
        """Create simple background if no stock footage"""
        from moviepy.video.VideoClip import ColorClip
        
        colors = [
            (20, 20, 30),      # Dark blue
            (30, 20, 40),      # Purple
            (40, 20, 20),      # Dark red
            (20, 30, 20),      # Dark green
        ]
        
        color = random.choice(colors)
        clip = ColorClip(size=(1080, 1920), color=color, duration=duration)
        return clip
    
    def generate_ai_image(self, prompt):
        """Generate AI image for background (optional)"""
        # Placeholder for AI image generation
        # Could integrate: DALL-E, Stability AI, or use Unsplash API
        pass
    
    def add_captions(self, video_clip, text, position='bottom'):
        """Add animated captions to video"""
        # Split text into chunks for better readability
        words = text.split()
        chunks = []
        chunk_size = 8  # words per caption
        
        for i in range(0, len(words), chunk_size):
            chunks.append(' '.join(words[i:i+chunk_size]))
        
        duration_per_chunk = video_clip.duration / len(chunks)
        
        caption_clips = []
        for i, chunk in enumerate(chunks):
            txt_clip = TextClip(
                chunk,
                fontsize=60,
                color='white',
                font='Arial-Bold',
                stroke_color='black',
                stroke_width=3,
                method='caption',
                size=(1000, None)
            )
            
            txt_clip = txt_clip.set_position(('center', 1400 if position == 'bottom' else 400))
            txt_clip = txt_clip.set_start(i * duration_per_chunk)
            txt_clip = txt_clip.set_duration(duration_per_chunk)
            
            caption_clips.append(txt_clip)
        
        return caption_clips
    
    def create_video(self, content_item):
        """Main video creation pipeline"""
        print(f"Generating video: {content_item['title']}")
        
        # 1. Generate voiceover
        voiceover_path = self.temp_dir / f"voice_{datetime.now().timestamp()}.mp3"
        self.generate_voiceover(content_item['script'], str(voiceover_path))
        audio = AudioFileClip(str(voiceover_path))
        
        # 2. Get background footage
        if isinstance(self.get_stock_footage(content_item.get('keyword', 'abstract'), audio.duration), str):
            background = VideoFileClip(self.get_stock_footage(content_item.get('keyword', 'abstract'), audio.duration))
        else:
            background = self.get_stock_footage(content_item.get('keyword', 'abstract'), audio.duration)
        
        background = background.set_duration(audio.duration)
        
        # Resize to 9:16 (1080x1920) for vertical video
        background = background.resize(height=1920)
        if background.w > 1080:
            background = background.crop(x_center=background.w/2, width=1080)
        elif background.w < 1080:
            background = background.resize(width=1080)
        
        # 3. Add captions
        caption_clips = self.add_captions(background, content_item['script'])
        
        # 4. Composite everything
        final_video = CompositeVideoClip([background] + caption_clips)
        final_video = final_video.set_audio(audio)
        
        # 5. Export
        output_filename = f"{content_item['title'].replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"
        output_path = self.output_dir / output_filename
        
        final_video.write_videofile(
            str(output_path),
            fps=30,
            codec='libx264',
            audio_codec='aac',
            preset='medium',
            threads=4
        )
        
        # Cleanup temp files
        if voiceover_path.exists():
            voiceover_path.unlink()
        
        print(f"Video created: {output_path}")
        return str(output_path)
    
    def batch_generate(self, content_list_path):
        """Generate multiple videos from content list"""
        with open(content_list_path, 'r') as f:
            content_list = json.load(f)
        
        results = []
        for item in content_list['videos']:
            try:
                video_path = self.create_video(item)
                results.append({
                    'title': item['title'],
                    'status': 'success',
                    'path': video_path
                })
            except Exception as e:
                results.append({
                    'title': item['title'],
                    'status': 'failed',
                    'error': str(e)
                })
                print(f"Failed to create {item['title']}: {e}")
        
        # Save results
        results_path = self.output_dir / f"results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(results_path, 'w') as f:
            json.dump(results, f, indent=2)
        
        return results


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python generate_video.py <content_list.json>")
        sys.exit(1)
    
    generator = VideoGenerator()
    results = generator.batch_generate(sys.argv[1])
    
    print(f"\n{'='*50}")
    print(f"Generation Complete!")
    print(f"Success: {len([r for r in results if r['status'] == 'success'])}")
    print(f"Failed: {len([r for r in results if r['status'] == 'failed'])}")
    print(f"{'='*50}")
