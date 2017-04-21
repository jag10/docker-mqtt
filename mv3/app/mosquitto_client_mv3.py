# -*- coding: utf-8 -*-

from optparse import OptionParser
import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # COMPLETAR: Suscribirse a un topic
    client.subscribe("topic1/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # COMPLETAR: Tratar el mensaje
    print(msg.topic+" "+str(msg.payload))
    if "COMPLETA" in msg.topic:
        pass # Quita esto cuando lo completes. Al mensaje se accede con msg.payload



if __name__=='__main__':
    parser= OptionParser(usage="%prog -b <broker-IP> -m <mongo-IP>")
    parser.add_option("-b", "--brokerip", action="store", dest="brokerip", metavar="<broker-IP>",default="localhost",
                      help= "IP del broker MQTT al que se conectará este cliente. Por defecto es localhost")

    (opciones, args) = parser.parse_args()

    ip_broker = opciones.brokerip

    client_mqtt = mqtt.Client()
    client_mqtt.on_connect = on_connect
    client_mqtt.on_message = on_message
    client_mqtt.connect(ip_broker, 1883, 60)

    client_mqtt.loop_forever()

