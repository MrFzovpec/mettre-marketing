from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from instagram.secret import get_username, get_password
import time

INSTAGRAM_LINK = 'https://www.instagram.com/'

class InstagramInteraction:
    def __init__(self, driver=webdriver.Chrome, debug=0):
        options = Options()
        if not debug:
            options.add_argument('--headless')

        self.driver = driver(ChromeDriverManager().install(), chrome_options=options)
        self.data = []
        self.driver.get(INSTAGRAM_LINK)
        self.login()

    def wait_by_css_selector(self, selector):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector))
        )

    def login(self, login=get_username(), password=get_password()):
        ''' Logining function '''
        self.wait_by_css_selector('input[name="username"]')

        u_input = self.driver.find_element_by_css_selector('input[name="username"]')
        u_input.send_keys(login)
        p_input = self.driver.find_element_by_css_selector('input[name="password"]')
        p_input.send_keys(password)

        login_btn = self.driver.find_element_by_css_selector(".DhRcB")
        login_btn.click()

        self.wait_by_css_selector('div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM')