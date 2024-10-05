#! usr/bin/micropython
'''
led->gpio15
光敏電阻->gpio28
可變電阻->gpio26
內建溫度->adc最後1pin,共5pin
'''

#import tool
from machine import Pin, PWM, ADC , Timer ,RTC


def do_thing(t1):
    '''
    :param t1:Timer的實體
    負責溫度和光線
    每兩秒執行一次
    '''
    conversion_factor = 3.3 / (65535)
    reading = adc.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    print()
    print("--------------------------")
    print(f"電壓:{reading}")
    print(f"溫度:{temperature}")  
    adc_value = adc_light.read_u16()
    print(f"光線:{adc_value}")
    print("--------------------------")
    (year, month, day, hour, minute, second, microsecond, tzinfo)=rtc.datetime()
    datetime_str=f"{year}-{month}-{day}  {hour}:{minute}:{second}:{microsecond}_{tzinfo}"
    print(datetime_str)
    print(tool.wlan.ifconfig())
    print(f"status = {tool.wlan.status()}")
def do_thing1(t2):
    '''
    :parma t2:Timer的實體
    負責可變電阻可改LED亮度
    '''    
    
    duty1 = adc1.read_u16()
    #pwm1.freq(1000)
    pwmd = pwm1.duty_u16(duty1)
    print()
    #print(f"可變電阻{round(duty1/65535*10)}")
    print(f"可變電阻:{duty1}")

def main():
    t1 = Timer(period=2000, mode=Timer.PERIODIC, callback=do_thing )
    t2 = Timer(period=500, mode=Timer.PERIODIC, callback=do_thing1 )

if __name__ == '__main__':
    #tool.connect()
    #rtc = RTC()
    adc = machine.ADC(4) #內建溫度
    adc1 = ADC(Pin(26)) #可變電阻
    adc_light = ADC(Pin(28)) #光線
    pwm1 = PWM(Pin(15),freq=1000) #pwm     
    
    main()
