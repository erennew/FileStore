from aiohttp import web
from plugins import web_server
import asyncio
import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime
from config import *

name = """
 BY CODEFLIX BOTS
"""

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        try:
            # Start the bot
            await super().start()
            usr_bot_me = await self.get_me()
            self.uptime = datetime.now()

            # Force subscription to channels
            await self._handle_force_subscription(FORCE_SUB_CHANNEL1, "invitelink1")
            await self._handle_force_subscription(FORCE_SUB_CHANNEL2, "invitelink2")
            await self._handle_force_subscription(FORCE_SUB_CHANNEL3, "invitelink3")
            await self._handle_force_subscription(FORCE_SUB_CHANNEL4, "invitelink4")

            # Verify DB channel connection
            await self._check_db_channel()

            # Set parse mode
            self.set_parse_mode(ParseMode.HTML)

            # Log bot running status
            self.LOGGER(__name__).info(f"Bot Running..! Created by \nhttps://t.me/weebs_support")
            self.LOGGER(__name__).info(f"""
  ___ ___  ___  ___ ___ _    _____  _____  ___ _____ ___ 
 / __/ _ \|   \| __| __| |  |_ _\ \/ / _ )/ _ \_   _/ __|
| (_| (_) | |) | _|| _|| |__ | | >  <| _ \ (_) || | \__  \
 \___\___/|___/|___|_| |____|___/_/\_\___/\___/ |_| |___/
                                                          """)

            self.set_parse_mode(ParseMode.HTML)
            self.username = usr_bot_me.username
            self.LOGGER(__name__).info(f"Bot Running..! Made by @Codeflix_Bots")

            # Start the web server
            await self._start_web_server()

            # Send bot restart notification to owner
            try:
                await self.send_message(OWNER_ID, text=f"<b><blockquote>🤖 Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ by @Codeflix_Bots</blockquote></b>")
            except Exception as e:
                self.LOGGER(__name__).warning(f"Failed to send restart message to owner: {e}")

        except Exception as e:
            self.LOGGER(__name__).error(f"Bot startup failed: {e}")
            sys.exit()

    async def _handle_force_subscription(self, force_sub_channel, invite_link_var_name):
        """Handles forced subscription to a channel and logs the outcome."""
        if force_sub_channel:
            try:
                link = (await self.get_chat(force_sub_channel)).invite_link
                if not link:
                    await self.export_chat_invite_link(force_sub_channel)
                    link = (await self.get_chat(force_sub_channel)).invite_link
                setattr(self, invite_link_var_name, link)  # Dynamically set the invite link attribute
            except Exception as a:
                self.LOGGER(__name__).warning(f"Error with Force Sub Channel: {force_sub_channel} - {a}")
                self.LOGGER(__name__).warning(f"Bot can't Export Invite link from {force_sub_channel}.")
                self.LOGGER(__name__).warning(f"Please double-check the {force_sub_channel} and permissions.")
                setattr(self, invite_link_var_name, None)  # Assign None if there's an issue

    async def _check_db_channel(self):
        """Verifies bot is admin in DB Channel and sends a test message."""
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id=db_channel.id, text="Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(f"Failed to verify DB channel: {e}")
            self.LOGGER(__name__).warning(f"Make sure bot is admin in DB Channel and double-check the CHANNEL_ID value.")
            sys.exit()

    async def _start_web_server(self):
        """Starts the web server."""
        try:
            app = web.AppRunner(await web_server())
            await app.setup()
            await web.TCPSite(app, "0.0.0.0", PORT).start()
            self.LOGGER(__name__).info(f"Web server started on port {PORT}")
        except Exception as e:
            self.LOGGER(__name__).error(f"Failed to start web server: {e}")
            sys.exit()

    async def stop(self, *args):
        """Stop the bot."""
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")

    def run(self):
        """Run the bot."""
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.start())
        self.LOGGER(__name__).info("Bot is now running. Thanks to @rohit_1888")
        try:
            loop.run_forever()
        except KeyboardInterrupt:
            self.LOGGER(__name__).info("Shutting down bot gracefully...")
        finally:
            loop.run_until_complete(self.stop())

