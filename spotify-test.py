import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "client id"
CLIENT_SECRET = "client secret"
REDIRECT_URI = "http://127.0.0.1:8888/callback/"


scope = "playlist-read-private user-library-read"


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=scope
))


user = sp.current_user()
print("✅ Logged in as:", user['display_name'])

mood_keywords = {
    "happy": ["happy", "joyful", "upbeat"],
    "sad": ["sad", "melancholy", "heartbreak"],
    "chill": ["chill", "relaxing", "calm"],
    "energetic": ["party", "workout", "energetic"],
    "romantic": ["love", "romantic", "romance"]
}
mood = input("Enter your mood (happy, sad, chill, energetic, romantic): ").lower()

if mood not in mood_keywords:
    print("Sorry, mood not recognized. Try one of: happy, sad, chill, energetic, romantic")
    exit()

print(f"\n🎵 Playlists for mood '{mood}':\n")

for keyword in mood_keywords[mood]:
    results = sp.search(q=f"{keyword} playlist", type="playlist", limit=5)
    for idx, playlist in enumerate(results['playlists']['items']):
        print(f"{idx + 1}. {playlist['name']} - {playlist['external_urls']['spotify']}")
    print("") 

track_ids = []
for keyword in mood_keywords[mood]:
    results = sp.search(q=f"{keyword} playlist", type="playlist", limit=5)
    for playlist in results['playlists']['items']:
        # Get up to 10 tracks from each playlist
        tracks = sp.playlist_items(playlist['id'], limit=10)
        for item in tracks['items']:
            track = item['track']
            if track:  # sometimes track can be None
                track_ids.append(track['id'])

track_ids = list(set(track_ids))

if not track_ids:
    print("❌ No tracks found for this mood.")
    exit()
playlist_name = f"{mood.capitalize()} Vibes"
playlist = sp.user_playlist_create(user=user['display_name'], name=playlist_name, public=False)
playlist_id = playlist['id']

for i in range(0, len(track_ids), 100):
    sp.playlist_add_items(playlist_id, track_ids[i:i + 100])

print(f"✅ Playlist '{playlist_name}' created with {len(track_ids)} tracks!")

print(f"🔗 Open in Spotify: {playlist['external_urls']['spotify']}")
