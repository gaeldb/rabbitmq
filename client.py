#!/usr/bin/env python3

# -*- coding: utf-8 -*-
# @Author: gael barbier
# @Date:   2018-01-26 16:57:27
# @Last Modified by:   Gaël Barbier
# @Last Modified time: 2018-01-26 17:52:37

import pika
import sys

queuename = 'queue1'

# Connect RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

# Open a new channel
channel = connection.channel()

# Create new queue through this channel
channel.queue_declare(queue=queuename)

message = ''.join(sys.argv[1:3]) or 'Default message'

channel.basic_publish(exchange='',
                      routing_key=queuename,
                      body=message)

print(" [x] Sent %r" % message)



connection.close()

