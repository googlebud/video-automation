https://googlebud.github.io/video-automation/

# 🎬 Automated Faceless Video Generation System

Generate viral TikTok/YouTube Shorts/Instagram Reels at scale with AI.

## 🚀 Quick Start

### Option 1: Local Generation (Recommended)

```bash
# 1. Clone repository
git clone https://github.com/yourusername/video-automation.git
cd video-automation

# 2. Install dependencies
pip install -r requirements.txt

# 3. Install ffmpeg (required)
# Mac: brew install ffmpeg
# Ubuntu: sudo apt-get install ffmpeg
# Windows: Download from ffmpeg.org

# 4. Configure API keys in config.json
# Get free Pexels API: https://www.pexels.com/api/
# Optional: OpenAI API for better TTS

# 5. Create your content list or use template
# Edit content_template.json with your scripts

# 6. Generate videos
python generate_video.py content_template.json

# Videos will be in outputs/ directory
```

### Option 2: GitHub Pages Dashboard

1. Fork this repository
2. Enable GitHub Pages (Settings → Pages → Source: main branch)
3. Visit `https://yourusername.github.io/video-automation/`
4. Use web interface to create content
5. Download JSON and run locally

### Option 3: GitHub Actions Automation

1. Add secrets to your repo:
   - `OPENAI_API_KEY` (optional)
   - `PEXELS_API_KEY` (free from pexels.com/api)
2. Push a `content_*.json` file to trigger generation
3. Download artifacts from Actions tab

## 📁 Project Structure

```
video-automation/
├── generate_video.py       # Main video generation script
├── config.json            # API keys and settings
├── content_template.json  # Example content structure
├── requirements.txt       # Python dependencies
├── index.html            # Web dashboard (GitHub Pages)
├── outputs/              # Generated videos
├── temp/                 # Temporary files
└── .github/workflows/    # GitHub Actions automation
```

## 🎯 Content Structure

Create a JSON file with your video scripts:

```json
{
  "videos": [
    {
      "title": "Your Video Title",
      "script": "Your 30-60 second script here...",
      "keyword": "keyword for background footage",
      "tags": ["tag1", "tag2", "tag3"],
      "niche": "self-improvement"
    }
  ]
}
```

### Script Writing Formula (60 seconds max):

1. **Hook (3-5 sec)**: Attention grabber
2. **Value (40-50 sec)**: Core content, tips, insights
3. **CTA (5-7 sec)**: Follow for more, like, share

**Example:**
```
"Want to 10x your productivity? [HOOK]
Here are 3 habits that changed everything for me.
First, time blocking. Second, single-tasking. Third, 
the 2-minute rule. [VALUE]
Follow for more productivity hacks. [CTA]"
```

## ⚙️ Configuration

Edit `config.json`:

```json
{
  "output_directory": "outputs",
  "openai_api_key": "sk-...",     // Optional, or use free edge-tts
  "pexels_api_key": "YOUR_KEY",   // Free API key
  "voice": "onyx",                 // Voice type
  "video_settings": {
    "width": 1080,
    "height": 1920,               // 9:16 vertical format
    "fps": 30
  }
}
```

### Free vs Paid Options:

| Feature | Free | Paid |
|---------|------|------|
| TTS | edge-tts | OpenAI ($0.015/1k chars) |
| Footage | Color backgrounds | Pexels (free) / Custom |
| Quality | Good | Excellent |

## 🎨 Customization

### Change Voice

In `config.json`:
- `onyx` - Deep male (default)
- `echo` - Male
- `nova` - Female
- `shimmer` - Female

### Custom Backgrounds

Replace `get_stock_footage()` function to:
- Use your own video files
- Generate AI images (DALL-E, Midjourney)
- Use alternative stock APIs (Pixabay, Unsplash)

### Caption Styling

Edit in `generate_video.py`:
```python
txt_clip = TextClip(
    chunk,
    fontsize=60,        # Adjust size
    color='white',      # Change color
    stroke_color='black',
    stroke_width=3
)
```

## 📊 Scaling Strategy

### Phase 1: Test (Week 1-2)
- Create 20 videos across 5 niches
- Post 3x daily
- Track what gets views

### Phase 2: Focus (Week 3-4)
- Kill underperforming niches
- 2x production on winners
- A/B test hooks

