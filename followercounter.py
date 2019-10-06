import requests
import json

def youtube(key, username):
  url = 'https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=' + username + '&key=' + key
  text = requests.get(url).content
  return int(json.loads(text)['items'][0]['statistics']['subscriberCount'])

def twitter(access_token, name):
  url = 'https://api.twitter.com/1.1/users/show.json?Name=%s' %(name)
  text = requests.get(url, headers={"authorization":"Bearer " + access_token}).content
  return int(json.loads(text)['followers_count'])
