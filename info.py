import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')
API_ID = 912074
API_HASH = '1a09c7cdf2751540f4dab73e87305af9'
BOT_TOKEN = '1990089587:AAG2idmBbWPGkLobE4_WPB3bVnNmWU-pfz4'
USERBOT_STRING_SESSION = 'BQCThh3joj6RaI1leL13UAOKotjVGU5FiQE2dV5pWj0oXXIbnhuf-wVrAq3tGHAV67gVuue-mjqERsJwwwKX_kOl_LZvHDkuw9NPc9KtCo6XDeLybrca1BrnZ27_a0IqAm3tJObEHvuTAdFTpG907eddwDTefpx-eb9DmhfJVINcVkkHR3TFhzizvmGPGWLMkBbjKh_lMFFJ-8cjbcKMDUd8FVW4QNil0Guygn717G_WOdLxleP5KNzHkiT0uK5c4OcvYzNXfPwJFTR-BDn5sIXQ52bYcmvu-GQQcWzcSdYKG1fQKYkl38Eqrq66s0Y7yqdLBZIc7OZFUPQw1tulwQsmKtqUPgA'

# Bot settings
CACHE_TIME = 300
USE_CAPTION_FILTER = True

# Admins, Channels & Users
ADMINS = [718967870]
CHANNELS = [-1001336097923, -1001205787325, -1001430310853, -1001193592929, -1001236158458]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = []
AUTH_CHANNEL = [-1001367552406]

# MongoDB information
DATABASE_URI = environ['DATABASE_URI']
DATABASE_NAME = environ['DATABASE_NAME']
COLLECTION_NAME = Telegram_files

# Messages
START_MSG = """
**Hi, I'm a Telegram Movie Search Bot**
Click **SEARCH Button** and type Movie name and year (Correct imdb Spelling)..

Our Second Bot **@ProSearchRobot**
Bot Updates **@ProSearchBots**
"""


SHARE_BUTTON_TEXT = 'Checkout {username} for searching files'
INVITE_MSG = 'First JOIN our BOT Channel **@ProSearchBots**'
