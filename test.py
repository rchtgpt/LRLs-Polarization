
import requests
import json
from datetime import date

url = 'https://open.tiktokapis.com/v2/research/video/query/?fields=id,video_description,create_time,region_code,share_count,view_count,like_count,comment_count,hashtag_names,username,voice_to_text'

# A new bearer token needs to be generated every 2 hours

headers = {
    'authorization': 'bearer clt.wOn5DLHP0Ddn7Yiwzm7e77wOIFHOZiQG9EFqWALjat6r8H786m8zDaCK54Ya',
    'Content-Type': 'application/json',
}

date_val = date(2023, 10, 7)
todays_date = date.today()
