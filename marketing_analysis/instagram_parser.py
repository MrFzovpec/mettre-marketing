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
        self.data = []

    def login(self, login='', password=''):
        ''' Logining function '''
        u_input = self.driver.find_element_by_css_selector('input[name="username"]')
        u_input.send_keys(login)
        p_input = self.driver.find_element_by_css_selector('input[name="password"]')
        p_input.send_keys(password)

        login_btn = self.driver.find_element_by_css_selector(".DhRcB")
        login_btn.click()

    def __call__(self):
        self.driver.get(self.url)

        # Login into Instagram in order to parse the page
        login_div = self.driver.find_element_by_class_name('eLAPa')
        self.driver.execute_script("arguments[0].click();", login_div)
        self.driver.implicitly_wait(10)
        self.login()
        time.sleep(5)

        self.driver.get(self.url)
        posts_div = self.driver.find_elements_by_class_name('eLAPa')  # getting a post

        for post_div in posts_div:
            # opening the post and getting the essential info out of it
            self.driver.execute_script("arguments[0].click();", post_div)

            # collecting data
            opened_post = self.driver.find_element_by_class_name('PdwC2')
            post_text = self.get_the_text(opened_post)
            likes_per_post = self.get_likes_countable(opened_post)
            date_per_post = self.get_datetime(opened_post)
            print(date_per_post.get_attribute('datetime'))

            # closing the post
            close_btn = self.driver.find_element_by_class_name('wpO6b')
            self.driver.execute_script("arguments[0].click();", close_btn)

            # saving a data as a dictionary
            post = {
                'text': post_text.text,
                'likes': likes_per_post.text,
                'date': date_per_post.get_attribute('datetime'),
            }
            self.data.append(post)

    @staticmethod
    def get_the_text(post):
        ''' The function gets the text from the !OPENED! post'''
        post_text_block = post.find_element_by_class_name('C4VMK')
        post_text = post_text_block.find_elements_by_tag_name('span')[1]

        return post_text

    @staticmethod
    def get_likes_countable(post):
        likes_block = post.find_element_by_css_selector('section.EDfFK.ygqzn > div > div.Nm9Fw > button > span')
        return likes_block

    @staticmethod
    def get_datetime(post):
        time_block = post.find_element_by_css_selector('div.eo2As > div.k_Q0X.NnvRN > a > time')
        return time_block


page_parse = InstagramPageParser(url='https://www.instagram.com/instagram/')
page_parse()