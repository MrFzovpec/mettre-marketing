from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import InvalidArgumentException


class InstagramPageParser():
    def __init__(self, url: str, driver=webdriver.Chrome):
        options = Options()
        self.driver = driver(ChromeDriverManager().install(), chrome_options=options)
        self.url = url

    def __call__(self):
        self.driver.get(self.url)
        posts_div = self.driver.find_elements_by_class_name('_bz0w')  # getting a post
        for post_div in posts_div:
            post_div.click()  # opening it
            opened_post = self.driver.find_element_by_class_name('PdwC2')
            post_text_block = opened_post.find_elements_by_class_name('C4VMK')
            post_text = post_text_block.find_element_by_tag_name('span')
            print(post_text)
            break


page_parse = InstagramPageParser(url='https://www.instagram.com/instagram/')
page_parse()