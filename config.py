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
ASSISTANT_SESSION = os.getenv("ASSISTANT_SESSION", "BQIiskMAVA6lEUPzkmTtQn7zh__KAJn0nzSuebU2tw30rtVbz4Tq4Ai03em8OlirqyZxa2ZNAgY2SBf87wY4hsiBin7uN7SYE6y4JSWtzKnGep3IfQe3rJE2-iGE1-0loCRhLLs_ZduSfyTIR7JXFP984-1_ZTwDQu_dGEXpc2a_2acwT4skZRj8mHUgT1SKW5JtEpf3CA8e2xiazKVHtz-jUI7w1wLHpQBm9iUGoaQ9poZQeMt1D8FhIDO335CzgUlwpZkYZ7B_gPg7gPXKfuz9V0OqFEYnZ5pYTNwRM45fWx_ozUfnNP8HAeJLhGRtGPtJeyI0Qyygui_2YSjjQ-Zd6vh5cQAAAAIHIiSYAA")

# ===== OPTIONAL =====
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", "")

# Owner ID (apni telegram user id)
OWNER_ID = int(os.getenv("OWNER_ID", "7953454559"))

# Welcome image path
START_IMAGE = "start.jpg"
