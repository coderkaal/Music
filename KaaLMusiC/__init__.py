from Kaalmusic.core.bot import kaal
from Kaalmusic.core.dir import dirr
from Kaalmusic.core.git import git
from Kaalmusic.core.userbot import Userbot
from Kaalmusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = kaal()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
