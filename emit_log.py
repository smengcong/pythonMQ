import pika
import sys

# 连接MQ服务器
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# 创建交换机
channel.exchange_declare(exchange='logs',exchange_type='fanout')
messgae = ' '.join(sys.argv[1:]) or 'hello world!'
# 向交换机发送消息
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=messgae)
print('[x] sent %r'%(messgae,))
connection.close()