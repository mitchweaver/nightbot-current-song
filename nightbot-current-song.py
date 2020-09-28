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
        musicName = (r.json()['_currentSong']['track']['title'])
        f = open(file, 'r', encoding='utf-8')
        if (f.read()) != musicName:
            f = open(file, 'w', encoding='utf-8')
            print(f"Now playing: {musicName}")
            f.write(musicName)
            f.close()
    except TypeError:
        print('Nothing playing...')

def main():
    channel_id = get_channel_id()

    while True:
        get_song(channel_id)
        time.sleep(10)

if __name__ == "__main__":
    main()
