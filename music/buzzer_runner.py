from time import sleep
from machine import Pin

from .buzzer_music import music

from .songs import darth_march as song_string
count=750

def play_song(mysong, count=500):
    """ Send an instance of music as mysong"""
    while count > 0:
        mysong.tick()
        sleep(0.04)
        count-=1
    mysong.stop()

#mySong = music(song_string, pins=[Pin(2)],duty=50000)   
mySong = music(song_string, pins=[Pin(13)],duty=50000)

play_song(mySong, count=count)
