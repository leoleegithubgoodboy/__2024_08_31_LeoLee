import time
import binascii
import machine
from umqtt.simple import MQTTClient
from machine import Pin
import tool

def main():
    try:        
        tool.connect()
        mqtt = MQTTClient(CLIENT_ID, SERVER,user='pi',password='raspberry')
        mqtt.connect()
        #print("Connected to %s, waiting for button presses" % server)
        while True:
                mqtt.publish(TOPIC, b"24.516")
                time.sleep_ms(2000)
    except Exception:
        mqtt.disconnect()
    
if __name__ == '__main__':
   # Default MQTT server to connect to
    SERVER = "192.168.0.252"
    CLIENT_ID = binascii.hexlify(machine.unique_id())
    TOPIC = b"SA-28/臥室/溫度"
    
    main()