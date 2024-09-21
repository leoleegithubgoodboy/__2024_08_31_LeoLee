#from machine import Pin
import machine
#led = Pin("LED",Pin.OUT)
#led = machine.Pin("LED",machine.Pin.OUT)
led = machine.Pin("LED",mode = machine.Pin.OUT)
#led.value(1)
led.on()