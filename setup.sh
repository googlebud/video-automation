#!/bin/bash

echo "🎬 Video Automation Setup"
echo "========================="
echo ""

# Check Python version
python_version=$(python3 --version 2>&1 | grep -oP '\d+\.\d+')
required_version="3.8"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo "❌ Python 3.8+ required. Found: $python_version"
    exit 1
fi

echo "✅ Python $python_version detected"
echo ""

# Check ffmpeg
if ! command -v ffmpeg &> /dev/null; then
    echo "⚠️  ffmpeg not found. Installing..."
    
    if [[ "$OSTYPE" == "darwin"* ]]; then
        brew install ffmpeg
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        sudo apt-get update && sudo apt-get install -y ffmpeg
    else
        echo "❌ Please install ffmpeg manually: https://ffmpeg.org/download.html"
        exit 1
    fi
fi

echo "✅ ffmpeg installed"
echo ""

# Install Python dependencies
echo "📦 Installing Python packages..."
pip install -r requirements.txt --quiet

echo "✅ Dependencies installed"
echo ""

# Create directories
mkdir -p outputs temp

echo "✅ Directories created"
echo ""

# Check for API keys
if [ ! -f "config.json" ]; then
    echo "⚠️  config.json not found. Creating template..."
    cp config.json.template config.json 2>/dev/null || true
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit config.json with your API keys"
echo "2. Get free Pexels API key: https://www.pexels.com/api/"
echo "3. Edit content_template.json with your scripts"
echo "4. Run: python generate_video.py content_template.json"
echo ""
echo "For web dashboard: open index.html in browser"
echo ""
