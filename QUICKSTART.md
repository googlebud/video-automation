# ⚡ Quick Reference Cheat Sheet

## 🚀 Getting Started (5 Minutes)

```bash
# 1. Setup
chmod +x setup.sh && ./setup.sh

# 2. Get API Key (Free)
# Visit: https://www.pexels.com/api/
# Add to config.json: "pexels_api_key": "YOUR_KEY"

# 3. Generate Videos
python script_generator.py finance 10
python generate_video.py content_finance_*.json

# 4. Upload & Profit
# Upload videos from outputs/ folder to TikTok/YouTube/IG
```

## 📝 Content Creation Commands

```bash
# Generate scripts for specific niche
python script_generator.py [niche] [count]

# Examples:
python script_generator.py finance 20
python script_generator.py self-improvement 15
python script_generator.py productivity 10

# Generate videos from scripts
python generate_video.py content_file.json

# Batch generate multiple files
for file in content_*.json; do python generate_video.py "$file"; done
```

## 🎯 Niches That Work

| Niche | CPM | Difficulty | Content Ideas |
|-------|-----|------------|---------------|
| 💰 Finance | $8-15 | Medium | Passive income, investing, side hustles |
| 🧠 Psychology | $6-12 | Low | Human behavior, relationships, mindset |
| 📈 Self-Improvement | $7-13 | Low | Habits, morning routines, productivity |
| 💻 AI/Tech | $10-20 | Medium | AI tools, tech reviews, tutorials |
| 🔥 Motivation | $5-10 | Low | Success stories, quotes, inspiration |

## 📊 Viral Formula

### Script Structure (45-55 seconds)
```
[3 sec]  Hook: "Want to make $10k/month?"
[5 sec]  Problem: "Most people struggle because..."
[35 sec] Value: Point 1, Point 2, Point 3
[7 sec]  CTA: "Follow for more tips"
```

### Best Hooks (Tested)
1. "Want to [benefit]? Here's how..."
2. "This changed my life forever..."
3. "Why [belief] is completely wrong..."
4. "I made $[amount] doing this..."
5. "The truth about [topic] nobody tells you..."

### Posting Schedule
| Platform | Best Times (EST) | Frequency |
|----------|------------------|-----------|
| TikTok | 6-9 AM, 5-8 PM | 3-5x/day |
| YouTube Shorts | 12-3 PM | 2-3x/day |
| Instagram Reels | 11 AM-1 PM | 2-3x/day |

## 🎨 Video Settings

### Optimal Settings
- **Duration**: 45-55 seconds
- **Format**: 1080x1920 (9:16 vertical)
- **FPS**: 30 (or 60 for smooth motion)
- **Captions**: Always enabled
- **Music**: Trending audio only

### Caption Tips
- Keep text on screen 2-3 seconds max
- Use high contrast (white text, black stroke)
- Position at bottom 1/3 of screen
- Font: Bold, simple, readable

## 💰 Monetization Path

### Phase 1: Foundation (Month 1-2)
- Post 100+ videos
- Find your winning formula
- Goal: 100k views/week

### Phase 2: Growth (Month 3-4)
- 2x output on winners
- Kill underperformers
- Goal: 500k views/week
- Revenue: $500-1500/month

### Phase 3: Scale (Month 5-6)
- Multiple accounts
- Affiliate marketing
- Goal: 2M+ views/week
- Revenue: $5-10k/month

## 🔧 Common Issues & Fixes

### "Video quality is poor"
```bash
# Edit generate_video.py line 175:
fps=60  # Change from 30 to 60
preset='slow'  # Change from 'medium' to 'slow'
```

### "Videos take too long to generate"
```bash
# Use batch processing
python generate_video.py content.json &
# Continue working while it generates
```

### "Captions not readable"
```python
# Edit generate_video.py lines 118-125
fontsize=70  # Increase from 60
stroke_width=4  # Increase from 3
```

### "Running out of API credits"
```bash
# Use free alternatives:
# TTS: edge-tts (free, unlimited)
# Footage: Local files or color backgrounds
# Remove API keys from config.json to use free options
```

## 📈 Success Metrics

### Track These Daily
- Views per video
- Engagement rate (likes + comments + shares / views)
- Follower growth
- Best performing time slots

### Weekly Goals
- Total views: 100k+ (beginner), 500k+ (intermediate), 2M+ (advanced)
- New followers: 1k+ (beginner), 5k+ (intermediate), 20k+ (advanced)
- Engagement rate: >5% (minimum), >10% (good), >15% (excellent)

### Monthly Targets
- Month 1: 500k total views, 5k followers
- Month 2: 1M total views, 15k followers
- Month 3: 3M total views, 50k followers, $2-5k revenue
- Month 6: 10M+ total views, 150k+ followers, $10k+ revenue

## 🎯 Content Ideas Generator

### Finance Niche
- "How I made $X in [timeframe]"
- "[Number] passive income streams"
- "Investing mistakes that cost me $X"
- "Side hustles that actually work"
- "How to save $X per month"

### Self-Improvement
- "Morning routine of successful people"
- "Habits that changed my life"
- "Books that made me [outcome]"
- "Why you can't [achieve goal]"
- "How to build [positive trait]"

### Psychology
- "Why people [behavior]"
- "Signs someone is [trait]"
- "How to read body language"
- "Psychology tricks that work"
- "What [action] says about you"

## ⚙️ File Locations

```
video-automation/
├── index.html          → Open in browser for dashboard
├── generate_video.py   → Main generation script
├── script_generator.py → Create content files
├── content_*.json      → Your video scripts
├── outputs/            → Generated videos here
├── config.json         → API keys and settings
└── README.md          → Full documentation
```

## 🚨 Don't Do This

❌ Post same video on multiple accounts (ban risk)
❌ Use copyrighted music without license
❌ Ignore analytics (data = profit)
❌ Spread across too many niches
❌ Copy competitors exactly (be unique)
❌ Buy followers (kills engagement)
❌ Post inconsistently (algorithm punishes)

## ✅ Do This

✅ Post consistently (3+ videos daily)
✅ Engage with comments (boosts algorithm)
✅ Use trending sounds
✅ Hook viewers in first 3 seconds
✅ Add value (don't just entertain)
✅ Track what works, kill what doesn't
✅ Batch create content weekly

## 🎬 Workflow Template

### Sunday (Batch Day - 2 hours)
1. Generate 30 scripts: `python script_generator.py finance 30`
2. Generate videos: `python generate_video.py content_*.json`
3. Review and select best 21 videos
4. Schedule posts for the week

### Daily (15 minutes)
1. Check analytics from previous day
2. Respond to top comments
3. Note viral patterns
4. Adjust strategy if needed

### Weekly Review (30 minutes)
1. Calculate metrics
2. Identify top performers
3. Adjust content mix
4. Plan next week

---

## 🚀 Start Now

```bash
# Get started in 3 commands:
./setup.sh
python script_generator.py finance 20
python generate_video.py content_finance_*.json

# Upload outputs/*.mp4 to TikTok
# Repeat daily
# Scale to $10k/month
```

**Remember**: Speed > Perfection. Post volume wins.
