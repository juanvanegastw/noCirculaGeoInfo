import asyncio
import os
from aiokafka import AIOKafkaConsumer
import pymongo
import json
from src.toolutils import structure_message
TOPIC_NAME = os.environ['TWITTER_TRACK']
SERVER = os.environ['MY_IP']
PORT = 9092
myclient = pymongo.MongoClient("mongodb://"+SERVER+":27017/")
mydb = myclient["hoynocircula"]
mycol = mydb["entry"]
print(SERVER)
print(TOPIC_NAME)


async def consume(consumer, consumer_id):
    await consumer.start()
    async for msg in consumer:
        structured_message = structure_message(msg.value['text'])
        is_data = structure_message.get('hologramas', []) and structure_message.get('placas', []) and \
                  structure_message.get('color', '')
        if is_data:
            mycol.insert({'consume_id': consumer_id, 'message': structured_message, 'user': msg.value['user']})
    await consumer.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    first_consumer = AIOKafkaConsumer(
        TOPIC_NAME,
        loop=loop,
        bootstrap_servers=f'{SERVER}:{PORT}',
        value_deserializer=lambda v: json.loads(v.decode('utf-8'))
    )

    second_consumer = AIOKafkaConsumer(
        TOPIC_NAME,
        loop=loop,
        bootstrap_servers=f'{SERVER}:{PORT}',
        value_deserializer=lambda v: json.loads(v.decode('utf-8'))
    )

    loop.run_until_complete(
        asyncio.wait([consume(first_consumer, 'first_consumer'), consume(second_consumer, 'second_consumer')])
    )
