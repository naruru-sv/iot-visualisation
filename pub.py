import paho.mqtt.client as paho
import time
import random

#hostname
broker="127.0.0.1"

#port
port=1883

def on_publish(client,userdata,result):
    print("Message published.")
    pass

client= paho.Client("admin")
client.on_publish = on_publish
client.connect(broker,port)
    
while True:
    
 #telemetry to send 
	message="Message : " + str(random.randint(1,100))
	    
 #publish message
	ret= client.publish("/data",message)
	time.sleep(5)  

print("Stopped...")
