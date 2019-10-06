import followercounter

def test_youtube_successfully(requests_mock):
  username = 'arthurthiago'
  key = 'youtubekey'
  
  data = '{ "kind": "youtube#channelListResponse", "etag": "8jEFfXBrqiSrcF6Ee7MQuz8XuAM/tJCRjsz5qsBwvvp99pWx35KOq48", "pageInfo": {"totalResults": 1,"resultsPerPage": 5 }, "items": [{"kind": "youtube#channel","etag": "8jEFfXBrqiSrcF6Ee7MQuz8XuAM/jfOzRCK1lb33zqvCaCXIUVCuvkM","id": "UC4KaxcIx06UG72NWkTmch4w","statistics": {  "viewCount": "45887", "commentCount": "0", "subscriberCount": "21", "hiddenSubscriberCount": false, "videoCount": "6"}} ] }'
  requests_mock.get('https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername='+username+'&key='+key, text=data)

  count = followercounter.youtube(key, username)

  assert count == 21

def test_twitter_successfully(requests_mock):
  name = 'novatics'
  key = 'somekey'
  
  data = '{ "id": 6253282, "id_str": "6253282", "name": "Twitter API", "screen_name": "TwitterAPI", "location": "San Francisco, CA", "followers_count": 6133636, "listed_count": 12936, "friends_count": 12 }'
  requests_mock.get('https://api.twitter.com/1.1/users/show.json?Name='+name, text=data)

  count = followercounter.twitter(key, name)

  assert count == 6133636

def test_instagram_successfully(requests_mock):
  access_token = 'someAccessToken'
  
  data = '{"data": {"id": "625224918", "username": "jeager13", "profile_picture": "https://scontent.cdninstagram.com/vp/83d10617aec58be7380a86b6fa5293f6/5E2C1C92/t51.2885-19/s150x150/20688256_108937706466040_7610686090076225536_a.jpg?_nc_ht=scontent.cdninstagram.com", "full_name": "Vinicius Franco", "bio": "you only live once.", "website": "", "is_business": false, "counts": {"media": 118, "follows": 653, "followed_by": 598}}, "meta": {"code": 200}}'
  requests_mock.get("https://api.instagram.com/v1/users/self/?access_token=%s" %access_token, text=data)

  count = followercounter.instagram('someAccessToken')

  assert count == 598
