# -*- coding: utf-8 -*-

__author__ = 'Chris Murray - cjjmurray@gmail.com'
__website__ = 'www.golci.com'

import sys
from secrets import SESSION_KEY

from webapp2 import WSGIApplication, Route
from models import User

# inject './lib' dir in the path so that we can simply do "import ndb" 
# or whatever there's in the app lib dir.
if 'lib' not in sys.path:
    sys.path[0:0] = ['lib']

# webapp2 config
app_config = {
  'webapp2_extras.sessions': {
    'cookie_name': '_simpleauth_sess',
    'secret_key': SESSION_KEY
  },
  'webapp2_extras.auth': {
    'user_model': User,  # default is webapp2_extras.appengine.auth.models.User
    'user_attributes':['gpoints' ]  # list of User model properties
  }
}
    
# Map URLs to handlers
routes = [
  Route('/', handler='handlers.IndexHandler', name='game_base'), 
#  Route('/tree', handler='handlers.TreeHandler', name='tree'),  
#  Route('/jsontree', handler='handlers.TreeJsonHandler', name='jsontree'), 
  Route('/profile', handler='handlers.ProfileHandler', name='profile'), 
  Route('/gview', handler='handlers.GViewHandler', name='gview'),  
  Route('/gamebot', handler='handlers.GamebotHandler', name='gamebot'),
  Route('/auth/<provider>', handler='handlers.AuthHandler:_simple_auth', name='auth_login'),
  Route('/auth/<provider>/callback', handler='handlers.AuthHandler:_auth_callback', name='auth_callback'),
  Route('/login', handler='handlers.LoginHandler', name='login'),
  Route('/logout', handler='handlers.AuthHandler:logout', name='logout'),
  Route('/index', handler='handlers.IndexHandler', name='index'),
  Route('/postgolci', handler='handlers.Postgolci', name='postgolci'),
  Route('/pd', handler='handlers.PostDate', name='pd'),
  Route('/upload', handler='handlers.FileUploadHandler', name='upload'),
  Route('/serve/([^/]+)?', handler='handlers.FileServeHandler', name='serve'),
  Route('/generate_upload_url', handler='handlers.UploadUrlHandler', name='generate_upload_url'),
  Route('/latestgolci', handler='handlers.latestgolciHandler', name='latestgolci'),
  Route('/image', handler='handlers.ImageHandler', name='image'),    
  Route('/images', handler='handlers.ImageHandler2', name='images'),    
  Route('/menu', handler='handlers.HomeMenuHandler', name='menu'),
  Route('/branch', handler='handlers.BranchHandler', name='branch'),
  Route('/ga', handler='handlers.GameAuthorHandler', name='ga'),
  Route('/cv', handler='handlers.ContentionHandler', name='cv'),
  Route('/conv', handler='handlers.ContentionHandler', name='conv'),
  Route('/add', handler='handlers.SimpleArgHandler', name='add'),
  Route('/map', handler='handlers.MapEditHandler', name='map'),
  Route('/textmatch', handler='knol_handlers.textmatch', name='textmatch'),
  Route('/initc', handler='knol_handlers.InitClassifier', name='initc'),
  Route('/flushc', handler='knol_handlers.Flush', name='flushc'),
  Route('/xyz101', handler='handlers._101', name='101'),
  Route('/aaaa', handler='handlers.aaaa', name='aaaa'),
  Route('/delete/', handler='handlers.DeleteKindHandler', name='delete')
]

app = WSGIApplication(routes, config=app_config, debug=True)
