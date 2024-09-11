from elasticsearch import AsyncElasticsearch
from config import ConfigSettings
import logging
import time


class ElasticDbConnection:
    ElasticClient: AsyncElasticsearch = None

    def __init__(self) -> None:
        pass

    async def Init(self):
        self.ElasticClient = AsyncElasticsearch(
            ConfigSettings.ELASTIC_HOST,
            basic_auth=(
                ConfigSettings.ELASTIC_USER,
                ConfigSettings.ELASTIC_PASSWORD,
            ),
        )
        if ConfigSettings.ENV_NAME == "dev":
            self.ElasticClient = AsyncElasticsearch(ConfigSettings.ELASTIC_HOST)

        logging.info("Connected to Elastic DB")
