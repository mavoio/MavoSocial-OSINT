# Social Media Username Finder

A Python tool to search for usernames across multiple social media platforms.

## Supported Platforms
- Instagram
- YouTube
- Reddit
- Roblox
- Twitter
- Steam
- GitHub
- TikTok
- Twitch
- Pinterest
- DeviantArt
- Spotify
- Medium
- Telegram
- VKontakte

## Requirements
- Python 3.12
- Required packages listed in `requirements.txt`

## Installation
1. Clone this repository
2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage
Run the script:
```bash
python app.py
```

- Enter a username when prompted
- The tool will search across all supported platforms
- Type 'quit' to exit the program
- Press Ctrl+C to terminate at any time

## Features
- Searches across 15 different platforms
- Color-coded results for better readability
- Built-in rate limiting to avoid API blocks
- Error handling for each platform
- Continuous search mode (search multiple usernames)
- Summary of found profiles

## Note
This tool performs basic checks for username availability. Due to rate limiting and platform restrictions, results may not always be 100% accurate. 