import followercounter

def test_youtube_successfully(requests_mock):
  username = 'arthurthiago'
  key = 'youtubekey'
  
  data = '{ "kind": "youtube#channelListResponse", "etag": "8jEFfXBrqiSrcF6Ee7MQuz8XuAM/tJCRjsz5qsBwvvp99pWx35KOq48", "pageInfo": {"totalResults": 1,"resultsPerPage": 5 }, "items": [{"kind": "youtube#channel","etag": "8jEFfXBrqiSrcF6Ee7MQuz8XuAM/jfOzRCK1lb33zqvCaCXIUVCuvkM","id": "UC4KaxcIx06UG72NWkTmch4w","statistics": {  "viewCount": "45887", "commentCount": "0", "subscriberCount": "21", "hiddenSubscriberCount": false, "videoCount": "6"}} ] }'
  requests_mock.get('https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername='+username+'&key='+key, text=data)

  count = followercounter.youtube(key, username)

  assert count == 21