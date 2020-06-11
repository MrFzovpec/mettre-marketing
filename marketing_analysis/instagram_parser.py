import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import InvalidArgumentException
import time


class InstagramPageParser():
    def __init__(self, url: str, driver=webdriver.Chrome):
        options = Options()
        self.driver = driver(ChromeDriverManager().install(), chrome_options=options)
        self.url = url

    def login(self, login='username', password='password'):
        ''' Logining user '''
        u_input = self.driver.find_element_by_css_selector('input[name="username"]')
        u_input.send_keys(login)
        p_input = self.driver.find_element_by_css_selector('input[name="password"]')
        p_input.send_keys(password)

        login_btn = self.driver.find_element_by_css_selector(".DhRcB")
        login_btn.click()

    def __call__(self):
        self.driver.get(self.url)

        login_div = self.driver.find_element_by_class_name('eLAPa')
        self.driver.execute_script("arguments[0].click();", login_div)
        self.driver.implicitly_wait(10)
        self.login()
        time.sleep(5)

        self.driver.get(self.url)
        posts_div = self.driver.find_elements_by_class_name('eLAPa')  # getting a post

        for post_div in posts_div:
            self.driver.execute_script("arguments[0].click();", post_div)

            opened_post = self.driver.find_element_by_class_name('PdwC2')
            post_text_block = opened_post.find_element_by_class_name('C4VMK')
            post_text = post_text_block.find_elements_by_tag_name('span')[1]
            print(post_text.text)
            break


page_parse = InstagramPageParser(url='https://www.instagram.com/instagram/')
page_parse()