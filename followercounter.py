import requests
import json

def youtube(key, username):
  url = 'https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=' + username + '&key=' + key
  text = requests.get(url).content
  return int(json.loads(text)['items'][0]['statistics']['subscriberCount'])