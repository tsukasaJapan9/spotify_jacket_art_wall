import argparse
import os
from random import sample

import requests
import spotipy
from PIL import Image
from spotipy.oauth2 import SpotifyOAuth

# 画像を何行何列にするか
IMAGE_COLUMN = 6  # 列
IMAGE_ROW = 6  # 行
SCALE = 0.3
IMAGE_SIZE = 640


def _create_random_image_name_list(image_names, num):
    random_image_name_list = []
    count = 0
    while True:
        random_image_names = sample(image_names, len(image_names))
        for name in random_image_names:
            random_image_name_list.append(name)
            count += 1
            if count >= num:
                return random_image_name_list


def main(args):
    os.makedirs("./images", exist_ok=True)

    scope = "user-library-read"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    playlists = sp.current_user_playlists()["items"]
    print("ID, playlist name")
    for i, playlist in enumerate(playlists):
        print(f"{i}, {playlist['name']}")

    if args.render_id is None:
        return

    resized_image_size = int(IMAGE_SIZE * SCALE)

    canvas_width = IMAGE_COLUMN * resized_image_size
    canvas_height = IMAGE_ROW * resized_image_size

    canvas = Image.new("RGBA", (canvas_width, canvas_height), color="#ffffff")
    album_names = []

    tracks = sp.playlist(playlists[args.render_id]["id"])["tracks"]["items"]
    for track in tracks:
        track_name = track["track"]["name"]
        image_url = track["track"]["album"]["images"][0]["url"]
        album_name = track["track"]["album"]["name"]
        artists = track["track"]["artists"]

        album_name = album_name.replace("/", "")

        album_names.append(album_name)

        print("============================")
        print(f"{album_name}, {track_name}, {image_url}")
        for artist in artists:
            print(artist["name"])

        album_image = Image.open(requests.get(image_url, stream=True).raw)
        album_image = album_image.resize((resized_image_size, resized_image_size))
        album_image.save(f"./images/{album_name}.jpg")

    # 重複を除く
    album_names = list(set(album_names))
    random_image_name_list = _create_random_image_name_list(album_names, IMAGE_COLUMN * IMAGE_ROW)

    index = 0
    for j in range(IMAGE_ROW):
        for i in range(IMAGE_COLUMN):
            image_name = random_image_name_list[index]
            image = Image.open(f"./images/{image_name}.jpg")
            canvas.paste(image, (i * resized_image_size, j * resized_image_size))
            index += 1

    canvas.save("out.png")
    show_scale = 0.6
    canvas.resize((int(canvas.width * show_scale), int(canvas_height * show_scale))).show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--render_id', help='render jacket art wall with the specified id', type=int)
    args = parser.parse_args()  

    main(args)
