import io
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
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
        self.root_dir = os.path.dirname(os.path.abspath(__file__))
        logging.info(f"Root dir: {self.root_dir}")

    def job(self):
        logging.info("Running job")
        self.dump_data()
        main_path = os.path.join(self.root_dir, f"{self.root_dir}/main.py")
        os.system(f"python {main_path}")

    def dump_data(self):
        date = time.strftime("%Y-%m-%d")
        path = os.path.join(self.root_dir, f"../../dumps")
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
