from machine import Timer , Pin

green_led = Pin("LED",Pin.OUT)
green_count = 0
def green_led_mycallback(t:Time):
    global green_count
    green_count += 1
    #print(f"目前mycallback被執行:{count}次")
    green_led.toggle()
    if green_count%2 == 0:
        print(f"目前green_led_mycallback被執行:{(int)(green_count/2)}次")
    if green_count >= 10:
        t.deinit()

green_led_time = Timer(period = 1000,mode = Timer.PERIODIC,callback = green_led_mycallback)


red_led = Pin(15,Pin.OUT)
red_count = 0
def red_led_mycallback(t:Time):
    global red_count
    red_count += 1
    #print(f"目前mycallback被執行:{count}次")
    red_led.toggle()
    if red_count%2 == 0:
        print(f"目前red_led_mycallback被執行:{(int)(red_count/2)}次")
    if red_count >= 10:
        red_led.off()
        t.deinit()
red_led_time = Timer(period = 2000,mode = Timer.PERIODIC,callback = red_led_mycallback)
