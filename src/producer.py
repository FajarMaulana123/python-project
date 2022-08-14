import pika, json

params = pika.URLParameters('amqps://nggyfnxm:tfNJIGp8mrnJ2T6z1zMuSz3OB9LD8mX7@armadillo.rmq.cloudamqp.com/nggyfnxm')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='app', body=json.dumps(body), properties=properties)