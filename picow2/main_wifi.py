import tool

from machine import Pin, PWM, ADC , Timer ,RTC

tool.connect()

rtc = RTC()
adc = machine.ADC(4)
conversion_factor = 3.3 / (65535)
def do_thing(t1):
    reading = adc.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    print()
    print(f"電壓:{reading}")
    print(f"溫度:{temperature}")
    (year, month, day, hour, minute, second, microsecond, tzinfo)=rtc.datetime()
    datetime_str=f"{year}-{month}-{day}  {hour}:{minute}:{second}:{microsecond}_{tzinfo}"
    print(datetime_str)
    print(tool.wlan.ifconfig())
    print(f"status = {tool.wlan.status()}")
def do_thing1(t2):
    pwm1 = PWM(Pin(15),freq=1000)
    adc1 = ADC(Pin(26))
    duty1 = adc1.read_u16()
    #pwm1.freq(1000)
    pwmd = pwm1.duty_u16(duty1)
    print()
    #print(f"可變電阻{round(duty1/65535*10)}")
    print(f"{duty1}")
    
t1 = Timer(period=2000, mode=Timer.PERIODIC, callback=do_thing )
t2 = Timer(period=500, mode=Timer.PERIODIC, callback=do_thing1 )

