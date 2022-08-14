import pika, json

params = pika.URLParameters('amqps://nggyfnxm:tfNJIGp8mrnJ2T6z1zMuSz3OB9LD8mX7@armadillo.rmq.cloudamqp.com/nggyfnxm')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='app')


def callback(ch, method, properties, body):
    print('Received in app')
    data = json.loads(body)
    print(data)

    if properties.content_type == 'users_created':
        print('User Created')

    elif properties.content_type == 'users_updated':
        print('User Updated')

    elif properties.content_type == 'users_deleted':
        print('User Deleted')


channel.basic_consume(queue='app', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()