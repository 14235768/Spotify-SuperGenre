import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time

""" 
I will be retrieving track information from my own playlist to check if the API works properly. 
Check the playlist here: https://open.spotify.com/playlist/3KUsPCxYIJ2USNFgseLLNn?si=f8acbf0ca4194492
"""

# Client ID set-up for API
client_id = '48635fa9d1ec447e8c7cc9ac846aaa28'
client_secret = '515de80f08b64bfa98a7e3a820e1f744'

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Get TrackID for my playlist
def get_playlist_track_ids(username, playlist_id):
  ids = []
  results = sp.user_playlist_tracks(username, playlist_id)
  tracks = results['items']
  while results['next']:
    results = sp.next(results)
    tracks.extend(results['items'])
    for item in tracks:
      ids.append(item['track']['id'])
  #CHECKPOINT 1 (uncomment to use)
  #print(len(ids))
  return ids

ids = get_playlist_track_ids('31a4nfvxz7zlukmsaony5ml5mdgi','3KUsPCxYIJ2USNFgseLLNn')

# Get Track Features and Genres
def getTrackFeatures(id):
  meta = sp.track(id)
  features = sp.audio_features(id)

  # meta
  name = meta['name']
  album = meta['album']['name']
  artist = meta['album']['artists'][0]['name']
  release_date = meta['album']['release_date']
  duration_ms = meta['duration_ms']
  popularity = meta['popularity']

  # features
  acousticness = features[0]['acousticness']
  danceability = features[0]['danceability']
  energy = features[0]['energy']
  key = features[0]['key']
  mode = features[0]['mode']
  instrumentalness = features[0]['instrumentalness']
  liveness = features[0]['liveness']
  loudness = features[0]['loudness']
  speechiness = features[0]['speechiness']
  valence = features[0]['valence']
  tempo = features[0]['tempo']
  time_signature = features[0]['time_signature']

  #Get Genre
  """
  #Spotify does not have genre for each track, so instead, we will retrieve artists' genres
  """

  artist_id = sp.artist(meta['album']['artists'][0]['external_urls']['spotify'])
  genres = artist_id['genres']

  track = [name, album, artist, release_date, duration_ms, popularity, acousticness, danceability, energy, key, mode, instrumentalness, liveness, loudness, speechiness, valence, tempo, time_signature, genres]
  return track


# loop over track ids
tracks = []
for i in range(len(ids)):
  #time.sleep(.5) (uncomment if needed)
  track = getTrackFeatures(ids[i])
  tracks.append(track)

#CHECKPOINT 2 (uncomment to use)
#print(len(tracks))


# create dataset
df = pd.DataFrame(tracks, columns = ['name', 'album', 'artist', 'release_date', 'duration_ms', 'popularity', 'acousticness', 'danceability', 'energy', 'key', 'mode', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'valence','tempo', 'time_signature', 'genres'])
df.to_csv("sample.csv", sep = ',')
