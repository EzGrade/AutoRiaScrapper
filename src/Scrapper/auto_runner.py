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
        os.system("python D:\\AutoRiaScrapper\\src\\Scrapper\\main.py")

    def run(self):
        schedule.every().day.at(self.time).do(self.job)

        while True:
            schedule.run_pending()
            time.sleep(30)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    runner = Runner()
    runner.run()
