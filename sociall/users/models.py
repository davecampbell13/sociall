from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
	user = models.OneToOneField(User)
	instagram_handle = models.CharField(max_length=100)
	twitter_handle = models.CharField(max_length=100)
