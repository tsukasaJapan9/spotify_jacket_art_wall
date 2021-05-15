import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint


def main():
    scope = "user-library-read"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    playlists = sp.current_user_playlists()["items"]
    for playlist in playlists:
        print(f"{playlist['name']}, {playlist['id']}")


if __name__ == "__main__":
    main()
