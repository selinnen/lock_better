
import webapp2
import os
import jinja2

import time

from usermodel import User
from google.appengine.ext import ndb
from google.appengine.ext.db import Model
from . import key as key_module



the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class HomePage(webapp2.RequestHandler):
    def get(self):
        home_template = the_jinja_env.get_template("templates/home.html")
        self.response.write(home_template.render())

class PurposePage(webapp2.RequestHandler):
    def post(self):
        username = self.request.get("username")
        user = User(username = username, lives = 3, points = 0, num_correct = {})
        user.put()
        time.sleep(.1)
        purpose_dictionary = {
            "userkey" : user.key
        }
        purpose_template = the_jinja_env.get_template("templates/purpose.html")
        self.response.write(purpose_template.render(purpose_dictionary))

class GamePage(webapp2.RequestHandler):
    def post(self):
        userkey = self.request.get("userkey")
        print(userkey)
        user = User.query().filter(User == userkey).get()
        game_dictionary = {
            "username" : user.username,
            "lives" : user.lives,
            "points" : user.points,
        }
        game_template = the_jinja_env.get_template("templates/game.html")
        self.response.write(game_template.render(game_dictionary))

# class BalloonGamePage(webapp2.RequestHandler):
#     def get(self):
#         get_user_info_template = the_jinja_env.get_template("templates/getuserinfo.html")
#         self.response.write(get_user_info_template.render())
#     def post(self):
#         username = self.request.get("username")
#         user = GameUser(username = username, lives = 3, points = 0, num_correct = {})
#         user.put()
#         time.sleep(.1)
#         game_template = the_jinja_env.get_template("templates/game.html")
#         game_dictionary = {
#             "username" : user.username,
#             "lives" : user.lives,
#             "points" : user.points,
#         }
#         self.response.write(game_template.render(game_dictionary))

app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/purpose', PurposePage),
    ('/game', GamePage),

    # ('/balloongame', BalloonGamePage),

], debug=True)
