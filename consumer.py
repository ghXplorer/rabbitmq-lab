import pika
import traceback, sys, time


conn_params = pika.ConnectionParameters('192.168.56.10', 5672)
connection = pika.BlockingConnection(conn_params)
channel = connection.channel()

channel.queue_declare(queue='first-queue', durable=True)

print("Waiting for messages. To exit press CTRL+C")

def on_message(ch, method, properties, body):
    print(body)
    time.sleep(1) #
    print('Done') #
    channel.basic_ack(delivery_tag=method.delivery_tag) #
    # acknowledges one or more messages. By default (without acks), when a broker comes back
    # online, it sends all "persistent" messages from a "durable" queue. Which could be very
    # overwhelming for a consumer.


channel.basic_consume('first-queue', on_message)

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
except Exception:
    channel.stop_consuming()
    traceback.print_exc(file=sys.stdout)
