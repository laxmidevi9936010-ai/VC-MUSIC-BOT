"""
🎵 PREMIUM VC MUSIC BOT 🎵
Termux mein run: python main.py
"""
import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup,
    Message, CallbackQuery
)
from pyrogram.enums import ChatType
from pytgcalls import PyTgCalls
from pytgcalls.types import MediaStream, AudioQuality

from config import API_ID, API_HASH, BOT_TOKEN, ASSISTANT_SESSION, START_IMAGE
from fonts import font
from youtube import search_youtube, download_audio, duration_to_seconds
from blur import send_blurred_photo

# ===== Clients =====
bot = Client(
    "musicbot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

assistant = Client(
    "assistant",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=ASSISTANT_SESSION,
)

call_py = PyTgCalls(assistant)

# ===== State =====
# chat_id -> {"file": path, "title": str, "duration": int, "position": int, "url": str}
active_streams = {}


# ============ HELPERS ============
def player_buttons(chat_id: int, duration_text: str):
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(font(f"⏱ {duration_text}"), callback_data="noop"),
        ],
        [
            InlineKeyboardButton("⏪ -10s", callback_data=f"seek_back_{chat_id}"),
            InlineKeyboardButton("⏸ Pause", callback_data=f"pause_{chat_id}"),
            InlineKeyboardButton("▶️ Play", callback_data=f"resume_{chat_id}"),
            InlineKeyboardButton("+10s ⏩", callback_data=f"seek_fwd_{chat_id}"),
        ],
        [
            InlineKeyboardButton(font("⏹ Stop"), callback_data=f"stop_{chat_id}"),
        ],
    ])


def start_buttons():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(font("➕ Add Me To Group"),
                                 url="https://t.me/your_bot_username?startgroup=true"),
        ],
        [
            InlineKeyboardButton(font("📚 Help"), callback_data="help"),
            InlineKeyboardButton(font("👤 Owner"), url="https://t.me/your_username"),
        ],
        [
            InlineKeyboardButton(font("💬 Support"), url="https://t.me/your_support"),
        ],
    ])


def help_buttons():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(font("« Back"), callback_data="start")],
    ])


# ============ COMMANDS ============
@bot.on_message(filters.command("start") & filters.private)
async def start_private(_, m: Message):
    text = (
        f"{font('Hey')} {m.from_user.mention} 👋\n\n"
        f"{font('I am a Premium VC Music Bot')} 🎵\n\n"
        f"{font('I can play music in your group voice chat from YouTube and Spotify.')}\n\n"
        f"{font('Add me to your group, promote as admin, and use /play song name')} ✨"
    )
    await m.reply_photo(
        photo=START_IMAGE,
        caption=text,
        reply_markup=start_buttons(),
    )


@bot.on_message(filters.command("start") & filters.group)
async def start_group(_, m: Message):
    await m.reply_text(
        font(f"Hello! I am alive in this group. Use /play song_name to start music."),
    )


@bot.on_message(filters.command("help"))
async def help_cmd(_, m: Message):
    text = (
        f"📚 {font('Help Menu')}\n\n"
        f"🎵 /play <song name> — {font('Play song from YouTube')}\n"
        f"⏸ /pause — {font('Pause current song')}\n"
        f"▶️ /resume — {font('Resume song')}\n"
        f"⏹ /stop — {font('Stop and leave VC')}\n"
        f"⏭ /skip — {font('Skip current song')}\n"
        f"🔁 /ping — {font('Check bot status')}\n\n"
        f"{font('Tip: Make sure I am admin and VC is started in your group.')}"
    )
    await m.reply_text(text)


@bot.on_message(filters.command("ping"))
async def ping(_, m: Message):
    await m.reply_text(font("Pong! Bot is alive ✨"))


# ============ PLAY ============
@bot.on_message(filters.command("play") & filters.group)
async def play(_, m: Message):
    if len(m.command) < 2 and not m.reply_to_message:
        return await m.reply_text(font("Usage: /play song name"))

    query = " ".join(m.command[1:]) if len(m.command) > 1 else m.reply_to_message.text
    status = await m.reply_text(font("🔍 Searching..."))

    info = await search_youtube(query)
    if not info:
        return await status.edit(font("❌ No results found."))

    await status.edit(font("⬇️ Downloading audio..."))
    try:
        file_path = await download_audio(info["link"])
    except Exception as e:
        return await status.edit(font(f"❌ Download failed: {e}"))

    chat_id = m.chat.id
    duration_seconds = duration_to_seconds(info["duration"])

    # Join VC and play
    try:
        await call_py.play(
            chat_id,
            MediaStream(
                file_path,
                audio_parameters=AudioQuality.HIGH,
            ),
        )
    except Exception as e:
        return await status.edit(font(f"❌ VC error: {e}\n\nMake sure VC is started in this group."))

    active_streams[chat_id] = {
        "file": file_path,
        "title": info["title"],
        "duration": duration_seconds,
        "url": info["link"],
        "thumb": info["thumbnail"],
    }

    await status.delete()

    caption = (
        f"🎵 {font('Started Successfully')}\n\n"
        f"🎶 {font('Title')}: {info['title']}\n"
        f"⏱ {font('Duration')}: {info['duration']}\n"
        f"👁 {font('Views')}: {info['views']}\n"
        f"📺 {font('Channel')}: {info['channel']}\n"
        f"🙋 {font('Requested by')}: {m.from_user.mention}"
    )

    try:
        await m.reply_photo(
            photo=info["thumbnail"],
            caption=caption,
            reply_markup=player_buttons(chat_id, info["duration"]),
        )
    except Exception:
        await m.reply_text(caption, reply_markup=player_buttons(chat_id, info["duration"]))


