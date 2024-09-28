
"""
範例一 用時間暫停來做動作(系統暫停在做事)
import machine 
import time

adc = machine.ADC(4)
conversion_factor = 3.3 / (65535)
while True:    
    reading = adc.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    print()
    print(f"電壓:{reading}")
    print(f"溫度:{temperature}")
    time.sleep(3)
"""


#範例二 用每隔幾次來做動作 (系統持續做當時間到才做動作)
from machine import Timer,ADC

adc = machine.ADC(4)
conversion_factor = 3.3 / (65535)
def do_thing(t):
    reading = adc.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    print()
    print(f"電壓:{reading}")
    print(f"溫度:{temperature}")
 

Timer(period=2000, mode=Timer.PERIODIC, callback=do_thing )