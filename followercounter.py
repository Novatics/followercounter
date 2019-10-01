import requests
import json

def youtube(key, username):
  url = 'https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=%s&key=%s' %(username, key)
  text = requests.get(url).content
  return int(json.loads(text)['items'][0]['statistics']['subscriberCount'])

def instagram(access_token):
  url = 'https://api.instagram.com/v1/users/self/?access_token=%s' %(access_token)
  response = requests.get(url).content
  return int(json.loads(response)['data']['counts']['followed_by'])