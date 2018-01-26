#!/usr/bin/env python3

# -*- coding: utf-8 -*-
# @Author: Gaël Barbier
# @Date:   2018-01-26 17:22:54
# @Last Modified by:   Gaël Barbier
# @Last Modified time: 2018-01-26 17:48:43

import pika

queuename = 'queue1'

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue=queuename)

channel.basic_consume(callback,
                      queue=queuename,
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()