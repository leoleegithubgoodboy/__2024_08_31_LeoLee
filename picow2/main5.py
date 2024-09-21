from machine import Pin
import time

pin15_red = Pin(15,Pin.OUT)
pin14_but = Pin(14,Pin.IN,Pin.PULL_DOWN)

while 1:
    if pin14_but.value():
        pin15_red.toggle()
        time.sleep(0.5)