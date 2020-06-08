from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import InvalidArgumentException


class GoogleParser:
    def __init__(self, driver=webdriver.Chrome, geo: str = 'RU'):
        '''
            The function initializes the Google Trends parser, which parses the data from their website
            :param driver: driver, which parser would work on
            :param geo: the geo zone
        '''
        options = Options()
        options.add_argument("--headless")
        self.driver = driver(ChromeDriverManager().install(), chrome_options=options)
        self.geo = geo

    def __call__(self):
        self.driver.get('https://trends.google.ru/trends/trendingsearches/daily?geo=' + self.geo)
        while True:
            try:
                button = self.driver.find_elements_by_class_name('feed-load-more-button')
                WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(button))
                button.click()
            except InvalidArgumentException:
                break


parser = GoogleParser()
parser()