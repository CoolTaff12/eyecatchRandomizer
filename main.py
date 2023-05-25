# This is a sample Python script.

# Press Skift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# ----------------
from os import listdir
from os.path import isfile, join
import random
import time
# ----------------
# vlc name is python-vlc if you want to install it
import vlc
# In this case libvlc.dll will not be found. Make sure to install the 64bit-version
# ----------------

mypath = ['Eyecatch_in/', 'Eyecatch_out/']

# Runs in Python 3.8.
# Package               version
# setuptools            65.5.2
# pip                   22.3.1
# numpy                 1.24.3
# wheel                 0.38.4
# python-vlc (vlc)      30.0.18122


def eyecatch_in():
    onlyfiles1 = [f for f in listdir(mypath[0]) if isfile(join(mypath[0], f))]
    onlyfiles2 = [f for f in listdir(mypath[1]) if isfile(join(mypath[1], f))]
    random.shuffle(onlyfiles1)
    random.shuffle(onlyfiles2)

    # creating a media player object
    media_player = vlc.MediaListPlayer()

    # creating Instance class object
    player = vlc.Instance()

    # creating a new media list object
    media_list = player.media_list_new()

    # creating a new media
    media = player.media_new(mypath[0] + str(onlyfiles1[0]))

    # adding media to media list
    media_list.add_media(media)

    # setting media list to the media player
    media_player.set_media_list(media_list)

    # creating a new media
    media = player.media_new(mypath[1] + str(onlyfiles2[0]))

    # adding media to media list
    media_list.add_media(media)

    # setting media list to the media player
    media_player.set_media_list(media_list)

    # start playing video
    media_player.play_item_at_index(0)
    time.sleep(0.5)
    time.sleep(media_list[0].get_duration() / 1000)

    # playing next media in list
    media_player.next()

    # wait so the video can be played for 5 seconds
    # irrespective for length of video
    time.sleep(media_list[1].get_duration() / 1000)

    media_player.stop()

    # preloaded


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    eyecatch_in()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
