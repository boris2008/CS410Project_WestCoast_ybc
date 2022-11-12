country_code = "US"

#get a fresh token, it expires in a short time.
#https://developer.spotify.com/console/post-playlists/
#get token
authorization = "BQDHnNWZ8jK4rkd1vgI35CI65-eHhiejvvHiu0rdbUKP0RLDitQzbZZFQGccjC-6J7CXmjmz0CaZsQ1kPOx3NJZ27kecPEhzonVDwtDQHgObyLp6Y1gDtaSfDHvDKBC-Yl3h0hPQyID7ohsf-mOOHsv_y1JXvwIO7P06PIdZSP4xRVWC4QvqMSmpuLfcs8hY1g8VazHecdVKGuCtyXGUGhrqezU4upD53Y-D3TYivsUOVuD2-ZVn"
user_id = "oz3udvh8gw737jcbug8eu1crv"
#this playlist id is for
playlist_id0= '00DEbjBighjpELJnp5Fh8s'


track0_id = "2ooIqOf4X2uz4mMptXCtie"
artist0_id = "1jeYbk5eqo6wgsQPjLeU5w"


import requests
import json
import pandas as pd
import numpy as np

def get_artist_from_artistid(artist_id):
  url = ''.join(["https://api.spotify.com/v1/artists/",artist_id])

  payload={}
  headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': ''.join(['Bearer ',authorization])}

  response = requests.request("GET", url, headers=headers, data=payload)
  data_temp = json.loads(response.text)
  return data_temp['name']

def get_artist_from_trackid(trackid):
  url = ''.join(["https://api.spotify.com/v1/artists/",trackid])

  payload={}
  headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': ''.join(['Bearer ',authorization])}

  response = requests.request("GET", url, headers=headers, data=payload)
  data_temp = json.loads(response.text)
  return data_temp['name']

#artist1 = get_artist_from_trackid(track0_id)
#print(artist1)

def get_track_from_trackid(trackid):
  url = ''.join(["https://api.spotify.com/v1/tracks/",trackid])

  payload={}
  headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': ''.join(['Bearer ',authorization])}

  response = requests.request("GET", url, headers=headers, data=payload)
  data_temp = json.loads(response.text)
  return data_temp['name']

def get_related_artists_from_trackid(trackid):
  url = ''.join(["https://api.spotify.com/v1/artists/",trackid,"/related-artists"])

  payload = {}
  headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': ''.join(['Bearer ', authorization])
  }


  response = requests.request("GET", url, headers=headers, data=payload)
  data_temp = json.loads(response.text)
  dic0= data_temp['artists']
  artist_list = []
  artist_id_list = []
  for value in dic0:
    artist_list.append(value['name'])
    artist_id_list.append(value['id'])
  return artist_list,artist_id_list


#artists1,artistid1 = get_related_artists_from_trackid(track0_id)
#print(artists1)
#print(artistid1)
#print(len(artists1))
#print(len(artistid1))

def create_a_playlist(new_playlist_name):
  url = ''.join(["https://api.spotify.com/v1/users/",user_id,"/playlists"])

  payload = json.dumps({
    "name": new_playlist_name,
    "description": "bocheng's playlist for the group project of CS410",
    "public": False
  })
  headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': ''.join(['Bearer ', authorization])
  }
  response = requests.request("POST", url, headers=headers, data=payload)
  data_temp = json.loads(response.text)
  new_playlist_id= data_temp['id']
  return new_playlist_id

#new_playlist_id = create_a_playlist("CS410ProjectList")
#print(new_playlist_id)

def get_artist_top_tracks_from_artist_id(artist_id):
  url = ''.join(["https://api.spotify.com/v1/artists/",artist_id,"/top-tracks?market=US"])

  payload = {}
  headers = {
    'Accept': 'application/json',
    'Authorization': ''.join(['Bearer ', authorization])
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  data_temp = json.loads(response.text)
  dic0= data_temp['tracks']
  track_list = []
  track_id_list = []
  for value in dic0:
    track_list.append(value['name'])
    track_id_list.append(value['id'])
  return track_list,track_id_list

#track_list1 = get_artist_top_tracks_from_artist_id(artist0_id0)[0]
#track_id_list1 = get_artist_top_tracks_from_artist_id(artist0_id0)[1]
#print(track_list1)
#print(track_id_list1)
#print(len(track_list1))
#print(len(track_id_list1))

def add_tracks_to_playlist(track_id_list,playlist_id):
  url = ''.join(["https://api.spotify.com/v1/users/",
               user_id,
                "/playlists/",
                playlist_id,
               "/tracks?uris="])
  for track_id in track_id_list:
    url+=''.join(["spotify:track:",
               track_id,
                 ","])
  payload = {}
  headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': ''.join(['Bearer ', authorization])
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  print(response.text)

#add_tracks_to_playlist(track_id_list1,playlist_id0)

def get_playlist_tracks(playlist_id):
  url = ''.join(["https://api.spotify.com/v1/playlists/",
        playlist_id,
        "/tracks"])

  payload = {}
  headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': ''.join(['Bearer ', authorization])
  }

  response = requests.request("GET", url, headers=headers, data=payload)
  data_temp = json.loads(response.text)
  info_temp = data_temp['items']
  playlist_tracks_info_list = []
  print("length:",len(info_temp))
  for i in np.arange(len(info_temp)):
    temp0 = [info_temp[i]['track']['artists'][0]['name'],
    info_temp[i]['track']['artists'][0]['id'],
    info_temp[i]['track']['name'],
    info_temp[i]['track']['id']]
    playlist_tracks_info_list.append(temp0)

  playlist_df = pd.DataFrame(playlist_tracks_info_list,
    columns=['artist_name', 'artist_id','track_name', 'track_id'])
  playlist_df.to_csv('my_playlist.csv',header=True, index=False)

  return playlist_df
  #return data_temp



playlist_tracks1= get_playlist_tracks(playlist_id0)
print(playlist_tracks1.shape)
print(playlist_tracks1['track_name'])
print(playlist_tracks1.head(5))


#artist_id0 = "5rSXSAkZ67PYJSvpUpkOr7"# backstreet boys
#track1_id = "3BsaRV5QIulYz2lV9WWa8T" #Show Me the Meaning of Being Lonely
#print(get_artist_from_artistid(artist_id0))
#print(get_track_from_trackid(track1_id))
