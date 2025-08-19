## 📺 Instagram Reel Watcher

A Flask web app to automate Instagram Reel watching using Selenium and TOR for privacy and IP rotation.

## Features

- Watch any Instagram Reel on multiple virtual screens (browser sessions)
- Optionally auto-like reels
- Uses TOR for IP rotation and privacy
- Live status logs and screenshots
- Save logs for later review

## Requirements

- Python 3.10+
- Google Chrome browser
- [ChromeDriver](https://chromedriver.chromium.org/) (matching your Chrome version)
- [TOR Expert Bundle](https://www.torproject.org/download/tor/)
- All Python dependencies in `requirements.txt`

## Setup

1. **Install Python dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

2. **Configure TOR:**
   - Download and extract the TOR Expert Bundle.
   - Edit your `torrc` file to include:
     ```
     SocksPort 9050
     ControlPort 9051
     ```
   - Update `tor_launcher.py` with the correct paths to `tor.exe` and `torrc`.

3. **Start TOR:**
   ```sh
   python tor_launcher.py
   ```
   You should see `🧅 TOR launched successfully.`

tor_launcher.py — Minimal TOR Bootstrapper
This script launches the TOR service using a custom tor.exe binary and configuration file (torrc). 
Designed for automation workflows, scraping shields, or privacy-first routing setups.

🔧 Requirements
Windows system with TOR installed

Valid paths to:

tor.exe binary

torrc configuration file

📂 Setup
Edit the script to include your local paths:

TOR_PATH = r"C:\path\to\tor.exe"
TORRC_PATH = r"C:\path\to\torrc"

5. **Run the Flask app:**
   ```sh
   python app.py
   ```

6. **Open your browser and go to:**
   ```
   http://127.0.0.1:5000
   ```

## Usage

- Paste an Instagram Reel link.
- Select the number of screens (1-10).
- Choose whether to auto-like the reel.
- Click "Start Watching".
- View live logs and screenshots in the app.
- Use the `/save-logs` endpoint to save logs.

## Notes

- Make sure ChromeDriver is in your PATH or the project folder.
- TOR must be running before starting the Flask app.
- For best privacy, do not use your main Instagram account.
- All logs are saved in the `logs/` folder, screenshots in `screenshots/`.

---

**For educational and research purposes
