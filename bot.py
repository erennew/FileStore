class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={"root": "plugins"},
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

        # FORCE SUB CHANNELS INVITE LINKS
        force_sub_channels = {
            "FORCE_SUB_CHANNEL1": FORCE_SUB_CHANNEL1,
            "FORCE_SUB_CHANNEL2": FORCE_SUB_CHANNEL2,
            "FORCE_SUB_CHANNEL3": FORCE_SUB_CHANNEL3,
            "FORCE_SUB_CHANNEL4": FORCE_SUB_CHANNEL4
        }

        for key, channel_id in force_sub_channels.items():
            if channel_id:
                try:
                    chat = await self.get_chat(channel_id)
                    link = chat.invite_link or await self.export_chat_invite_link(channel_id)
                    setattr(self, f"invitelink{key[-1]}", link)
                except Exception as e:
                    self.LOGGER(__name__).warning(e)
                    self.LOGGER(__name__).warning(
                        f"Bot can't export invite link from {key}. Make sure the bot is admin and has 'invite via link' permission.\n"
                        f"Current Value: {channel_id}"
                    )
                    self.LOGGER(__name__).info("Bot Stopped. Join https://t.me/weebs_support for help.")
                    sys.exit()

        # ✅ Validate ALL DB Channels in CHANNEL_IDS
        for cid in CHANNEL_IDS:
            try:
                db_channel = await self.get_chat(cid)
                test = await self.send_message(chat_id=cid, text="✅ Bot is Active and Has Admin Access")
                await test.delete()
            except Exception as e:
                self.LOGGER(__name__).warning(e)
                self.LOGGER(__name__).warning(
                    f"Make sure bot is admin in DB Channel {cid}, and double check your CHANNEL_ID env variable."
                )
                self.LOGGER(__name__).info("Bot Stopped. Join https://t.me/weebs_support for support.")
                sys.exit()

        self.set_parse_mode(ParseMode.HTML)
        self.username = usr_bot_me.username
        self.LOGGER(__name__).info("Bot Running...! Made by @Cultuedteluguweeb")

        # Start Web Server
        app = web.AppRunner(await web_server())
        await app.setup()
        await web.TCPSite(app, "0.0.0.0", PORT).start()

        try:
            await self.send_message(OWNER_ID, text="<b><blockquote>🤖 Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ </blockquote></b>")
        except:
            pass

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")
        from pyrogram import filters
from pyrogram.types import Message
import random

ANIME_GIFS = [
    "https://media.giphy.com/media/11kEuHSQAXXiGQ/giphy.gif",
    "https://media.giphy.com/media/XIqCQx02E1U9W/giphy.gif",
    "https://media.giphy.com/media/v6aOjy0Qo1fIA/giphy.gif"
]

@Bot.on_message(filters.text & filters.private)
async def anime_reply(_, message: Message):
    gif = random.choice(ANIME_GIFS)
    await message.reply_animation(animation=gif, caption="✨ I only work for my master @CulturedTeluguweeb-sama~ 🌸")


    def run(self):
        """Run the bot."""
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.start())
        self.LOGGER(__name__).info("Bot is now running. Thanks to @rohit_1888")
        try:
            loop.run_forever()
        except KeyboardInterrupt:
            self.LOGGER(__name__).info("Shutting down...")
        finally:
            loop.run_until_complete(self.stop())
