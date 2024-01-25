import io

from src.setup import setup_django

setup_django()

from django.core.management import call_command

import logging
import os
import time

import dotenv
import schedule


class Runner:
    def __init__(self):
        logging.info("Initializing runner")
        dotenv.load_dotenv()
        self.time = os.environ.get("TIME", "09:00")
        logging.info(f"Runner initialized with time: {self.time}")

    @staticmethod
    def job():
        logging.info("Running job")
        Runner.dump_data()
        os.system("python D:\\AutoRiaScrapper\\src\\Scrapper\\main.py")

    @staticmethod
    def dump_data():
        date = time.strftime("%Y-%m-%d")
        root_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(root_dir, f"../../dumps")
        with io.open(f"{path}/{date}.json", "w", encoding='utf-8') as file:
            call_command("dumpdata", "ticket", stdout=file, format='json')

    def run(self):
        schedule.every().day.at(self.time).do(self.job)

        while True:
            try:
                schedule.run_pending()
                time.sleep(30)
            except Exception as e:
                logging.error(e)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    runner = Runner()
    runner.run()