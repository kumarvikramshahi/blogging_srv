from elasticsearch import AsyncElasticsearch
from config import ConfigSettings
import logging


class ElasticDbConnection:
    ElasticClient: AsyncElasticsearch = None

    def __init__(self) -> None:
        pass

    def Init(self):
        self.ElasticClient = AsyncElasticsearch(
            ConfigSettings.ELASTIC_HOST,
            basic_auth=(ConfigSettings.ELASTIC_USER, ConfigSettings.ELASTIC_PASSWORD),
        )
        logging.info("Connected to Elastic DB")
