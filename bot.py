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

    async def _check_db_channel(self):
        """Verifies bot is admin in DB Channel and sends a test message."""
        try:
            # Check if the bot is already verified as an admin
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel

            # You can store the message ID after sending it, so it doesn't get sent again.
            test_message_sent = False

            # Check if the bot has already sent the test message to avoid re-sending it
            async for message in self.get_chat_history(db_channel.id, limit=5):  # Check the last 5 messages
                if message.text == "Test Message":
                    test_message_sent = True
                    break

            # Send a test message if it hasn't been sent already
            if not test_message_sent:
                test = await self.send_message(chat_id=db_channel.id, text="Test Message")
                await test.delete()

        except Exception as e:
            self.LOGGER(__name__).warning(f"Failed to verify DB channel: {e}")
            self.LOGGER(__name__).warning(f"Make sure bot is admin in DB Channel and double-check the CHANNEL_ID value.")
            sys.exit()

    async def send_file_to_db_channel(self, file):
        """Send a file to the database channel, but only if it hasn't been sent before."""
        sent_files = set()  # Ideally, store this in a database or a persistent file

        # Check if the file has already been sent
        if file.file_id in sent_files:
            self.LOGGER(__name__).info(f"File {file.file_id} already sent, skipping...")
            return

        # Send the file if it hasn't been sent before
        await self.send_document(CHANNEL_ID, file)
        sent_files.add(file.file_id)  # Add the file ID to the set of sent files

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
