import requests
from bs4 import BeautifulSoup
import re

# Function Takes a Mobile YT url and attempts to return the artist and song names from the title

# url should be Mobile YT link(m.youtube.com)
def get_songs(URL):
    M_url = URL[:8] + "m" + URL[11:]
    data = requests.get(URL)
    data = BeautifulSoup(data.text, features="html.parser")
    table = data.find("table", "pl-video-table")
    songs = table.find_all("tr", "pl-video yt-uix-tile")
    # print(sum(1 for _ in songs))
    song_names = [s.get("data-title") for s in songs]
    print(song_names)
    song_names = [s.replace("\n", "") for s in song_names]
    song_names = [s.replace("(Official Video)", "") for s in song_names]
    song_names = [s.replace("(Official Lyric Video)", "") for s in song_names]
    song_names = [s.replace("Lyric Video", "") for s in song_names]
    song_names = [s.replace("lyrics", "") for s in song_names]
    song_names = [s.replace("Lyrics", "") for s in song_names]
    song_names = [s.split("by")[0].strip() for s in song_names]
    artist_names = [s.split("-")[0].strip() for s in song_names]
    # song_names = [s.split("-")[1].strip() for s in song_names]
    print("\n\n\n")
    print(song_names)
    print("\n\n\n")
    print(artist_names)

    # print(song_names)


yt_url = "https://www.youtube.com/playlist?list=PLHipon1nMaMB0VPt_n_5Fwie0vYCXaNC4"
get_songs(yt_url)
