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
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002659351510"))
# NAMA OWNER
OWNER = os.environ.get("OWNER", "roxcy")
# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1047253913"))
# Port
PORT = os.environ.get("PORT", "8000")
# Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://erenyeagermikasa84:<pkbOXb3ulzi9cEFd>@cluster0.ingt8mt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

# Time in seconds for message delete, put 0 to never delete
TIME = int(os.environ.get("TIME", "30"))

# Force subscription channel IDs (0 to disable)
FORCE_SUB_CHANNEL1 = int(os.environ.get("FORCE_SUB_CHANNEL1", "-1002650862527"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "0"))
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "0"))
FORCE_SUB_CHANNEL4 = int(os.environ.get("FORCE_SUB_CHANNEL4", "0"))

# Set the number of workers for the bot
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Start Image URL
START_PIC = os.environ.get("START_PIC", "https://i.ibb.co/fdtSRzz3/x.jpg")
# Force Subscription Image URL
FORCE_PIC = os.environ.get("FORCE_PIC", "https://telegra.ph/file/e292b12890b8b4b9dcbd1.jpg")

# Enable Token for specific purposes
TOKEN = True if os.environ.get('TOKEN', "False") == "False" else False 
# Shortlink settings
SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "publicearn.online")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "adabe1c0675be8ffc5ccbc84a9a65bc5a5d3ec69")
# Verify Expiry time (in seconds)
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 600))  # Add time in seconds
# Verification status
IS_VERIFY = os.environ.get("IS_VERIFY", "False")
# Tutorial video link
TUT_VID = os.environ.get("TUT_VID", "https://t.me/hwdownload/3")

# Help text for the bot
HELP_TXT = "<b><blockquote>ᴛʜɪs ɪs ᴀɴ ғɪʟᴇ ᴛᴏ ʟɪɴᴋ ʙᴏᴛ ᴡᴏʀᴋ ғᴏʀ @Cultuedteluguweeb\n\n❏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs\n├/start : sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n├/about : ᴏᴜʀ Iɴғᴏʀᴍᴀᴛɪᴏɴ\n└/help : ʜᴇʟᴘ ʀᴇʟᴀᴛᴇᴅ ʙᴏᴛ\n\n sɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ ʙᴏᴛʜ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ.....!\n\n ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ <a href=https://t.me/cosmic_freak>sᴜʙᴀʀᴜ</a></blockquote></b>"

# About text for the bot
ABOUT_TXT = "<b><blockquote>◈ ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/cosmic_freak>Yato</a>\n◈ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/otakuflix_network>ᴏᴛᴀᴋᴜғʟɪx ɴᴇᴛᴡᴏʀᴋ</a>\n◈ ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/anime_cruise_netflix>ᴀɴɪᴍᴇ ᴄʀᴜɪsᴇ</a>\n◈ sᴇʀɪᴇs ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/webseries_flix>ᴡᴇʙsᴇʀɪᴇs ғʟɪx</a>\n◈ ᴀᴅᴜʟᴛ ᴍᴀɴʜᴡᴀ : <a href=https://t.me/pornhwa_flix>ᴘᴏʀɴʜᴡᴀs</a>\n◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/cosmic_freak>subaru</a></blockquote></b>"

# Start message for the bot
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜᴇʟʟᴏ {first}\n\n<blockquote> The perfect dish can heal the soul! .</blockquote></b>")

try:
    ADMINS = [6376328008]  # Owner and Admins list
    for x in (os.environ.get("ADMINS", "5115691197 6273945163 6103092779 5231212075 7328629001").split()):
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

# Force subscription message
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}\n\n<b>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</b>")

# Custom Caption for files
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @Culturedteluguweeb</b>")

# Set to True if you want to protect content (prevent forwarding)
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

# Set to True to disable channel posts share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

# Bot uptime text format
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"

# Admin Reply Text (If needed)
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!"

# Add more Admins if needed
ADMINS.append(OWNER_ID)
ADMINS.append(6497757690)

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
