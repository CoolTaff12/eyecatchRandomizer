# This is a sample Python script.

# Press Skift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# ----------------
# from io import BytesIO
# import numpy as np
# from random import *
# ----------------
# vlc name is python-vlc if you want to install it
import vlc
# In this case libvlc.dll will not be found. Make sure to install the 64bit-version
# ----------------


# Runs in Python 3.8.
# Package               version
# setuptools            65.5.2
# pip                   22.3.1
# numpy                 1.24.3
# wheel                 0.38.4
# python-vlc (vlc)      30.0.18122


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def eyecatch_p1(id):
    file = {
        1: ["mPw6ecM33QzSi48Y.mp3", 0.1],
        2: ["burunyaa.wav", 10.1],
        3: ["suicide_eng.wav", 10.1],
        4: ["Laughs_in_muda.mp3", 10.1]
    }
    play_the_fanfare = vlc.MediaPlayer('SFX/'+str(file.get(id)[0]))
    play_the_fanfare.play()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
