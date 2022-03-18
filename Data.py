from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
ʜᴇʏ {}

sᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ ᴅɪ {}

ɴᴏᴛᴇ : 
1) ᴊᴀɴɢᴀɴ ʙʟᴏᴄᴋ ʙᴏᴛ ɪɴɪ
2) ᴋᴀʀᴇɴᴀ ᴋᴀᴍᴜ ᴛɪᴅᴀᴋ ᴀᴋᴀɴ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ sᴛʀɪɴɢ ᴍᴜ ᴊɪᴋᴀ ᴋᴀᴍᴜ ʙʟᴏᴄᴋ ʙᴏᴛ ɪɴɪ

ᴀɴᴅᴀ ᴅᴀᴘᴀᴛ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ sᴀʏᴀ ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀsɪʟᴋᴀɴ sᴇssɪᴏɴ sᴛʀɪɴɢ ᴘʏʀᴏɢʀᴀᴍ ᴅᴀɴ ᴛᴇʟᴇᴛʜᴏɴ. ɢᴜɴᴀᴋᴀɴ ᴛᴏᴍʙᴏʟ ᴅɪʙᴀᴡᴀʜ ɪɴɪ ᴜɴᴛᴜᴋ ᴛᴀʜᴜ ʟᴇʙɪʜ ʙᴀɴʏᴀᴋ!
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("⚡ Mulai Ambil String ⚡", callback_data="generate")],
        [InlineKeyboardButton(text="🔄 Kembali 🔄", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("⚡ Mulai Ambil String ⚡", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("⚡ Mulai Ambil String ⚡", callback_data="generate")],
        [InlineKeyboardButton("🔥 Dikelola Oleh 🔥", url="https://t.me/JustRex")],
        [
            InlineKeyboardButton("Cara Pakai ❔", callback_data="help"),
            InlineKeyboardButton("⚠️ Tentang ⚠️", callback_data="about")
        ],
        [InlineKeyboardButton("⚡ Venz Groups ⚡", url="https://t.me/justvenzzz")],
    ]

    # Help Message
    HELP = """
⌨ **Available Commands** ⌨

/about - Untuk Mengetahui Tentang Ini 🤖
/help - Periksa Perintah Bot 🔧
/start - Mulai Bot
/generate - Mulai Mengambil String Anda ✨
/cancel - Membatalkan Proses ❌
/restart - Mulai Ulang Dan Mulai Hasilkan String 💯
"""

    # About Message
    ABOUT = """
**About This Bot** 

Bot Telegram Untuk Menghasilkan Sesi Pyrogram Dan String Telethon...

Venz Support : [VENZ SUPPORT](https://t.me/justvenzzz)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @moonscrsh
    """
