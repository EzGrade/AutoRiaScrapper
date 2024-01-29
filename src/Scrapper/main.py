import time

from src.setup import setup_django

setup_django()

import requests
from selenium import webdriver
import logging
import dotenv
import os

from parser import Parser
from src.AutoRia.ticket.serializers import TicketSerializer


class Scrapper:
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/json',
        'Content-Length': '739',
        'Referer': '',
        'X-Ria-Source': 'vue3-0.0.1',
        'Origin': 'https://auto.ria.com',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'DNT': '1',
        'Sec-GPC': '1',
        'Connection': 'keep-alive'
    }

    def __init__(self):
        dotenv.load_dotenv()
        if os.environ.get("HEADLESS") == "True":
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            self.driver = webdriver.Chrome(options=options)
        else:
            self.driver = webdriver.Chrome()
        self.delay = os.environ.get("DELAY", 1)
        self.url = "https://auto.ria.com/car/used/"
        self.page_number = 0
        self.car_links = []
        self.data = {}

    def __GetPageNumber(self):
        self.__GetPage()
        self.page_number = Parser(self.driver.page_source).GetPageNumber()

    def __GetPage(self, page: int = 1):
        url = self.url + f"?page={page}"
        self.driver.get(url)

    def __GetCarLinks(self):
        self.car_links = Parser(self.driver.page_source).GetCarLinks()

    def __GenerateCookie(self):
        cookie = self.driver.get_cookies()
        cookie_dict = [{
            "name": i['name'],
            "value": i['value']
        } for i in cookie]
        keys = [
            "_ga_KGL740D7XD",
            "_ga",
            "ui",
            "_gcl_au",
            "showNewFeatures",
            "extendedSearch",
            "showNewFinalPage",
            "informerIndex",
            "PHPSESSID",
            "test_new_features",
            "advanced_search_test",
            "ipp",
            "promolink2",
            "gdpr",
            "_504c2",
            "ria_sid"]
        result = [f"{i['name']}={i['value']}" for i in cookie_dict if i['name'] in keys]
        return result

    def __GetPhoneNumber(self):
        url = "https://auto.ria.com/bff/final-page/public/auto/popUp/"
        cookies_list = self.driver.get_cookies()
        cookies_dict = {cookie['name']: cookie['value'] for cookie in cookies_list}
        headers = self.header
        headers['Referer'] = self.driver.current_url
        headers['Cookie'] = "; ".join(self.__GenerateCookie())

        current_url = self.driver.current_url

        ticket_id = current_url.split("/")[-1].replace(".html", "").split("_")[-1]
        parser = Parser(self.driver.page_source)
        user_id = parser.GetUserId()
        phone_id = parser.GetPhoneId()
        profile_picture = parser.GetProfilePictureUrl()
        data = {
            "blockId": "autoPhone",
            "isLoginRequired": False,
            "autoId": int(ticket_id),
            "data": [["userId", user_id],
                     ["phoneId", phone_id],
                     ["title", self.data['title']],
                     ["isCheckedVin", "1"],
                     ["avatar", profile_picture],
                     ["userName", self.data['username']],
                     ["isCardPayer", "1"],
                     ["dia", ""],
                     ["isOnline", ""],
                     ["srcAnalytic",
                      "sellerInfoFloat_sellerInfoRowFloat_sellerInfoUserGridFloat_sellerInfoPhoneFloat_showBottomPopUp"]]
        }
        response = requests.post(url, cookies=cookies_dict, headers=headers, json=data)
        return response.json()

    def __AddTicket(self):
        serializer = TicketSerializer(data=self.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return True
            return False
        except Exception as e:
            logging.warning(e)
            return False

    def RunScrapper(self):
        logging.info("Scrapper started")
        self.__GetPageNumber()
        for page in range(1, self.page_number + 1):
            self.__GetPage(page)
            self.__GetCarLinks()
            for car_link in self.car_links:
                self.driver.get(car_link)
                time.sleep(self.delay)
                html = self.driver.page_source
                try:
                    self.data = Parser(html).ParseTicket()
                except Exception as e:
                    logging.warning(e)
                    continue
                additional_params = self.__GetPhoneNumber().get('additionalParams', None)
                if additional_params is not None:
                    phone_str = additional_params.get('phoneStr')
                    self.data['phone_number'] = phone_str
                self.data['url'] = car_link
                self.__AddTicket()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    scrapper = Scrapper()
    scrapper.RunScrapper()
