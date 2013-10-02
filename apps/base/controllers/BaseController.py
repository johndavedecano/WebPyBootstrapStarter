import web
from apps.base.config import *
from configs.conf import (base_url, assets_url)
from configs.database import *

class BaseController():

    def GET(self):
        return render.index()