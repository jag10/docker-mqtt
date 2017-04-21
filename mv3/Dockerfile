FROM python:2.7
#WORKDIR /app
ENV IP_BROKER "172.17.0.4"
ENV IP_MONGO "172.17.0.5"
ADD requeriments.txt ./requeriments.txt
RUN pip install -r ./requeriments.txt
#ADD * /app/
ADD mqtt_sub.py ./mqtt_sub.py
CMD python ./mqtt_sub.py -b $IP_BROKER #-m $IP_MONGO
