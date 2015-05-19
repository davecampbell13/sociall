import requests
import datetime
import ast

import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text

# def timemachine(the_time):
# 	converted = datetime.datetime.fromtimestamp(
#         int(the_time)
#     ).strftime('%Y-%m-%d %H:%M:%S')
# 	print converted

# timemachine(1431300535)

# hashtag = "anotherbestday"
# #url = "https://api.instagram.com/v1/tags/anotherbestday/media/recent?access_token=48995350.1fb234f.ff5ff4fba6eb4d23a106182f3be74b40"
# url = "https://api.instagram.com/v1/tags/%s/media/recent?access_token=48995350.1fb234f.ff5ff4fba6eb4d23a106182f3be74b40" % (hashtag)

# instagram_json = requests.get(url).json()

# print url

# pagination = instagram_json["pagination"]

# print pagination["next_url"]

# meta = instagram_json["meta"]

# data = instagram_json["data"]


# def url_loop():
# 	hashtag = "anotherbestday"
# 	url = "https://api.instagram.com/v1/tags/%s/media/recent?access_token=48995350.1fb234f.ff5ff4fba6eb4d23a106182f3be74b40" % (hashtag)
# 	i = 0

# 	print url

# 	for i in range(0,5):
# 		instagram_json = requests.get(url).json()
# 		pagination = instagram_json["pagination"]
# 		url = pagination["next_url"]
# 		print url
# 		i += 1

# url_loop()

# instagram_json = requests.get(url).json()

# print url

# pagination = instagram_json["pagination"]

# print pagination["next_url"]

# meta = instagram_json["meta"]

# data = instagram_json["data"]



# def load_data_for_instagram_hashtag(hashtag):
# 	url = "https://api.instagram.com/v1/tags/%s/media/recent?access_token=48995350.1fb234f.ff5ff4fba6eb4d23a106182f3be74b40" % (hashtag)
# 	instagram_json = requests.get(url).json()
# 	return instagram_json["data"]

# print load_data_for_instagram_hashtag("anotherbestday")

# for i in data:
# 	print "==============================="
# 	print "HASHTAGS: " + str(i["tags"])
# 	#tag_unicode = i["tags"]
# 	print type(i["tags"])
# 	# # for i in tag_unicode:
# 	# # 	print i
# 	# # print [ item.encode('ascii') for item in ast.literal_eval(tag_unicode) ]
# 	# tag = ast.literal_eval(i["tags"])
# 	# print tag

# 	#print "CAPTION: " + str(i["caption"]["text"])
# 	print "CREATED TIME: " + str(i["created_time"])
# 	print "LINK: " + str(i["link"])
# 	print "LIKES COUNT: " + str(i["likes"]["count"])
# 	print "IMAGE URL: " + str(i["images"]["standard_resolution"]["url"])
# 	print "USERNAME: " + str(i["user"]["username"])
