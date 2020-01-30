
import webapp2
import os
import jinja2

import time

from usermodel import User
from google.appengine.ext import ndb
from google.appengine.api import memcache
from google.appengine.api import mail
from google.appengine.api import urlfetch
from google.appengine.ext import db

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class HomePage(webapp2.RequestHandler):
    def get(self):
        home_template = the_jinja_env.get_template("templates/home.html")
        self.response.write(home_template.render())

class PurposePage(webapp2.RequestHandler):
    def get(self):
        # username = self.request.get("username")
        # user = User(username = username, lives = 3, points = 0, num_correct = {})
        # user.put()
        # time.sleep(.1)
        # purpose_dictionary = {
        #     "username" : user.username
        # }
        purpose_template = the_jinja_env.get_template("templates/purpose.html")
        self.response.write(purpose_template.render())

class LoginPage(webapp2.RequestHandler):
    def get(self):
        login_template = the_jinja_env.get_template("templates/login.html")
        self.response.write(login_template.render())

class GamePage(webapp2.RequestHandler):
    def post(self):
        username = self.request.get("username")
        # user = User.query().filter(User.username == username).get()
        game_dictionary = {
            "username" : username,
        }
        game_template = the_jinja_env.get_template("templates/game.html")
        self.response.write(game_template.render(game_dictionary))

class GamePage2(webapp2.RequestHandler):
    def post(self):
        username = self.request.get("username")
        user = User.query().filter(User.username == username).get()
        game_2_dictionary = {
            "username" : user.username,
            "lives" : user.lives,
            "points" : user.points,
        }
        game_2_template = the_jinja_env.get_template("templates/game2.html")
        self.response.write(game_2_template.render(game_2_dictionary))

class GamePage3(webapp2.RequestHandler):
    def post(self):
        username = self.request.get("username")
        user = User.query().filter(User.username == username).get()
        game_3_dictionary = {
            "username" : user.username,
            "lives" : user.lives,
            "points" : user.points,
        }
        game_3_template = the_jinja_env.get_template("templates/game3.html")
        self.response.write(game_3_template.render(game_3_dictionary))

class CongratPage(webapp2.RequestHandler):
    def post(self):
        username = self.request.get("username")
        user = User.query().filter(User.username == username).get()
        congrat_dictionary = {
            "username" : user.username,
            "lives" : user.lives,
            "points" : user.points,
        }
        congrat_template = the_jinja_env.get_template("templates/congrat.html")
        self.response.write(congrat_template.render(congrat_dictionary))

class SurveyPage(webapp2.RequestHandler):
    def get(self):
        # username = self.request.get("username")
        # user = User.query().filter(User.username == username).get()
        # survey_dictionary = {
        #     "username" : user.username,
        #     "lives" : user.lives,
        #     "points" : user.points,
        # }
        survey_template = the_jinja_env.get_template("templates/survey.html")
        self.response.write(survey_template.render())

class ThankPage(webapp2.RequestHandler):
    def post(self):
        # username = self.request.get("username")
        # user = User.query().filter(User.username == username).get()
        # survey_dictionary = {
        #     "username" : user.username,
        #     "lives" : user.lives,
        #     "points" : user.points,
        # }
        thank_template = the_jinja_env.get_template("templates/thank.html")
        self.response.write(thank_template.render())
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
    ('/login', LoginPage),
    ('/game', GamePage),
    ('/game2', GamePage2),
    ('/game3', GamePage3),
    ('/congratulation', CongratPage),
    ('/survey', SurveyPage),
    ('/thankyou', ThankPage),
    # ('/balloongame', BalloonGamePage),

], debug=True)
