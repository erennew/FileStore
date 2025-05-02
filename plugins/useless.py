from bot import Bot
from pyrogram.types import Message
from pyrogram import filters
from config import ADMINS, BOT_STATS_TEXT, USER_REPLY_TEXT
from datetime import datetime
from helper_func import get_readable_time

@Bot.on_message(filters.command('stats') & filters.user(ADMINS))
async def stats(bot: Bot, message: Message):
    now = datetime.now()
    delta = now - bot.uptime
    time = get_readable_time(delta.seconds)
    await message.reply(BOT_STATS_TEXT.format(uptime=time))
    
WAIT_MSGS = [
    "<b>🔥 Cooking up your request, love~ Just a moment... 🕺🍽️</b>",
    "<b>👨‍🍳 Chef Sanji’s on it! Your file is being prepared with love... ❤️‍🔥</b>",
    "<b>💨 Preheating the kitchen! Sanji-style speed incoming... 🍷💋</b>",
    "<b>🍜 Stirring the spices... Your file is almost ready, sweetheart~ 😘</b>",
    "<b>🍷 Let’s make it perfect — just like a romantic dinner! Wait a sec~</b>",
    "<b>💋 Anything for a beautiful user like you~ Preparing your file now 😌</b>",
    "<b>🔥 Just like my cooking — I’m serving your request hot and fresh!</b>",
    "<b>🧑‍🍳 The prince of the kitchen is on it... stay gorgeous while you wait~ 💛</b>",
    "<b>🍖 Grilling your file with love and flavor... Almost done, mon chéri~</b>",
    "<b>💃 A dish for a queen! File incoming, just a sec my lady~ 💐</b>",
    "<b>🍽️ Gourmet mode: ON — prepping your file with elegance and spice~</b>",
    "<b>❤️‍🔥 File loading... like my passion in the kitchen~</b>",
    "<b>👠 Serving beauty and bytes — your file’s on the way, angel~</b>",
    "<b>🕶️ Cool, classy, and delicious — your file is almost plated!</b>",
    "<b>💎 Sanji never rushes perfection. File’s nearly ready, darling~</b>"
]

#=====================================================================================##


WAIT_MSG = random.choice(WAIT_MSGS)

#=====================================================================================##


@Bot.on_message(filters.command('users') & filters.private & admin)
async def get_users(client: Bot, message: Message):
    msg = await client.send_message(chat_id=message.chat.id, text=WAIT_MSG)
    users = await db.full_userbase()
    await msg.edit(f"{len(users)} users are using this bot")


@Bot.on_message(filters.private & filters.command('dlt_time') & admin)
async def set_delete_time(client: Bot, message: Message):
    try:
        duration = int(message.command[1])

        await db.set_del_timer(duration)

        await message.reply(f"<b>Dᴇʟᴇᴛᴇ Tɪᴍᴇʀ ʜᴀs ʙᴇᴇɴ sᴇᴛ ᴛᴏ <blockquote>{duration} sᴇᴄᴏɴᴅs.</blockquote></b>")

    except (IndexError, ValueError):
        await message.reply("<b>Pʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴠᴀʟɪᴅ ᴅᴜʀᴀᴛɪᴏɴ ɪɴ sᴇᴄᴏɴᴅs.</b> Usage: /dlt_time {duration}")

@Bot.on_message(filters.private & filters.command('check_dlt_time') & admin)
async def check_delete_time(client: Bot, message: Message):
    duration = await db.get_del_timer()

    await message.reply(f"<b><blockquote>Cᴜʀʀᴇɴᴛ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇʀ ɪs sᴇᴛ ᴛᴏ {duration}sᴇᴄᴏɴᴅs.</blockquote></b>")

