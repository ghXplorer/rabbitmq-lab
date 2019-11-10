import pika, time


conn_params = pika.ConnectionParameters('192.168.56.10', 5672)
connection = pika.BlockingConnection(conn_params)
channel = connection.channel()

channel.queue_declare(queue='first-queue', durable=True) # Makes a queue durable. So that it exists after reboot.

for i in range(100):
    channel.basic_publish(exchange='', routing_key='first-queue', body=f'Hi, consumer {i}!',
    					  properties=pika.BasicProperties(delivery_mode=2)) # Makes messages persistent.
    print("Greeting sent")
    time.sleep(2)

connection.close()
