import json
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
        await self._producer.start()

    async def Stop(self):
        await self._producer.stop()

    async def ProduceMessage(self, data: dict) -> bool:
        message = json.dumps(jsonable_encoder(data)).encode("utf-8")
        response = await self._producer.send_and_wait(
            ConfigSettings.BLOGGING_TOPIC_NAME, value=message
        )
        print(response)
        return response
