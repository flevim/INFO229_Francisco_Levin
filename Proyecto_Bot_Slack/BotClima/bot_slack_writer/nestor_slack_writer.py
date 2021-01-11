#!/usr/bin/env python
import pika
import time
import os
from slack import WebClient

time.sleep(30)

CANAL_SLACK = "#general"


##### CONNEXIÓN A SLACK ########

# Create a slack client
slack_web_client = WebClient(token=os.environ.get("SLACK_TOKEN"))


########## ESPERA Y PUBLICA UN MENSAJE EN SLACK CUANDO RECIBE UN MENSAJE ####

def callback(ch, method, properties, body):
    text = body.decode()
    message = {
            "channel": CANAL_SLACK,
            "blocks": [
                {"type": "section", "text": {"type": "mrkdwn", "text": text}},
            ],
        }
    #PUBLICACION DEL MENSAJE EN SLACK
    slack_web_client.chat_postMessage(**message)

########### CONNEXIÓN A RABBIT MQ #######################
HOST = os.environ['RABBITMQ_HOST']

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=HOST))
channel = connection.channel()

#El consumidor utiliza el exchange 'nestor'
channel.exchange_declare(exchange='ultiminio', exchange_type='topic', durable=True)

#Se crea un cola temporaria exclusiva para este consumidor (búzon de correos)
result = channel.queue_declare(queue="publicar_slack", exclusive=True, durable=True)
queue_name = result.method.queue

#La cola se asigna a un 'exchange'
channel.queue_bind(exchange='ultiminio', queue=queue_name, routing_key="publicar_slack")

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()

