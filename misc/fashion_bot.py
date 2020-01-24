from selenium.webdriver.remote.webelement import WebElement
from typing import List

from selenium import webdriver
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--username", help="Your Instagram username")
parser.add_argument("--password", help="Your Instagram password")
args = parser.parse_args()
url = "https://www.gq.com/gallery/the-menswear-essentials-youll-need-in-the-new-year"


class Item:
    def __init__(self, price: str, title: str, description: str):
        self.title = title
        self.price = float(price.replace("$", "").replace(",", "_"))
        self.desription = description.replace("\\", "")


class FashionBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.items: List[Item] = []

        png = self.driver.get_screenshot_as_png()

        # slides: WebElement = self.driver.find_elements_by_class_name("gallery-slide-caption")
        #
        # for slide in slides:
        #     title: WebElement = slide.find_element_by_class_name("gallery-slide-caption__hed")
        #     price: WebElement = slide.find_element_by_class_name("product-offer__price")
        #     description: WebElement = slide.find_element_by_css_selector("div.gallery-slide-caption__dek > div > "
        #                                                                  "p:nth-child(1)")
        #     try:
        #         if price != "N/A":
        #             self.items.append(Item(price=price.text, description=description.text, title=title.text))
        #     except ValueError:
        #         print(f"Item could not be added: \nTitle: {title}\nPrice: {price}\nDescription: {description}")
        #
        # print(f"Total cost: {sum([item.price for item in self.items])}")


if __name__ == "__main__":
    FashionBot()
