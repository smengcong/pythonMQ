import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

#临时队列exclusive
result = channel.queue_declare(exclusive=True)
#获取临时队列的名称并绑定
queue_name = result.method.queue
channel.queue_bind(exchange='logs',
                   queue=queue_name)
print(queue_name)
print("waiting for logs.")

def callback(ch,method,properties,body):
    print("[x] %r" % (body,))

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()