"""
Run this once to generate ASSISTANT_SESSION string
Termux: python gen_session.py
"""
from pyrogram import Client

API_ID = int(input("Enter API_ID: "))
API_HASH = input("Enter API_HASH: ")

with Client("assistant", api_id=API_ID, api_hash=API_HASH, in_memory=True) as app:
    print("\n\n===== SESSION STRING =====\n")
    print(app.export_session_string())
    print("\n==========================\n")
    print("Copy this and paste in config.py as ASSISTANT_SESSION")
