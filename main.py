import time
time.sleep(1)

#Peer 
from mac import get_peer_mac
from peer import peer
peer = get_peer_mac(peer)

#Leds
from machine import Pin
ylw = Pin(27, Pin.OUT)
grn = Pin(14, Pin.OUT)
red = Pin(32, Pin.OUT)

import time
import network
import espnow
import uasyncio

sta = network.WLAN(network.STA_IF)  # Or network.AP_IF
sta.active(True)
sta.disconnect()      # For ESP8266ValueError


ylwb =  Pin(18, Pin.IN, Pin.PULL_UP)
grnb =  Pin(22, Pin.IN, Pin.PULL_UP)
redb =  Pin(15, Pin.IN, Pin.PULL_UP)
reds =  Pin(4, Pin.IN, Pin.PULL_UP)

def post(num):
    for x in range(num):
        grn.on()  ;  red.on();  ylw.on()
        time.sleep(1)
        grn.off()  ;  red.off();  ylw.off()
        time.sleep(1)

e = espnow.ESPNow()
e.active(True)
e.add_peer(peer)      # Must add_peer() before send()
    
""" In Coming """

def check_messages():
    
    if (received_messages[0] is None) and (received_messages[1] is None):
        print('No message')
    else:
        msg=received_messages[1].decode()
        check_content(msg)
        
def check_content(msg):
        print(msg)
        if msg == "red":
            red.on()  ; grn.off(); ylw.off()
            if reds.value() == 1:
                import music.buzzer_runner
        if msg == "green":    
            red.off()  ; grn.on(); ylw.off()
        if msg == "yellow":
            red.off()  ; grn.off(); ylw.on()
            
""" Out Going """
def check_button_values():
    
    if redb.value() == 0:
        send_2_peer("red")
    
    if grnb.value() == 0:
        send_2_peer("green")
        
    if ylwb.value() == 0:
        send_2_peer("yellow")
        

def send_2_peer(color):
    e.send(peer, color)

def retrieve_new_msgs():
    global received_messages
    received_messages = e.recv(timeout_ms=50)
    
post(2)
received_messages = None

while True:
    
    check_button_values()
    
    try:
        retrieve_new_msgs()
    except OSError as err:
        print(err)
    else:
        check_messages()
    
    time.sleep_ms(50)   
