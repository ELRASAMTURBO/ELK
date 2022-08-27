from modules.config import (
    START_PIC, 
    BOT_USERNAME,
    SUPPORT_GROUP,
    OWNER_USERNAME,
    UPDATES_CHANNEL,
)
from modules.helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message



@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_private(client: Client, message: Message):
 await message.reply_photo(
        photo=f"{START_PIC}",
        caption=f"""**╭──── • ⍟ • ────╮
⌁ 𝑆𝑂𝐔𝑅𝐶𝐸 𝐸𝐿𝑅𝐴𝑆𝐴𝑀 ’⚡
⌁ 𝐴𝑆𝐾 𝑇𝑂 𝑀𝑌 ’⚡
⌁ 𝐸𝐿𝑅𝐴𝑆𝐴𝑀 ’⚡
╰──── • ⍟ • ────╯
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎯 ¦ اضـفـني الى مـجمـوعـتك ¦ 🎯",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [
                    InlineKeyboardButton("🥇 ¦ المـــطور", url=f"https://t.me/{OWNER_USERNAME}"),
                    InlineKeyboardButton("🖥 ¦ الأوامــر", url=f"https://telegra.ph/%D8%A7%D9%87%D9%84%D8%A7-%D8%A8%D9%83-%D8%AC%D9%85%D9%8A%D8%B9-%D8%A7%D9%84%D8%A7%D9%88%D8%A7%D9%85%D8%B1-%D8%B9%D8%B1%D8%A8%D9%8A%D9%87-%D9%8A%D9%85%D9%83%D9%86%D9%83-%D8%AA%D8%B4%D8%BA%D9%8A%D9%84-%D9%81%D9%8A-%D8%A7%D9%84%D8%A7%D9%88%D8%A7%D9%85%D8%B1-%D8%A7%D9%84%D8%A7%D8%AC%D9%86%D8%A8%D9%8A%D9%87-%D8%A7%D9%8A%D8%B6%D8%A2-%D9%88%D8%B4%D9%83%D8%B1%D8%A7-%D9%84%D9%83%D9%85-07-01"),
                ],
                [
                    InlineKeyboardButton(
                        "🥇 ¦ الــكروب", url=f"{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
                        "⚙️ ¦ الـسـورس", url=f"{UPDATES_CHANNEL}"
                    ),
                ],
            ]
        ),
    )


