from collections import namedtuple
from random import choice
import sys
from time import sleep
import urllib.parse

from bs4 import BeautifulSoup
import requests
from selenium import webdriver

TIPS_PAGE = 'https://codechalleng.es/tips'
PYBITES_HAS_TWEETED = 'pybites/status'
CARBON = 'https://carbon.now.sh/?l=python&code={code}'
TWEET = '''{tip} {src}
🐍 Check out / submit more @pybites tips at https://codechalleng.es/tips 💡
(image built with @carbon_app)
{img}
'''

def get_carbon_image(code):
    """Visit carbon.now.sh with the code, click the Tweet button
       and grab and return the Twitter picture url
    """
    code = urllib.parse.quote_plus(code)
    url = CARBON.format(code=code)

    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.get(url)

    driver.find_element_by_xpath("//button[contains(text(),'Export')]").click()
    driver.find_element_by_xpath("//button[contains(text(),'Open')]").click()
    sleep(10)  # this might take a bit
    print(driver.current_url)
    driver.save_screenshot("ss.png")

    driver.quit()
    return True


if __name__ == '__main__':

    with open('ques_2.py') as f:
        code = f.read()

    img = get_carbon_image(code)
    print(img)