# ============ CONTROLS ============
@bot.on_message(filters.command("pause") & filters.group)
async def pause(_, m: Message):
    try:
        await call_py.pause_stream(m.chat.id)
        await m.reply_text(font("⏸ Paused"))
    except Exception as e:
        await m.reply_text(font(f"Error: {e}"))


@bot.on_message(filters.command("resume") & filters.group)
async def resume(_, m: Message):
    try:
        await call_py.resume_stream(m.chat.id)
        await m.reply_text(font("▶️ Resumed"))
    except Exception as e:
        await m.reply_text(font(f"Error: {e}"))


@bot.on_message(filters.command(["stop", "end"]) & filters.group)
async def stop(_, m: Message):
    try:
        await call_py.leave_call(m.chat.id)
        active_streams.pop(m.chat.id, None)
        await m.reply_text(font("⏹ Stopped & left VC"))
    except Exception as e:
        await m.reply_text(font(f"Error: {e}"))


# ============ CALLBACKS ============
@bot.on_callback_query()
async def cb(_, q: CallbackQuery):
    data = q.data

    if data == "noop":
        return await q.answer()

    if data == "help":
        text = (
            f"📚 {font('Help Menu')}\n\n"
            f"🎵 /play <song> — {font('Play music')}\n"
            f"⏸ /pause — {font('Pause')}\n"
            f"▶️ /resume — {font('Resume')}\n"
            f"⏹ /stop — {font('Stop')}\n"
        )
        return await q.message.edit_caption(caption=text, reply_markup=help_buttons())

    if data == "start":
        text = (
            f"{font('Hey')} {q.from_user.mention} 👋\n\n"
            f"{font('I am a Premium VC Music Bot')} 🎵"
        )
        return await q.message.edit_caption(caption=text, reply_markup=start_buttons())

    if data.startswith("pause_"):
        chat_id = int(data.split("_")[1])
        try:
            await call_py.pause_stream(chat_id)
            await q.answer(font("Paused"), show_alert=False)
        except Exception as e:
            await q.answer(str(e), show_alert=True)

    elif data.startswith("resume_"):
        chat_id = int(data.split("_")[1])
        try:
            await call_py.resume_stream(chat_id)
            await q.answer(font("Resumed"), show_alert=False)
        except Exception as e:
            await q.answer(str(e), show_alert=True)

    elif data.startswith("stop_"):
        chat_id = int(data.split("_")[1])
        try:
            await call_py.leave_call(chat_id)
            active_streams.pop(chat_id, None)
            await q.answer(font("Stopped"), show_alert=False)
            await q.message.edit_caption(caption=font("⏹ Stream stopped."))
        except Exception as e:
            await q.answer(str(e), show_alert=True)

    elif data.startswith("seek_back_") or data.startswith("seek_fwd_"):
        # Seeking requires re-streaming with offset - simplified notice
        await q.answer(font("Seek will be supported soon ⏱"), show_alert=False)


# ============ PHOTO BLUR FEATURE ============
@bot.on_message(filters.photo & filters.private & ~filters.command(["start"]))
async def blur_photo(_, m: Message):
    """Jab user image bheje, bot blur version bhej dega - click karte hi original"""
    file_path = await m.download()
    try:
        await send_blurred_photo(
            bot, m.chat.id, file_path,
            caption=font("🔒 Tap to reveal")
        )
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)


# ============ MAIN ============
async def main():
    print("Starting bot...")
    await bot.start()
    await assistant.start()
    await call_py.start()
    me = await bot.get_me()
    print(f"✅ Bot started as @{me.username}")
    print("✅ Assistant started")
    print("✅ PyTgCalls started")
    print("Bot is now running. Press Ctrl+C to stop.")
    await asyncio.Event().wait()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nBot stopped.")
