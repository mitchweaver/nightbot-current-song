#!/usr/bin/env python3

import time
from urllib.request import urlopen
import json
import requests

file = '/tmp/nightbot-current-song.txt'
f = open(file, 'w', encoding='utf-8')

while True:
    try:
        channelName = input('Channel name: ')
        channel_url = f'https://api.nightbot.tv/1/channels/t/{channelName}'
        channel_load = urlopen(channel_url)
        jsonList = json.load(channel_load)
        channel_id = jsonList['channel']['_id']
        print(f"Channel's id: {channel_id}")
        break
    except OSError:
        print('Channel not found, try again')
        time.sleep(3)

def get_song():
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

while True:
    get_song()
    time.sleep(10)
