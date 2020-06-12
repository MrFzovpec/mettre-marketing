import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import InvalidArgumentException
from secret import get_username, get_password
import time


class InstagramInteraction:
    def __init__(self, url: str, driver=webdriver.Chrome):
        options = Options()
        self.driver = driver(ChromeDriverManager().install(), chrome_options=options)
        self.url = url
        self.data = []

    def login(self, login=get_username(), password=get_password()):
        ''' Logining function '''
        u_input = self.driver.find_element_by_css_selector('input[name="username"]')
        u_input.send_keys(login)
        p_input = self.driver.find_element_by_css_selector('input[name="password"]')
        p_input.send_keys(password)

        login_btn = self.driver.find_element_by_css_selector(".DhRcB")
        login_btn.click()

    def simple_post_login_initializer(self):
        '''
            When we're just coming to the Instagram page and clicking on the post it's asking us to log in
            This function does this thing
        '''
        # Login into Instagram in order to parse the page
        login_div = self.driver.find_element_by_css_selector('div.ZcHy5 > span.r9-Os > a.tdiEy > button.sqdOP')
        self.driver.execute_script("arguments[0].click();", login_div)
        time.sleep(5)
        self.login()
        time.sleep(5)

        # Relocating back to the searchable page
        self.driver.get(self.url)
