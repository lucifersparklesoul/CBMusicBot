import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQE1hZwAOazZq8HBJL49vntLUnHlLqWUu_Jsndkx4kFXnj2dlS2k8nwFipW5YYcJti6jJOj0NxlkgoDIb47sw0hCg33sgSVk7MkG1ruF3iMRzupkg0T9i8f-1I3Od_SbX2Ae0o1hHbZI_2HRF-KIrVyKSG_uisUUhwoYkPsdrLFVVDTBJ9lUsuUsY-P0V5lgeog2pv2PAQpgJg94iCKO7Wt3GKVE3ZNwddJyL3nw0uvqET-E391UJ4BZ2V3QC2mPOapWIJuMZG6nT6DfNStQtVveKdrjT_18WYDvaNQGZo48PMVs1F2SlX-pXepUh4yZujoes5GCQrScor7KEsaYmBceOZCfSwAAAAHdtb5_AA")
BOT_TOKEN = getenv("8503980326:AAH9d0IljJ33UlDz5OsuGdMxFIDqFbt5lhw")
BOT_NAME = getenv("BOT_NAME", "𝙰𝙻𝚈𝙰 ᴍᴜsɪᴄ ʙᴏᴛ")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/6790864f5fe27471bdc8d.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/e9a4d6655e5ddf51f9160.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/91034f175d41040d45b38.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/c8a0e9c544c5ea689caf9.jpg")
API_ID = int(getenv("38410931"))
API_HASH = getenv("7f3214c1088398018d37c21dddae7c44")
BOT_USERNAME = getenv("BOT_USERNAME", "Ruabw_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "𝐂𝐑𝐎𝐒𝐒 Helper")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "SupportGroup")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "MusicProject")
OWNER_NAME = getenv("OWNER_NAME", "༒☬ $asuke ☬༒") # isi dengan username kamu tanpa simbol @
PMPERMIT = getenv("PMPERMIT", None)
OWNER_ID = int(os.environ.get("8218405121")) # fill with your id as the owner of the bot
DATABASE_URL = os.environ.get("mongodb+srv://rj5706603:O95nvJYxapyDHfkw@cluster0.fzmckei.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # fill with your mongodb url
LOG_CHANNEL = int(os.environ.get("-1002742904374")) # make a private channel and get the channel id
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False)) # just fill with True or False (optional)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
LANG = getenv("LANG", "id")
