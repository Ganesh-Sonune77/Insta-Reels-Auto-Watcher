# tor_launcher.py
import subprocess
import os

TOR_PATH = r"replace with your tor.exe path"
TORRC_PATH = r" replace with your torrc path"
if os.path.exists(TOR_PATH) and os.path.exists(TORRC_PATH):
    subprocess.Popen([TOR_PATH, "-f", TORRC_PATH])
    print("🧅 TOR launched successfully.")
else:
    print("❌ TOR path or torrc not found.")