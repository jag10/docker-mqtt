# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import time
from optparse import OptionParser
 
def on_publish(client, userdata, mid):
    print("mid: "+str(mid))


if __name__=='__main__':
    parser= OptionParser(usage="%prog -b <broker-IP> -m <mongo-IP>")
    parser.add_option("-b", "--brokerip", action="store", dest="brokerip", metavar="<broker-IP>",default="localhost",
                      help= "IP del broker MQTT al que se conectará este cliente. Por defecto es localhost")

    (opciones, args) = parser.parse_args()
    print("helloooo")
    ip_broker = opciones.brokerip

    client = mqtt.Client()
    client.on_publish = on_publish
    client.connect(ip_broker, 1883, 60)
    print(ip_broker, 'loll')
    (rc, mid) = client.publish("topic1", str(2), qos=1)

    #client.loop_start()
    #while True:
        #temperature = 2 #read_from_imaginary_thermometer()
        #(rc, mid) = client.publish("topic1", str(temperature), qos=1)
        #time.sleep(3)
        #print("iterating...")
