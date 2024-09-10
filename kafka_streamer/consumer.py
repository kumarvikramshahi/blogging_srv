import httpx
import logging
from aiokafka import AIOKafkaConsumer, TopicPartition
from config import ConfigSettings


class Consumer:
    _consumer: AIOKafkaConsumer = None

    def __init__(self) -> None:
        pass

    async def Init(self):
        self._consumer = AIOKafkaConsumer(
            ConfigSettings.BLOGGING_TOPIC_NAME,
            bootstrap_servers=ConfigSettings.KAFKA_BROKER,
            enable_auto_commit=False,
            group_id=ConfigSettings.BLOGGING_TOPIC_NAME,
        )
        await self._consumer.start()

    async def Stop(self):
        await self._consumer.stop()

    async def ConsumeMessage(self):
        async for msg in self._consumer:
            data = msg.value.decode("utf-8")
            try:
                async with httpx.AsyncClient() as client:
                    resp = await client.post(
                        "http://localhost:3000/blogging/v1/save_blog", data=data
                    )
                    if resp.status_code != 200:
                        logging.error(
                            f"non-success response from save_blog endpoint - {resp.json()}"
                        )
            except Exception as error:
                logging.error(f"{error} - error at consumer while sendind blog data")

            tp = TopicPartition(msg.topic, msg.partition)
            await self._consumer.commit({tp: msg.offset + 1})
