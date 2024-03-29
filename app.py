import requests
import json
from datetime import date, timedelta

url = 'https://open.tiktokapis.com/v2/research/video/query/?fields=id,video_description,create_time,region_code,share_count,view_count,like_count,comment_count,hashtag_names,username,voice_to_text'

# A new bearer token needs to be generated every 2 hours

headers = {
    'authorization': 'bearer clt.8eiCHUeaEzd2wo8C3ocZwSuTBgwU4H5twRkg1JcSrBm5Y65jCKGlsA2CvVtf',
    'Content-Type': 'application/json',
}

final_json = []
username_vidID_pair = {}

date_val = date(2023, 10, 7)
todays_date = date.today()

while (date_val < date(2023, 10, 9)):
    prev_cursor = -1
    cursor = 0
    search_id = ""

    current_date_vids = []

    while (prev_cursor != cursor): 
        print("the value of cursor being fed into the query", cursor)

        current_date = date_val.strftime("%Y%m%d")

        data = {
            "query": {
                "and": [
                    {"operation": "IN", "field_name": "hashtag_name", "field_values": ["עזה"]}, # עזה means gaza 
                ]
            },
            "cursor": cursor,
            "search_id": search_id,
            "start_date": current_date,
            "end_date": current_date,
            "is_random": False 
        }
        
        response = requests.post(url, headers=headers, json=data)
        json_data = response.json()

        if 'data' in json_data and 'videos' in json_data['data']:
            current_date_vids.extend(json_data['data']['videos'])
            prev_cursor = cursor
            cursor = json_data['data'].get('cursor', -1)
            search_id = json_data['data'].get('search_id', "")

        else:
            print(json_data)
            print("No 'data' key found in the response JSON.")
            break

    for video in current_date_vids:
        username_vidID_pair[video["id"]] = video["username"]

    # Write the JSON data to a new file
    final_json.append({
                    "date": date_val.strftime("%Y%m%d"), 
                    "value": {
                        "has_more": json_data['data'].get('has_more', False), 
                        "videos": current_date_vids, 
                        "cursor": cursor
                        }
                })

    date_val += timedelta(days=1)
    print("new date to be explored is", date_val)

with open('hashtag2_filtered.json', 'a', encoding='utf-8') as json_file:
        json.dump(final_json, 
                json_file, 
                indent=2, 
                ensure_ascii=False
            )

def findURLs(username_vidID_pair):
    """
    Using Video IDs and username, we can create the URL ourselves:

    https://www.tiktok.com/@{username}/video/{video_id}
    """
    for video_id, username in username_vidID_pair.items():
        print(f"https://www.tiktok.com/@{username}/video/{video_id}")


findURLs(username_vidID_pair)