import os,web
from apps.base.config import *
from configs.conf import (base_url, assets_url)
from configs.database import *

VIEWS_PATH = os.path.abspath(os.path.dirname( __file__ ) + '/views')
CTRLS_PATH = os.path.abspath(os.path.dirname( __file__ ) + '/controllers')
MODLS_PATH = os.path.abspath(os.path.dirname( __file__ ) + '/models')

template_globals = {
    'base_url': base_url,
    'assets_url':assets_url
}

render = web.template.render(VIEWS_PATH,base='master',globals=template_globals)