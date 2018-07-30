import pika
#连接MQ服务器
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
#定义回调函数
def callback(ch,method,properties,body):
    print("[x] Received %s" %body)

channel.basic_consume(callback,queue='hello',no_ack=True)

print('waiting for messages.')
channel.start_consuming()