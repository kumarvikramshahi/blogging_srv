import json
import time
import logging
from fastapi.encoders import jsonable_encoder
from aiokafka import AIOKafkaProducer
from config import ConfigSettings


class Producer:
    _producer: AIOKafkaProducer = None

    def __init__(self) -> None:
        self._producer = AIOKafkaProducer(
            bootstrap_servers=ConfigSettings.KAFKA_BROKER, enable_idempotence=True
        )

    async def Init(self):
        for index in range(10):
            try:
                logging.info(f"Attempt ({index} of 10) to connect Kafka")
                await self._producer.start()
                break
            except Exception as error:
                logging.info("Failed to connect to Kafka, retrying in 2 seconds...")
                time.sleep(2)  # Wait

    async def Stop(self):
        await self._producer.stop()

    async def ProduceMessage(self, data: dict):
        message = json.dumps(jsonable_encoder(data)).encode("utf-8")
        response = await self._producer.send_and_wait(
            ConfigSettings.BLOGGING_TOPIC_NAME, value=message
        )
        return response
