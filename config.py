#(©)t.me/CodeFlix_Bots




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7285500774:AAEfpvgj8EX43bCxx3qWhKsFtSwUwqgEOyw")
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "22213072"))
#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "8ec41c246b5074ab926933fb286fb43f")
#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002341804786"))
# NAMA OWNER
OWNER = os.environ.get("OWNER", "urr_trafalgar")
#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7263364323"))
#Port
PORT = os.environ.get("PORT", "8030")
#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://sagatobots00001:sagatobots100@cluster00001.vgdshkw.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "Hanabi_Hyuga_Probot")
#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "--1002203092644"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002318887893"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_PIC = os.environ.get("START_PIC", "https://envs.sh/IiW.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://envs.sh/IiB.jpg")

HELP_TXT = "<b>ᴛʜɪs ɪs ᴀ ʜᴇɴᴛᴀɪ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ ᴡᴏʀᴋ ғᴏʀ <a href=https://t.me/+PaCAA6D2RnBlYmVl>𝐅ʟᴜx 𝐇ᴇɴᴛᴀɪ</a>\n\n❏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs\n├/start : sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n├/about : ᴏᴜʀ Iɴғᴏʀᴍᴀᴛɪᴏɴ\n└/help : ʜᴇʟᴘ ʀᴇʟᴀᴛᴇᴅ ʙᴏᴛ\n\nsɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ ʙᴏᴛʜ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ.....!\n\n𝐌ᴀɪɴ 𝐂ʜᴀɴɴᴇʟ : <a href=https://t.me/+PaCAA6D2RnBlYmVl>𝐅ʟᴜx 𝐇ᴇɴᴛᴀɪ</a></b>"
ABOUT_TXT = "<b>◈ ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/urr_trafalgar>Trafalgar D. Law</a>\n◈ ᴍᴇᴍʙᴇʀ ᴏꜰ : <a href=https://t.me/Straw_Hat_Bots>𝐒ᴛʀᴀᴡ 𝐇ᴀᴛ 𝐁ᴏᴛs</a>\n◈ ʜᴇᴍᴛᴀɪ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/+PaCAA6D2RnBlYmVl>𝐅ʟᴜx 𝐇ᴇɴᴛᴀɪ</a>\n◈ ᴍᴏᴠɪᴇ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/Movies_Castlevania>𝐂ᴀsᴛʟᴇ 𝐕ᴀɴɪᴀ</a>\n◈ ʜɪɴᴅɪ sᴜʙ ᴀɴɪᴍᴇ : <a href=https://t.me/anime_flux>𝐀ɴɪᴍᴇ 𝐅ʟᴜx</a>\n◈ ʜɪɴᴅɪ ᴅᴜʙ ᴀɴɪᴍᴇ : <a href=https://t.me/Anime_Multiverse_Hindi>𝐂ʀᴜɴᴄʜʏʀᴏʟʟ</a>\n◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/Straw_Hat_Bots>𝐒ᴀɴᴊɪ 𝐒ᴀᴍᴀ</a></b>"
START_MSG = os.environ.get("START_MESSAGE", "<b>𝐊ᴏɴɴɪᴄʜɪᴡᴀ!! {mention}⚡,\n\nɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.\n\n𝐌ᴀɪɴ 𝐂ʜᴀɴɴᴇʟ : <a href='https://t.me/+PaCAA6D2RnBlYmVl'>𝐅ʟᴜx 𝐇ᴇɴᴛᴀɪ</a></b>")
try:
    ADMINS=[6727550037]
    for x in (os.environ.get("ADMINS", "1683225887 5961139833 6727550037 7263364323 7162615398").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>𝐊ᴏɴɴɪᴄʜɪᴡᴀ!! {mention}✨,\n\nᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴄʟɪᴄᴋ ᴏɴ • ᴛʀʏ ᴀɢᴀɪɴ • ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.\n\n𝐌ᴀɪɴ 𝐂ʜᴀɴɴᴇʟ : <a href='https://t.me/+PaCAA6D2RnBlYmVl'>𝐅ʟᴜx 𝐇ᴇɴᴛᴀɪ</a></b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!\n\nᴍʏ ᴏᴡɴᴇʀ : @Anime_Flux ..."

ADMINS.append(OWNER_ID)
ADMINS.append(7316619429)

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
   
   