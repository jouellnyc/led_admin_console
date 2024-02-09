from buzzer_music import music
from time import sleep

from machine import Pin
from songs import song

#One buzzer on pin 0
#mySong = music(song, pins=[Pin(0)])

#Two buzzer
Buzz1 = Pin(14)
mySong = music(song, pins=[Buzz1])

count = 370
while count > 0 :
    print(mySong.tick())
    sleep(0.04)
    count-=1
mySong.stop()    