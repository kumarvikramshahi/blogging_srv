import os


class Settings:
    SERVICE_NAME = "blogging"

    ENV_NAME = os.getenv("ENV_NAME")
    PORT = os.getenv("PORT")
    API_TIMEOUT = os.getenv("API_TIMEOUT")

    LOG_LEVEL = os.getenv("LOG_LEVEL")


ConfigSettings = Settings()