### Phase 3: Scale (Month 2+)
- Automate posting with scheduling tools
- Multiple accounts per platform
- Batch generate 50-100 videos/week

## 🔧 Troubleshooting

### "ModuleNotFoundError"
```bash
pip install -r requirements.txt --upgrade
```

### "ffmpeg not found"
Install ffmpeg for your OS (see Quick Start)

### Videos not generating
- Check API keys in config.json
- Verify script length (<60 seconds)
- Check temp/ directory permissions

### Low quality output
- Increase fps to 60
- Use OpenAI TTS instead of edge-tts
- Source higher quality Pexels videos

## 💡 Pro Tips

1. **Script Length**: 45-55 seconds = optimal engagement
2. **Hooks**: First 3 seconds decide everything
3. **Captions**: Essential for sound-off viewing
4. **Posting Time**: 
   - TikTok: 6-9 AM, 5-8 PM EST
   - YouTube Shorts: 12-3 PM EST
   - Instagram: 11 AM-1 PM EST
5. **Consistency**: 3 videos/day minimum
6. **Niches**: Money, self-improvement, psychology = highest CPM

## 🎯 High-Performing Niches

| Niche | Avg Views | CPM | Difficulty |
|-------|-----------|-----|------------|
| Finance | High | $8-15 | Medium |
| Psychology | Very High | $6-12 | Low |
| Self-Improvement | High | $7-13 | Low |
| AI/Tech | Medium | $10-20 | Medium |
| Motivation | Very High | $5-10 | Low |

## 📈 Monetization Paths

1. **Platform Revenue**
   - TikTok Creator Fund: $0.02-0.04 per 1k views
   - YouTube Shorts: $0.01-0.03 per 1k views
   - Instagram: Bonuses vary

2. **Affiliate Marketing** (Recommended)
   - Add affiliate links in bio
   - Target: $50-200 per sale
   - Scale: 1M views/month = $5-10k affiliate income

3. **Sponsored Content**
   - 100k followers = $500-2000 per post
   - Reach out to brands once you hit 50k

4. **Sell Accounts**
   - 100k TikTok = $500-1500
   - Build → Grow → Flip

## 🔄 Workflow Automation

### Daily Routine:
1. Generate 3-5 videos (10 minutes)
2. Schedule with Later/Buffer
3. Engage 30 minutes (reply to comments)
4. Analyze top performers

### Weekly:
1. Batch create 20-30 scripts
2. Generate all videos Sunday
3. Schedule week ahead

### Monthly:
1. Analyze metrics
2. Kill underperforming content
3. Scale winners

## 🚨 Common Mistakes to Avoid

1. ❌ Using copyrighted music (use royalty-free)
2. ❌ Inconsistent posting (algorithm punishment)
3. ❌ Ignoring analytics (data = profit)
4. ❌ Too many niches (focus wins)
5. ❌ Low quality scripts (viewers smell AI slop)

## 📝 License

MIT License - Do whatever you want with this code.

## 🤝 Contributing

PRs welcome for:
- Additional TTS providers
- Auto-posting integrations
- Analytics tracking
- UI improvements

## ⚡ Next Steps

1. ✅ Generate your first 10 videos
2. ✅ Post to TikTok/YouTube/Instagram
3. ✅ Track what works
4. ✅ Scale winners
5. ✅ Monetize

**Target: 1M views/month by Month 3**

---

## 🎬 Advanced Features

### Auto-Posting Integration

```python
# Add to generate_video.py after video creation:

def auto_post_tiktok(video_path, caption, tags):
    # Use TikTok API or selenium automation
    pass

def auto_post_youtube(video_path, title, description):
    # Use YouTube API
    pass
```

### A/B Testing Hooks

Create multiple versions of the same video with different hooks:

```json
{
  "title": "Productivity Hack",
  "hooks": [
    "Want to 10x your productivity?",
    "This changed my entire life...",
    "Nobody talks about this trick..."
  ],
  "body": "...",
  "cta": "Follow for more"
}
```

### Analytics Tracking

Integrate with platform APIs to track:
- View count
- Engagement rate
- Best performing hooks
- Optimal posting times

---

**Remember: Volume × Quality × Consistency = Results**

Generate 100 videos. 10 will pop off. Scale those 10. Repeat.
