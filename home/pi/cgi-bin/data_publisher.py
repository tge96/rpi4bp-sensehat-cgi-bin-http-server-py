import csv
import json
import paho.mqtt.client as paho # pip3 install paho-mqtt
import ssl
import time

def on_connect(client, userdata, flags, rc):
	print("Connection returned result: ", + str(rc))

def on_message(client, userdata, msg):
	print(msg.topic + " " + str(msg.payload))

mqttc = paho.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message

awshost =  "1234-ats.iot.ap-south-1.amazonaws.com" #broker endpoint URL: AWS IoT:Setting tab
awsport = 8883
clientId = "crawlerzaws"
thingName = "crawlerzaws"
caPath = "root-CA.crt"
certPath = "crawlerzaws.cert.pem"
keyPath = "crawlerzaws.private.key"

mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
mqttc.connect(awshost, awsport ,keepalive=60)
mqttc.loop_start() 

with open(r"/home/pi/iot.txt") as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	for row in csv_reader:
		#print(row)
		payload = json.dumps({'temperature':row[0], 'humidity':row[1], 'pressure':row[2], 'timestamp':row[3]})
		#print(payload)
		mqttc.publish("iot", payload, qos=0) #qos=0 means "fire and forget"
		time.sleep(1) 
