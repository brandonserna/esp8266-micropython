# Original code from https://randomnerdtutorials.com/micropython-relay-module-esp32-esp8266/

try:
    import usocket as socket
except:
    import socket

from machine import Pin
import network

import esp

esp.osdebug(None)

import gc

gc.collect()

ssid = "<your-ssid>"
password = "<your-password>"

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
    pass

print("Connection successful")
print(station.ifconfig())

# onboard led 
led = Pin(2, Pin.OUT).value(0)
