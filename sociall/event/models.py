from django.db import models
from django.contrib.auth.models import User
import requests
import datetime
import ast

class Event(models.Model):
	user = models.ForeignKey(User)
	event_name = models.CharField(max_length=255)
	instagram_hashtag = models.CharField(max_length=255)
	instagram_handle = models.CharField(max_length=255)
	twitter_hashtag = models.CharField(max_length=255)
	twitter_handle = models.CharField(max_length=255)
	status = models.IntegerField()

class Photos(models.Model):
	event = models.ForeignKey(Event)
	image_url = models.TextField()
	caption = models.TextField()
	post_by = models.CharField(max_length=255)
	post_date = models.DateTimeField()
	tags = models.TextField()
	like_count = models.CharField(max_length=255)
	show = models.BooleanField()

	def tag_array(self):
		return ast.literal_eval(self.tags)

def load_data(hashtag):
	url = "https://api.instagram.com/v1/tags/%s/media/recent?access_token=48995350.1fb234f.ff5ff4fba6eb4d23a106182f3be74b40" % (hashtag)
	instagram_json = []
	i = 0

	for i in range(0,5):
		new_data = requests.get(url).json()
		pagination = new_data["pagination"]
		url = pagination["next_url"]
		new_data = new_data["data"]
		instagram_json.append(new_data)
		print url
		i += 1

	#print instagram_json
	return instagram_json

def timemachine(the_time):
	converted = datetime.datetime.fromtimestamp(int(the_time)).strftime('%Y-%m-%d %H:%M:%S')
	return converted

def create_photos(data, event_id):
	print "The Data:"

	for d in data:
		for i in d:
			p = Photos()
			p.event_id = event_id
			p.image_url = i["images"]["standard_resolution"]["url"]
			p.caption = i["caption"]["text"]
			p.post_by = i["user"]["username"]
			p.post_date = timemachine(i["created_time"])
			p.tags = (i["tags"])
			print type(p.tags)
			#p.tags = [ item.encode('ascii') for item in ast.literal_eval(tag_unicode) ]
			p.like_count = i["likes"]["count"]
			p.show = True

			p.save()


# class Download_Data():
# 	def __init__(self):
# 		import requests

# 	def url(hashtag):
# 		url = "https://api.instagram.com/v1/tags/%s/media/recent?access_token=48995350.1fb234f.ff5ff4fba6eb4d23a106182f3be74b40" % (hashtag)

# 		instagram_json = requests.get(url).json()
# 		pagination = instagram_json["pagination"]
# 		meta = instagram_json["meta"]
# 		data = instagram_json["data"]

# 		for i in data:
# 			p = Photos
# 			p.image_url = i["images"]["standard_resolution"]["url"]
# 			p.caption = i["caption"]["text"]
# 			p.post_by = i["user"]["username"]
# 			p.post_date = i["created_time"]
# 			p.tags = i["tags"]
# 			p.like_count = i["likes"]["count"]
# 			p.show = True

# 			p.save()



