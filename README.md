# spotify jacket art wall
spotifyのプレイリストを取得し、プレイリストに含まれる曲のジャケットを並べてレンダリングするソフトウェアです。

# How to use
### spotify APIの設定
[spotifyのdeveloperページ](https://developer.spotify.com/)にてアカウント登録、アプリケーション作成(Create app)を行いClient IDとClient secretを発行する。アプリケーション作成の際、以下の通りに入力する。
- Website
  - 空のまま
- Redirect URIs
  - http://localhost:8888/callback
- APIs used
  - Web API

### アプリケーションの実行
環境変数をexportする。
```
$ export SPOTIPY_CLIENT_ID="<発行したClient ID>"
$ export SPOTIPY_CLIENT_SECRET="<発行したClient secret>"
$ export SPOTIPY_REDIRECT_URI="http://localhost:8888/callback"
```
必要パッケージをインストールする。
```
$ pip install -r requirements.txt
```
プレイリスト一覧を取得する。
```
$ python main.py
ID, playlist name
0, all my best
1, マイ Shazam トラック
2, Reggae supremes
```
ジャケットアートのレンダリングを行う。ここで id にはプレイリスト一覧で出力したIDを指定する。例えば「all my best」のプレイリストに入っている楽曲のジャケットをレンダリングしたければ0を指定する。
```
$ python main.py --render_id <id>
```
out.pngという名前で画像が出力される。
