#from machine import Pin
import machine
import time
#led = Pin("LED",Pin.OUT)
#led = machine.Pin("LED",machine.Pin.OUT)
led = machine.Pin("LED",mode = machine.Pin.OUT)
#led.value(1)
status = True

while True:
    led.on()
    if status == False:
        led.on()
        status = True
    else:
        led.off()
        status = False
    time.sleep(1)
