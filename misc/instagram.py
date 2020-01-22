from selenium import webdriver
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument("--username", help="Your Instagram username")
parser.add_argument("--password", help="Your Instagram password")
args = parser.parse_args()

class InstaBot:
    def __init__(self, username, pw):
        self.driver: webdriver.Chrome = webdriver.Chrome()
        self.driver.get("https://www.instagram.com")
        self.driver.find_element_by_xpath("//a[contains(text()='Log in')]").click()
        time.sleep(2)

if __name__ == "__main__":
    InstaBot(args.username, args.password)