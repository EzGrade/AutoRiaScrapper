from bs4 import BeautifulSoup


class Parser:
    def __init__(self, html):
        self.soup = BeautifulSoup(html, 'html.parser')

    def GetCarLinks(self):
        ticket_items = self.soup.find_all('section', class_='ticket-item')
        car_links = []
        for ticket_item in ticket_items:
            car_links.append(ticket_item.find('a', class_="m-link-ticket").get('href'))
        return car_links

    def GetPageNumber(self):
        self.soup = self.soup.find('nav', class_='unstyle pager')
        last_page_button = self.soup.find_all('span', class_='page-item mhide')[-1]
        last_page_text = last_page_button.find('a', class_='page-link').text
        return int(last_page_text.replace(' ', ''))

    def ParseTicket(self):
        title_element = self.soup.find("h3", class_="auto-content_title")
        title = title_element.text

        price_element = self.soup.find("div", class_="price_value")
        price_usd = price_element.find("strong").text
        formatted_price_usd = price_usd.replace(' ', '').replace('$', '')

        odometer_element = self.soup.find("div", class_="base-information bold")
        odometer_text = odometer_element.find("span").text
        odometer_raw = odometer_text.replace("тиc. км", "").replace(" ", "")
        odometer = int(odometer_raw) * 1000

        username_element = self.soup.find("div", class_="seller_info_name bold")
        if username_element is None:
            username_element = self.soup.find(class_="seller_info_name")
        if username_element is None:
            username = ""
        else:
            username = username_element.text[1:]

        image_element = self.soup.find("div", class_="carousel-inner _flex")
        first_image_element = image_element.find("div")
        image_url_first = first_image_element.find("img")
        if image_url_first is None:
            image_url = ""
        else:
            image_url = image_url_first.get("src")

        images_count_element = self.soup.find("div", class_="count-photo left")
        images_count = int(images_count_element.find("span", class_="mhide").text.split(" ")[1])

        car_number_element = self.soup.find("span", class_="state-num ua")
        if car_number_element is not None:
            car_number = car_number_element.text.split(" ")[:3]
            car_number = " ".join(car_number)
        else:
            car_number = ""

        car_vin_element = self.soup.find("span", class_="label-vin")
        if car_vin_element is None:
            car_vin_element = self.soup.find("span", class_="vin-code")
        if car_vin_element is not None:
            car_vin = car_vin_element.text
        else:
            car_vin = ""

        return {
            "title": title,
            "price_usd": formatted_price_usd,
            "odometer": odometer,
            "username": username,
            "image_url": image_url,
            "images_count": images_count,
            "car_number": car_number,
            "car_vin": car_vin
        }

    def GetUserId(self):
        script_tag = self.soup.select_one('script[class^="js-user-secure"]')
        class_name = script_tag.get('class')[0]
        user_id = class_name.split('-')[-1]
        return user_id

    def GetPhoneId(self):
        a_tag = self.soup.find('a', id='openPopupCommentSeller')
        if a_tag is None:
            return None
        return a_tag.get('data-phone-id')

    def GetProfilePictureUrl(self):
        section = self.soup.find('section', id='userInfoBlockMobile')
        if section is None:
            return None
        return section.find('img', class_="img").get('src')
