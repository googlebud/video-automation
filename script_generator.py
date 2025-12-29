#!/usr/bin/env python3
"""
AI Script Generator
Generates multiple video scripts for a given niche using OpenAI API
"""

import json
import os
from datetime import datetime

# Uncomment when you have OpenAI API key
# import openai

def generate_scripts(niche, count=10, api_key=None):
    """Generate multiple video scripts for a niche"""
    
    script_prompts = {
        "self-improvement": [
            "3 morning habits that will change your life",
            "Why you're not productive (and how to fix it)",
            "The truth about discipline vs motivation",
            "How to build unbreakable habits",
            "5 books that made me successful"
        ],
        "finance": [
            "5 passive income streams for 2025",
            "How I made my first $10k online",
            "Investing mistakes that cost me $50k",
            "Best side hustles that actually work",
            "The compound effect of saving $10/day"
        ],
        "productivity": [
            "Time blocking changed my life",
            "Why you can't focus (and the fix)",
            "The Pomodoro technique explained",
            "Deep work vs shallow work",
            "My productivity system that actually works"
        ],
        "motivation": [
            "When you feel like giving up, watch this",
            "The pain of discipline vs regret",
            "Why comfort is killing your dreams",
            "You're running out of time",
            "Success leaves clues - here they are"
        ],
        "health": [
            "5 foods destroying your health",
            "Why you're always tired (fix this)",
            "The truth about intermittent fasting",
            "Simple workout routine for busy people",
            "Sleep hacks that actually work"
        ]
    }
    
    titles = script_prompts.get(niche, script_prompts["self-improvement"])[:count]
    
    # If you have OpenAI API key, uncomment below:
    """
    if api_key:
        openai.api_key = api_key
        
        scripts = []
        for title in titles:
            prompt = f'''
            Create a viral TikTok/YouTube Shorts script about: {title}
            
            Requirements:
            - 45-55 seconds when read aloud
            - Start with a strong hook (first 3 seconds)
            - Provide clear value/insights
            - End with a call-to-action
            - Use simple, direct language
            - No fluff or filler
            
            Format: Just the script, no labels or descriptions.
            '''
            
            response = openai.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=200,
                temperature=0.8
            )
            
            script = response.choices[0].message.content.strip()
            scripts.append(script)
        
        return titles, scripts
    """
    
    # Template scripts (replace with AI-generated when you have API key)
    template = """
    {hook}
    
    {value_point_1}
    
    {value_point_2}
    
    {value_point_3}
    
    {cta}
    """
    
    hooks = [
        "Want to know the secret?",
        "This changed everything for me.",
        "Nobody talks about this.",
        "Here's what they don't tell you.",
        "Stop doing this immediately."
    ]
    
    ctas = [
        "Follow for more tips like this.",
        "Save this for later. You'll need it.",
        "Drop a 🔥 if this helped you.",
        "Comment your biggest challenge below.",
        "Share this with someone who needs it."
    ]
    
    scripts = []
    for i, title in enumerate(titles):
        script = f"""Want to {title.lower()}? Here's what actually works.

First, understand this: {niche} isn't about perfection. It's about consistency.

Second, most people fail because they overcomplicate things. Keep it simple.

Third, results take time. Give it 90 days minimum.

Follow for more {niche} content that actually works."""
        
        scripts.append(script)
    
    return titles, scripts


def create_content_file(niche, count=10, api_key=None):
    """Create a complete content.json file"""
    
    titles, scripts = generate_scripts(niche, count, api_key)
    
    keywords = {
        "self-improvement": ["motivation", "success", "discipline", "habits"],
        "finance": ["money", "investing", "wealth", "success"],
        "productivity": ["focus", "work", "efficiency", "success"],
        "motivation": ["success", "inspire", "achieve", "goals"],
        "health": ["fitness", "healthy", "wellness", "energy"]
    }
    
    tags_map = {
        "self-improvement": ["selfimprovement", "personaldevelopment", "growth"],
        "finance": ["money", "finance", "investing", "wealth"],
        "productivity": ["productivity", "focus", "efficiency"],
        "motivation": ["motivation", "inspiration", "success"],
        "health": ["health", "fitness", "wellness"]
    }
    
    videos = []
    for title, script in zip(titles, scripts):
        video = {
            "title": title,
            "script": script,
            "keyword": keywords.get(niche, ["abstract"])[0],
            "tags": tags_map.get(niche, ["viral"]),
            "niche": niche
        }
        videos.append(video)
    
    content = {"videos": videos}
    
    # Save to file
    filename = f"content_{niche}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, 'w') as f:
        json.dump(content, f, indent=2)
    
    print(f"✅ Created {filename} with {count} video scripts")
    print(f"📊 Niche: {niche}")
    print(f"📝 Total videos: {len(videos)}")
    print(f"\nNext step: python generate_video.py {filename}")
    
    return filename


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python script_generator.py <niche> [count] [api_key]")
        print("\nAvailable niches:")
        print("- self-improvement")
        print("- finance")
        print("- productivity")
        print("- motivation")
        print("- health")
        print("\nExample: python script_generator.py finance 20")
        sys.exit(1)
    
    niche = sys.argv[1]
    count = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    api_key = sys.argv[3] if len(sys.argv) > 3 else None
    
    create_content_file(niche, count, api_key)
