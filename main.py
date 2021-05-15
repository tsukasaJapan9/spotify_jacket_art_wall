import requests
import spotipy
from PIL import Image
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint


def main():
    scope = "user-library-read"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    playlists = sp.current_user_playlists()["items"]
    print("ID, playlist name, playlist id")
    for i, playlist in enumerate(playlists):
        print(f"{i}, {playlist['name']}, {playlist['id']}")

    tracks = sp.playlist("")["tracks"]["items"]
    for track in tracks:
        print("============================")
        track_name = track["track"]["name"]
        image_url = track["track"]["album"]["images"][0]["url"]
        album_name = track["track"]["album"]["name"]
        artists = track["track"]["artists"]

        print(f"{album_name}, {track_name}, {image_url}")
        for artist in artists:
            print(artist["name"])

        album_image = Image.open(requests.get(image_url, stream=True).raw)
        album_image.save(f"./images/{album_name}.jpg")


if __name__ == "__main__":
    main()
