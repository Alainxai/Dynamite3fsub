#(©)Codexbotz
#Recoded By @Its_Tartaglia_Childe

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>┏━━━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━━━┓\n× ○ 𝐃ᴇᴠᴇʟᴏᴘᴇᴅ 𝐁ʏ : <a href='tg://user?id=5437374877'>ᴀʙʀᴀʜᴀᴍ™</a>\n× ○ 𝐀ɴɪᴍᴇ 𝐂ʜᴀᴛ : <a href='https://t.me/+04k5y7NJpdc0YTll'>ᴄʜᴀᴛ ʜᴜʙ</a>\n× ○ 𝐂ᴏᴍᴍᴜɴɪᴛʏ : <a href='https://t.me/Anime_Flix_Network'>ᴀɴɪᴍᴇ ꜰʟɪx ɴᴇᴛᴡᴏʀᴋ</a>\n┗━━━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━━━┛</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("☠️ ᴄʟᴏꜱᴇ ☠️", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
