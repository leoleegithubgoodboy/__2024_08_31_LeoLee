import paho.mqtt.client as mqtt
from datetime as datetime
import csv,os
def on_connect(client, userdata, flags, reason_code, properties):
    #連線bloker成功時,只會執行一次
    client.subscribe("SA-28/#")

def on_message(client, userdata, msg):
    global led_S_value
    topic = msg.topic
    value = msg.payload.decode()
    if topic == "SA-28/LED_LEVEL":
        led_value = int(value)
        if led_value != led_S_value:
            led_S_value = led_value  #####  建立變數區域變數，所以必須要有global
            print(f'led_value:{led_value}')
            
    #print(f"Received message '{msg.payload.decode()}' on topic '{msg.topic}'")
def record(r):
    pass


def main():
    client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
    # 設定用戶名和密碼
    username = "pi"  # 替換為您的用戶名
    password = "raspberry"  # 替換為您的密碼
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("192.168.0.252", 1883, 60)
    client.loop_forever()


if __name__ == "__main__":
    led_S_value = 0
    main()