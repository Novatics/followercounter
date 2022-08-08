import time
import requests
import json

GOOGLE_API_URL='https://www.googleapis.com/youtube/v3'

def make_url(host, params):

    return f'{host}/{params}'

def send_request(host, params):

    full_url = make_url(host, params)

    print(full_url)

    return requests.get(full_url).json()

def get_youtube_channel_id(key, channel_name):

    params = f'channels?key={key}&forUsername={channel_name}&part=id'

    params = f'search?key={key}&q={channel_name}&part=snippet,id';
    return send_request(GOOGLE_API_URL, params)

def get_youtube_subscribers(key, channel_id):
    params = f'channels?part=statistics&id={channel_id}&key={key}'

    youtube_data = send_request(GOOGLE_API_URL, params)

    subsCount = youtube_data['items'][0]['statistics']['subscriberCount']

def twitter(access_token, name):
  url = 'https://api.twitter.com/1.1/users/show.json?Name=%s' %(name)
  text = requests.get(url, headers={"authorization":"Bearer " + access_token}).content
  return int(json.loads(text)['followers_count'])

def instagram(access_token):
  url = 'https://api.instagram.com/v1/users/self/?access_token=%s' %(access_token)
  response = requests.get(url).content
  return int(json.loads(response)['data']['counts']['followed_by'])


def print_json(json_data):
    print(json.dumps(json_data, indent=2))

def main():

    key = 'AIzaSyAKTlhIZQv3EKms5ZLqPZQkZKJyNbAS5OA'
    
    #result = get_youtube_channel_id(key, 'StudioM4Arquitetura')

    print_json(get_youtube_subscribers(key, 'UCeyH-g2_EXMFpGlTM9v6ZJg'))


if __name__ == "__main__":
    main()
