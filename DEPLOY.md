# 🚀 GitHub Deployment Guide

## Quick Deploy to GitHub

### 1. Create Repository

```bash
# In your video-automation directory
git init
git add .
git commit -m "Initial commit: Automated video generation system"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/video-automation.git
git push -u origin main
```

### 2. Enable GitHub Pages

1. Go to repository Settings
2. Navigate to "Pages" section
3. Source: Deploy from branch `main`
4. Folder: `/ (root)`
5. Save

Your dashboard will be live at: `https://YOUR_USERNAME.github.io/video-automation/`

### 3. Set Up GitHub Secrets (for Actions)

1. Go to Settings → Secrets and variables → Actions
2. Add these secrets:
   - `OPENAI_API_KEY` (optional, for better TTS)
   - `PEXELS_API_KEY` (free from pexels.com/api)

### 4. Using GitHub Actions

**Trigger video generation:**

```bash
# Push a content file
git add content_finance_20250101.json
git commit -m "Add finance content"
git push

# Or manually trigger via GitHub Actions tab
```

Videos will be available as artifacts in the Actions tab.

## Local Development Workflow

```bash
# 1. Generate scripts
python script_generator.py finance 20

# 2. Generate videos
python generate_video.py content_finance_*.json

# 3. Review outputs
ls outputs/

# 4. Upload to social media manually or with automation
```

## Recommended Repository Structure

```
your-repo/
├── README.md                  # Main documentation
├── DEPLOY.md                  # This file
├── generate_video.py          # Core generator
├── script_generator.py        # Script creation tool
├── requirements.txt           # Python deps
├── config.json               # Config (don't commit with keys!)
├── index.html                # Web dashboard
├── content_template.json     # Example content
├── .github/
│   └── workflows/
│       └── generate.yml      # Auto-generation workflow
├── outputs/                  # Generated videos (gitignored)
└── temp/                     # Temporary files (gitignored)
```

## Customization

### Change Branding

Edit `index.html`:
- Line 37: Change title
- Line 38: Change description
- Lines 40-44: Update gradient colors

### Add Custom Niches

Edit `script_generator.py`:
- Add to `script_prompts` dict
- Add to `keywords` dict
- Add to `tags_map` dict

### Modify Video Style

Edit `generate_video.py`:
- Caption styling: Lines 118-125
- Video dimensions: Lines 142-148
- Background colors: Lines 101-106

## Best Practices

### Repository Management
- ✅ Keep config.json in .gitignore
- ✅ Commit content templates
- ✅ Don't commit generated videos (use Actions artifacts)
- ✅ Document your workflow in README

### API Keys Security
- ❌ Never commit API keys to public repos
- ✅ Use GitHub Secrets for automation
- ✅ Use environment variables locally
- ✅ Provide template config file

### Content Organization
- Create separate content files per niche
- Name files: `content_{niche}_{date}.json`
- Keep archive of successful scripts
- Track performance metrics

## Automation Setup

### Option A: GitHub Actions (Cloud)
- Pros: No local resources, automated
- Cons: Limited free minutes, slower
- Best for: Batch generation, scheduled posts

### Option B: Local Scripts (Recommended)
- Pros: Fast, unlimited, customizable
- Cons: Requires local setup
- Best for: Rapid iteration, testing

### Option C: Hybrid
- Generate locally for speed
- Use Actions for scheduled automation
- Keep everything synced in repo

## Troubleshooting

### GitHub Pages not showing dashboard
- Check Settings → Pages is enabled
- Ensure index.html is in root
- Wait 2-3 minutes for deployment
- Clear browser cache

### Actions failing
- Verify secrets are set correctly
- Check workflow logs in Actions tab
- Ensure content file format is correct

### Large files rejected
- Videos should stay in outputs/ (gitignored)
- If needed, use Git LFS for large assets
- Or use artifacts/releases for distribution

## Next Steps

1. ✅ Deploy to GitHub
2. ✅ Enable GitHub Pages
3. ✅ Set up secrets
4. ✅ Test workflow
5. ✅ Generate first batch
6. ✅ Share with team/clients

## Support

Issues? Check:
1. README.md for main documentation
2. GitHub Issues for common problems
3. Workflow logs for debugging

---

**Pro Tip**: Fork this repo, customize for your niche, and keep your successful scripts private in a separate branch.
