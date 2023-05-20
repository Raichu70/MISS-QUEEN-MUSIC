import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
OWNER_ID = list(map(int, getenv("OWNER_ID").split()))
API_HASH = getenv("API_HASH")
MONGODB_URL = getenv("MONGODB_URL")
OWNER_NAME = getenv("OWNER_NAME", "MAFIAQUEEN")
ALIVE_NAME = getenv("ALIVE_NAME", "QUEEN MUSIC QN")
BOT_USERNAME = getenv("BOT_USERNAME", "MISS_QUEEN_MUSIC_BOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "QN QUEEN ASSISTANT")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "QUEEN_SUPPORTS_CHAT")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "QUEEN_NETWORK")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/b31fe4b7eefd373ff9031.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Professor-Ashu/M.V._PLAYER")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/ba61dc70493114fa362d5.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/29cf973aeffe9b47d545c.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/fe0ce773882776652337b.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/26763825186e658e4460b.jpg")


