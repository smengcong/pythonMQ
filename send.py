import pika
#连接MQ服务器
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
#创建队列
channel.queue_declare(queue='hello')
#通过交换机将信息投递到指定队列
channel.basic_publish(exchange='',routing_key='hello',body='hello world!')
print("[x] sent hello world!")
#关闭连接
connection.close()
