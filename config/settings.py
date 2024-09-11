import os


class Settings:
    SERVICE_NAME = "blogging"

    ENV_NAME = os.getenv("ENV_NAME")
    PORT = os.getenv("PORT")
    API_TIMEOUT = os.getenv("API_TIMEOUT")

    LOG_LEVEL = os.getenv("LOG_LEVEL")

    KAFKA_BROKER = os.getenv("KAFKA_BROKER")
    BLOGGING_TOPIC_NAME = os.getenv("BLOGGING_TOPIC_NAME")

    MONGODB_USER = os.getenv("MONGODB_USER")
    MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")
    MONGODB_HOST = os.getenv("MONGODB_HOST")
    MONGODB_NAME = os.getenv("MONGODB_NAME")

    ELASTIC_PASSWORD = os.getenv("ELASTIC_PASSWORD")
    ELASTIC_HOST = os.getenv("ELASTIC_HOST")
    ELASTIC_USER = os.getenv("ELASTIC_USER")

    SELF_HOST=os.getenv("SELF_HOST")
