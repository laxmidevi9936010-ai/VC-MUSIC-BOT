# 🎵 Premium VC Music Bot

Telegram Voice Chat Music Bot — YouTube se gaane play karta hai premium font ke saath.

## ✨ Features

- 🎵 `/play <song name>` — YouTube se gaana search & play
- 🎨 Premium small-caps font (sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ style)
- 🖼 Thumbnail + duration + views ke saath message
- ⏸ Inline buttons: Pause / Resume / Stop / Seek
- 🌟 Welcome image + interactive start menu
- 📸 Image blur feature — bheji gayi photo blur dikhti hai, tap karne pe khulti hai
- 📚 Help menu

## 📦 Installation (Termux)

```bash
# Update Termux
pkg update -y && pkg upgrade -y

# Required packages
pkg install -y python git ffmpeg rust binutils

# Clone / Copy this folder, then:
cd vc-music-bot

# Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

## ⚙️ Setup

### Step 1 — Generate Assistant Session String

```bash
python gen_session.py
```
- API_ID, API_HASH dalo (my.telegram.org se)
- Phone number → OTP dalo
- Session string copy karo

### Step 2 — Edit `config.py`

```python
API_ID = 12345678                  # my.telegram.org se
API_HASH = "abcd1234..."           # my.telegram.org se
BOT_TOKEN = "123:ABC..."           # @BotFather se
ASSISTANT_SESSION = "BQF..."       # gen_session.py se
OWNER_ID = 123456789               # Apna telegram ID
```

OR environment variables set karo:
```bash
export API_ID=12345678
export API_HASH=abcd...
export BOT_TOKEN=123:ABC
export ASSISTANT_SESSION=BQF...
```

### Step 3 — Run

```bash
python main.py
```

## 🚀 Usage

1. Bot ko apne group mein add karo
2. Bot ko **admin** banao (with manage voice chats permission)
3. Assistant account ko bhi group mein add karo
4. Group mein VC start karo
5. `/play believer` type karo
6. Done! 🎉

## 📝 Notes

- Voice chat **pehle se start** hona chahiye group mein
- Assistant account = woh account jiska session string generate kiya
- Assistant account group mein hona zaroori hai
- Termux mein chalane ke liye phone hamesha on rakho

## 🐛 Troubleshooting

**`No active group call`** → Group mein pehle VC start karo  
**`PEER_ID_INVALID`** → Assistant account ko group mein add karo  
**FFmpeg errors** → `pkg install ffmpeg` karo Termux mein  
**`tgcrypto` install fail** → `pkg install rust binutils` karo
