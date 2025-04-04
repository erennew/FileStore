import os
from os import environ, getenv
import logging
from logging.handlers import RotatingFileHandler

# Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7598604465:AAHmYBl6oxcJBNgSCuF9p41I9lHkiB0PXjU")  # Update with your actual token
# Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "24500584"))
# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "449da69cf4081dc2cc74eea828d0c490")
# Your db channel Id
CHANNEL_IDS = [int(x) for x in os.environ.get("CHANNEL_ID", "").split(",") if x]
# NAMA OWNER
OWNER = os.environ.get("OWNER", "senku")
# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1047253913"))
# Port
PORT = os.environ.get("PORT", "8000")
# Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://erenyeagermikasa84:<pkbOXb3ulzi9cEFd>@cluster0.ingt8mt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

# Time in seconds for message delete, put 0 to never delete
TIME = int(os.environ.get("TIME", "900"))

START_GIFS = os.getenv("START_GIFS", "").split(",")
END_GIFS = os.getenv("END_GIFS", "").split(",")

# Force subscription channel IDs (0 to disable)
FORCE_SUB_CHANNEL1 = int(os.environ.get("FORCE_SUB_CHANNEL1", "-1002650862527"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002331321194"))
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "-1001956677010"))
FORCE_SUB_CHANNEL4 = int(os.environ.get("FORCE_SUB_CHANNEL4", "-1002508438247"))

# Set the number of workers for the bot
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_GIFS = os.getenv("START_GIFS", "").split(",")
END_GIFS = os.getenv("END_GIFS", "").split(",")
# Start Image URL
START_PIC = os.environ.get("START_PIC", "https://i.ibb.co/F4ytZfyG/x.jpg")
# Force Subscription Image URL
FORCE_PIC = os.environ.get("FORCE_PIC", "https://i.ibb.co/FqK4HFX4/x.jpg")

# Enable Token for specific purposes
TOKEN = False if os.environ.get('TOKEN', "True") == "True" else False
SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "https://example.com")  # Change to a placeholder or irrelevant URL
SHORTLINK_API = os.environ.get("SHORTLINK_API", "dummy_api_key")  # Replace with a dummy key or keep it disabled
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 0))  # Set to 0 to disable expiration
IS_VERIFY = os.environ.get("IS_VERIFY", "False")  # Set to "False" to turn off verification
TUT_VID = os.environ.get("TUT_VID", "")  # Empty or change to a different irrelevant URL


# Help text for the bot

HELP_TXT = "<b><blockquote>ᴛʜɪs ɪs ᴀɴ ғɪʟᴇ ᴛᴏ ʟɪɴᴋ ʙᴏᴛ ᴡᴏʀᴋ ғᴏʀ @Culturedteluguweeb\n\n❏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs\n├/start : sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n├/about : ᴏᴜʀ Iɴғᴏʀᴍᴀᴛɪᴏɴ\n└/help : ʜᴇʟᴘ ʀᴇʟᴀᴛᴇᴅ ʙᴏᴛ\n\n sɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ ʙᴏᴛʜ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ.....!</blockquote></b>"

# About text for the bot
ABOUT_TXT = "<b><blockquote>◈ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/CulturedTeluguweeb> ᴄᴜʟᴛᴜʀᴇᴅ ᴡᴇᴇʙ </a>\n◈ ᴏɴɢᴏɪɴɢ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/+BiVvkpD5ieIxZTNl>ᴏɴɢᴏɪɴɢ ᴄᴛᴡ </a>\n◈ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴀɴɪᴍᴇꜱ : <a href=https://t.me/+uCZlBWrgKCMyYmI1>ᴄᴛᴡ ᴀɴɪᴅᴇx</a></blockquote></b>"

# Start message for the bot
START_MSG = os.environ.get("START_MESSAGE", "<blockquote><b> 𝐇𝐈 {first}✨ Cᴏᴍᴇ ғᴏʀ ᴛʜᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ, ᴅᴏɴ'ᴛ ᴍɪss ᴍʏ ᴄᴏᴏᴋɪɴɢ! <blockquote></b>\n<blockquote> The perfect dish can heal the soul! .</blockquote></b>")

try:
    ADMINS = [6376328008]  # Owner and Admins list
    for x in (os.environ.get("ADMINS", "5115691197 6273945163 6103092779 5231212075 7328629001").split()):
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

# Force subscription message
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<blockquote><b> ʜᴇʟʟᴏ {first}✌️<blockquote></b> \n\n<blockquote>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</blockquote></b>")

# Custom Caption for files
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<blockquote>• ʙʏ @Culturedteluguweeb<blockquote></b>")

# Set to True if you want to protect content (prevent forwarding)
PROTECT_CONTENT = False if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

# Set to True to disable channel posts share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'False'

# Bot uptime text format
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"

# Admin Reply Text (If needed)
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!"

# Add more Admins if needed
ADMINS.append(OWNER_ID)
ADMINS.append(7187218010)

# Log file name for bot operations
LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
