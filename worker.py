import pika
import time
#连接MQ服务器
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='task_queue',durable=True)
#定义回调函数
def callback(ch,method,properties,body):
    strbody = str(body,encoding='utf-8')
    print("[x] Received %r"%(strbody,))
    time.sleep(strbody.count('.'))
    print('[x] done')
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
#no_ack是为了让消费者消化完后返回响应 让MQ释放并删除这条消息
# channel.basic_consume(callback,queue='hello',no_ack=True)
channel.basic_consume(callback,queue='task_queue')

print('waiting for messages.')
channel.start_consuming()