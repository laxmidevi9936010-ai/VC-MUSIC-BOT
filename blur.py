"""
Image blur helper - photo blur karke bhejta hai, click karne pe original
Telegram has 'has_spoiler=True' which gives blur effect natively
"""
from pyrogram.types import InputMediaPhoto


async def send_blurred_photo(client, chat_id, photo_path, caption=""):
    """Send photo with native Telegram spoiler/blur"""
    return await client.send_photo(
        chat_id=chat_id,
        photo=photo_path,
        caption=caption,
        has_spoiler=True,
    )
