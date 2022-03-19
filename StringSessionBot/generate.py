from asyncio.exceptions import TimeoutError
from Data import Data
from pyrogram import Client, filters
from telethon import TelegramClient
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)

ERROR_MESSAGE = "Ups! Pengecualian terjadi! \n\n**Error** : {} " \
            "\n\nBeritahu di Grup Saya @justvenzzz Oh Errors 😱" \
            "informasi sensitif dan Anda jika ingin melaporkan ini sebagai " \
            "pesan kesalahan ini tidak dicatat oleh kami!"


@Client.on_message(filters.private & ~filters.forwarded & filters.command('generate'))
async def main(_, msg):
    await msg.reply(
        "Select Your String Telethon/Pyrogram",
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("Pyrogram", callback_data="pyrogram"),
            InlineKeyboardButton("Telethon", callback_data="telethon")
        ]])
    )


async def generate_session(bot, msg, telethon=False):
    await msg.reply("Seccusfully {} Session Generation...".format("Telethon" if telethon else "Pyrogram"))
    user_id = msg.chat.id
    api_id_msg = await bot.ask(user_id, 'Berikan saya `API_ID`', filters=filters.text)
    if await cancelled(api_id_msg):
        return
    try:
        api_id = int(api_id_msg.text)
    except ValueError:
        await api_id_msg.reply('Sent Your API_ID (which must be an integer). Please start generating session again.', quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    api_hash_msg = await bot.ask(user_id, 'Sekarang Berikan Saya `API_HASH`', filters=filters.text)
    if await cancelled(api_id_msg):
        return
    api_hash = api_hash_msg.text
    phone_number_msg = await bot.ask(user_id, 'Masukan `PHONE_NUMBER` To Get Your String. \nExample : `+628xxxxxxx`', filters=filters.text)
    if await cancelled(api_id_msg):
        return
    phone_number = phone_number_msg.text
    await msg.reply("Sending OTP...")
    if telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    else:
        client = Client(":memory:", api_id, api_hash)
    await client.connect()
    try:
        if telethon:
            code = await client.send_code_request(phone_number)
        else:
            code = await client.send_code(phone_number)
    except (ApiIdInvalid, ApiIdInvalidError):
        await msg.reply('`API_ID` and `API_HASH` kombinasi salah tolol. tolong start ulang.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError):
        await msg.reply('`PHONE_NUMBER` salah tolol. Silakan mulai membuat sesi lagi.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    try:
        phone_code_msg = await bot.ask(user_id, "Silakan periksa OTP di akun telegram resmi. Jika Anda mendapatkannya, kirim OTP ke sini setelah membaca format di bawah ini. \njika OTP `12345`, **tolong kirim seperti ini** `1 2 3 4 5`.", filters=filters.text, timeout=600)
        if await cancelled(api_id_msg):
            return
    except TimeoutError:
        await msg.reply('Batas waktu tercapai 10 menit. Silakan mulai membuat sesi lagi.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    phone_code = phone_code_msg.text.replace(" ", "")
    try:
        if telethon:
            await client.sign_in(phone_number, phone_code, password=None)
        else:
            await client.sign_in(phone_number, code.phone_code_hash, phone_code)
    except (PhoneCodeInvalid, PhoneCodeInvalidError):
        await msg.reply('OTP tidak valid. Silakan mulai membuat sesi lagi.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    except (PhoneCodeExpired, PhoneCodeExpiredError):
        await msg.reply('OTP sudah kadaluarsa. Silakan mulai membuat sesi lagi.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    except (SessionPasswordNeeded, SessionPasswordNeededError):
        try:
            two_step_msg = await bot.ask(user_id, 'Akun Anda telah mengaktifkan verifikasi dua langkah. Tolong berikan kata sandinya.', filters=filters.text, timeout=300)
        except TimeoutError:
            await msg.reply('Batas waktu tercapai 5 menit. Silakan mulai membuat sesi lagi.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
        try:
            password = two_step_msg.text
            if telethon:
                await client.sign_in(password=password)
            else:
                await client.check_password(password=password)
            if await cancelled(api_id_msg):
                return
        except (PasswordHashInvalid, PasswordHashInvalidError):
            await two_step_msg.reply('Kata Sandi yang Diberikan Tidak Valid. Silakan mulai membuat sesi lagi.', quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
    if telethon:
        string_session = client.session.save()
    else:
        string_session = await client.export_session_string()
    text = "**{} STRING SESSION** \n\n`{}` \n\nGenerated by @justvenzzz".format("TELETHON" if telethon else "PYROGRAM", string_session)
    await client.send_message("me", text)
    await client.disconnect()
    await phone_code_msg.reply("Berhasil {} sesi string. \n\nSekarang Cek/Pesan Tersimpan! \n\nBy @justvenzzz".format("telethon" if telethon else "pyrogram"))


async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("Proses dengan hati-hati!", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif "/restart" in msg.text:
        await msg.reply("Mulai Ulang Saya Dan Coba Lagi...!", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif msg.text.startswith("/"):  # Bot Commands
        await msg.reply("saya Berhasil Restart \nSekarang Hasilkan String Anda !", quote=True)
        return True
    else:
        return False


# @Client.on_message(filters.private & ~filters.forwarded & filters.command(['cancel', 'restart']))
# async def formalities(_, msg):
#     if "/cancel" in msg.text:
#         await msg.reply("Berhasil Diproses!", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
#         return True
#     elif "/restart" in msg.text:
#         await msg.reply("Mulai Ulang Saya Dan Coba Lagi...!", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
#         return True
#     else:
#         return False
