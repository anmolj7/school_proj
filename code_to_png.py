from time import sleep
import urllib.parse
from selenium import webdriver
import os

CARBON = 'https://carbon.now.sh/?l=python&code={code}'

def get_carbon_image(fName):
    """
    Visit carbon.now.sh with the code, click the open button, take ss 
    """

    print(f'On File {fName}')

    global driver
    with open(fName) as f:
        code = f.read()

    code = urllib.parse.quote_plus(code)
    url = CARBON.format(code=code)


    driver.get(url)

    driver.find_element_by_xpath("//button[contains(text(),'Export')]").click()
    driver.find_element_by_xpath("//button[contains(text(),'Open')]").click()
    sleep(5)  # this might take a bit
    driver.save_screenshot(fName.strip('.py')+'.png')
    print(f"{fName.strip('.py')+'.png'} saved.")
    return True


if __name__ == '__main__':
    global driver
    driver = webdriver.Chrome(executable_path="chromedriver.exe")

    Files = os.listdir(os.getcwd())
    for file in Files:
        if os.path.isfile(file):
            if ".py" == file[-3:] and "ques" in file:
                get_carbon_image(file)
    driver.quit()