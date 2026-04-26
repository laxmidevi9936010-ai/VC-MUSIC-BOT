"""
Premium small caps font converter
sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ style
"""

SMALL_CAPS = {
    'a': 'ᴀ', 'b': 'ʙ', 'c': 'ᴄ', 'd': 'ᴅ', 'e': 'ᴇ',
    'f': 'ғ', 'g': 'ɢ', 'h': 'ʜ', 'i': 'ɪ', 'j': 'ᴊ',
    'k': 'ᴋ', 'l': 'ʟ', 'm': 'ᴍ', 'n': 'ɴ', 'o': 'ᴏ',
    'p': 'ᴘ', 'q': 'ǫ', 'r': 'ʀ', 's': 's', 't': 'ᴛ',
    'u': 'ᴜ', 'v': 'ᴠ', 'w': 'ᴡ', 'x': 'x', 'y': 'ʏ',
    'z': 'ᴢ',
}

def font(text: str) -> str:
    """Convert text to premium small caps font"""
    result = ""
    for ch in text:
        lower = ch.lower()
        if lower in SMALL_CAPS:
            result += SMALL_CAPS[lower]
        else:
            result += ch
    return result
