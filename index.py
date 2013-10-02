#!C:\Python27\python.exe
import web
import os,sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from importlib import import_module

import configs.routes as routes
import configs.conf as settings
from configs.database import DB
#import configs.emails as email

#AUTO IMPORT CONTROLLERS
apps = os.path.abspath(os.path.dirname( __file__ )) + '/apps'
dirs = os.listdir(apps)
for d in dirs:
    if os.path.isdir(apps + '/' + d):
        dir = os.listdir(apps + '/' + d)
        controllers_path = apps + '/' + d + '/controllers'
        sys.path.append(os.path.abspath(controllers_path))
        for root, dirs, files in os.walk(controllers_path):
            for f in files:
                split = os.path.splitext(f)
                if f != '__init__.py' and split[1] == '.py':
                    c = split[0]
                    m = 'apps.' + d + '.controllers.' + c
                    module = import_module(m)
                    class_name = getattr(module, c)
                    globals()[c] = class_name

#PATHS DEFINITIONS
BASE_PATH = os.path.dirname(__file__)
APP_PATH = os.path.dirname(__file__) + '/apps'
CONFIG_PATH = os.path.dirname(__file__) + '/configs'

web.config.debug = settings.debug
app = web.application(routes.URLS, globals())

#BY DEFAULT THE APPLICATION IS USING DB to STORE THE SESSIONS
store = web.session.DBStore(DB, 'sessions')

#UNCOMMENT IF YOU WANT TO USE DISKTORE SESSIONS
#curdir = os.path.dirname(__file__)
#store = web.session.DiskStore(os.path.join(curdir,'sessions'))

session = web.session.Session(app, store, initializer={'count': 0})

#ERROR PAGES
def notfound():
    return web.notfound("Sorry, the page you were looking for was not found.")
    # You can use template result like below, either is ok:
    #return web.notfound(render.notfound())
    #return web.notfound(str(render.notfound()))

def internalerror():
    return web.internalerror("There was a bad error happened.")

app.notfound = notfound
app.internalerror = internalerror

# WEBPY SERVER
#if __name__ == "__main__":app.run()
#INITIALIZE AS WSGI APPLICATION
application = app.wsgifunc()



