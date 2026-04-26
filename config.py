"""
Configuration file - Apni values yahan dalo
"""
import os

# ===== TELEGRAM API CREDENTIALS =====
# my.telegram.org se le sakte ho
API_ID = int(os.getenv("API_ID", "35828291"))   # <-- Apni API ID
API_HASH = os.getenv("API_HASH", "c025ee9d01d73b9d738d4f3e5e6137e2")  # <-- Apni API HASH

# ===== BOT TOKEN =====
# @BotFather se le sakte ho
BOT_TOKEN = os.getenv("BOT_TOKEN", "8631333041:AAHWj3Ut17BSn4laROufER6gF24eA0Hqj2c")

# ===== ASSISTANT (USERBOT) SESSION =====
# Pyrogram string session - ye account VC join karega
ASSISTANT_SESSION = os.getenv("ASSISTANT_SESSION", "BQIiskMACRzC9BbFiXFDr4ACFHYBi0IJhISHrEnahWa20jdzZQlCYZmFJ0T2NiCQh9it2kkqQyPNqGWkUtOciXh1GQM_0PutISDgz4FeZ98uamBikeoFUv5rBew0qxNRpUujo8siG_jPxxisUGmaW56_J_7HiObJB3QfJKhwUQqi0YtUDrCU8ofZIMCQAdGNYj_22vcqaSdahtWOS_y52VXfvxqRDHY6WqUlojY8wJjhKJTR_qeNl2MwdaY329nChY4cEJBqHO7zuSCI9CyIz8wCf3PSWvJKM03VzI-z-KvjjWuUH0yT5aXjd27WNGqaVAVEw2JxU8zZ79j6IjDBrEsnj14mYwAAAAIHIiSYAA")

# ===== OPTIONAL =====
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", "")

# Owner ID (apni telegram user id)
OWNER_ID = int(os.getenv("OWNER_ID", "7953454559"))

# Welcome image path
START_IMAGE = "start.jpg"
