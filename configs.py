# (c) @PredatorHackerzZ || @TeleRoidGroup

import os

class Config(object):
	API_ID = int(os.environ.get("API_ID", "0"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-100"))
	SHORTLINK_URL = os.environ.get('SHORTLINK_URL')
	SHORTLINK_API = os.environ.get('SHORTLINK_API')
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1445283714"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ **🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅**]────⍟
│
├🔸 **My Name:** [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 **Language:** [Python 3](https://www.python.org)
│
├🔹 **Library:** [Pyrogram](https://docs.pyrogram.org)
│
├🔹 **Hosted On:** [Heroku](https://heroku.com)
│
├🔸 **Developer:** [Pro morningstar](https://t.me/pro_morningstar) 
│
├🔹 **Bot Support:** [Support Group](https://t.me/movies_request_02)
│
├🔸 **Channel:** [Channel](https://t.me/bhabhi_ke_pom_pom)
│
╰──────[ 😎 ]───────────⍟
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿:** [@pro_morningstar](https://telegram.me/pro_morningstar)
 ``
"""
	HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.
"""
