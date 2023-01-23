import pandas as pd
import spotipy
import spotipy.util as util
import secret

def CreatePlaylist(username, playlist_name):
  if (GetPlaylistID(username, playlist_name)):
    print('Playlist with name of', playlist_name, 'already exist.')
    return ''

  sp.user_playlist_create(username, name=playlist_name)

  print('Playlist', playlist_name, 'successfully created.')
  return playlist_name

def GetPlaylistID(username, playlist_name):
  playlist_id = ''
  playlists = sp.user_playlists(username)

  for playlist in playlists['items']:
    if (playlist['name'] == playlist_name):
      playlist_id = playlist['id']
  
  if (playlist_id): 
    print('Playlist found with id', playlist_id)

  return playlist_id

scope = 'playlist-modify-public'
username = secret.username
client_id = secret.client_id
client_secret = secret.client_secret

token = util.prompt_for_user_token(username,scope,client_id=client_id,client_secret=client_secret,redirect_uri='http://localhost:8888/callback')
sp = spotipy.Spotify(auth=token)

playlist_name = CreatePlaylist(username, 'Test 1')
playlist_id = GetPlaylistID(username, playlist_name)