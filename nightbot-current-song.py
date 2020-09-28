#!/usr/bin/env python3

import time
import sys
from urllib.request import urlopen
import json
import requests

file = '/tmp/nightbot-current-song.txt'
f = open(file, 'w', encoding='utf-8')

def get_channel_id():
    try:
        name = sys.argv[1]
    except IndexError:
        name = input('Channel name: ')

    while True:
        try:
            channel_url = f'https://api.nightbot.tv/1/channels/t/{name}'
            channel_load = urlopen(channel_url)
            jsonList = json.load(channel_load)
            channel_id = jsonList['channel']['_id']
            return channel_id
        except OSError:
            print('Channel not found, try again')
            time.sleep(3)

def get_song(channel_id):
    r = requests.get("https://api.nightbot.tv/1/song_requests/queue",
                     headers={"Nightbot-Channel":channel_id})
    try:
        song_title = (r.json()['_currentSong']['track']['title'])
        song_artist = (r.json()['_currentSong']['track']['artist'])
        f = open(file, 'r', encoding='utf-8')
        if (f.read()) != song_title:
            f = open(file, 'w', encoding='utf-8')
            print(f"Now playing: {song_artist} - {song_title}")
            # f.write(song_artist + " - " + song_title)
            f.write(song_title)
            f.close()
    except TypeError:
        print('Nothing playing...')
        # blank the file when nothing is playing
        f = open(file, 'w', encoding='utf-8')
        f.write("")
        f.close()

def main():
    channel_id = get_channel_id()

    while True:
        get_song(channel_id)
        time.sleep(5)

if __name__ == "__main__":
    main()
