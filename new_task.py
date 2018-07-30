import pika
import sys

# 连接MQ服务器
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# 创建队列
# channel.queue_declare(queue='hello')
# 消息持久化注意两点，将"队列"、"消息"设为持久化 durable=True
channel.queue_declare(queue='task_queue',durable=True)
#创建一个fanout类型的交换机，命名为logs
channel.exchange_declare(exchange='logs',type='fanout')

messgae = ' '.join(sys.argv[1:]) or 'hello world!'
# 通过交换机将信息投递到指定队列   现在可以发送消息到上面定义的交换机
channel.basic_publish(exchange='logs',
                      routing_key='task_queue',
                      body=messgae,
                      properties=pika.BasicProperties(
                          delivery_mode=2, #让消息持久化
                      ))
#同一时刻不会将超过一条消息分送给一个工作者，也就是说哪个工作者空闲就传给谁
channel.basic_qos(prefetch_count=1)
print("[x] sent %r" % (messgae,))
# 关闭连接
connection.close()
