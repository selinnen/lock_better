import webapp2

from google.appengine.ext import ndb

class User(ndb.Model):
    username = ndb.StringProperty()
    lives = ndb.IntegerProperty()
    points = ndb.FloatProperty()
    num_correct = ndb.JsonProperty()
