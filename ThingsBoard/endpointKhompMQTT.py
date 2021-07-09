import requests
import json
from datetime import datetime
import time
import sys
import random
import paho.mqtt.client as mqtt_client

json_data = None

STWIN_DIR = "./STWIN"

host = 'http://34.204.166.205:80/api/v1'
APIKEY_A = 'HdwAvKas5ZfogOQOGu21' #Vibration_A
APIKEY_B = 'u3E5SvQaYcR2nwjGWkaJ' #Vibration_B

broker = '52.201.224.181'
port = 1883
topic = "itg200/embrapii"
client_id = f'khomp-mqtt-{random.randint(0, 1000)}'
username = 'gregory'
password = 'Astra2010'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        payload = msg.payload.decode()
        print(f"Received `{payload}` from `{msg.topic}` topic")
        payload = """{"data":""" + payload + "}"""
        try:
            postOnTB(APIKEY_A, (payload))
            print(f"Sent: '{payload}'")
        except:
            print("Fail to connect to TB")
            time.sleep(5)

    client.subscribe(topic)
    client.on_message = on_message
 
def postOnTB(APIKEY, payload):
    requests.post(f'{host}/{APIKEY}/telemetry',json = json.loads(payload))  

def main():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()    
        

if __name__ == "__main__":
    main() 

# auth='3NHMOAtNXa4Kacn87q2e'

# r = requests.post('http://localhost:9090/api/v1/3NHMOAtNXa4Kacn87q2e/telemetry', json=json_data)