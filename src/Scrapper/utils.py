import os

import dotenv


class Os:
    @staticmethod
    def LoadDotEnv():
        dotenv.load_dotenv(dotenv.find_dotenv())

    @staticmethod
    def GetEnv(key: str) -> str:
        try:
            return os.environ[key]
        except KeyError:
            raise KeyError(f"Key {key} not found in .env file")
