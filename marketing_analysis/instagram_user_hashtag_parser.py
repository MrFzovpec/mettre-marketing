import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import InvalidArgumentException
from secret import get_username, get_password
import time
from instagram_interaction import InstagramInteraction


class HashtagUserParser(InstagramInteraction):
    def __init__(self, url):
        super().__init__(url)

    def login(self, login=get_username(), password=get_password()):
        super().login()

    def __call__(self, max_posts=None):
        self.driver.get(self.url)
        try:
            self.simple_post_login_initializer()
        except selenium.common.exceptions.NoSuchElementException:
            pass

        # Getting data about posts
        if max_posts:
            posts_div = self.driver.find_elements_by_class_name('eLAPa')[:max_posts]
        else:
            posts_div = self.driver.find_elements_by_class_name('eLAPa')

        # Starting a loop in order to scrap info from posts
        for post_div in posts_div:
            self.driver.execute_script("arguments[0].click();", post_div)
            time.sleep(3)

            try:
                link_to_the_profile = self.driver.find_element_by_css_selector('div.e1e1d > a.sqdOP')
                self.data.append(link_to_the_profile.get_attribute('href'))
            except selenium.common.exceptions.NoSuchElementException:
                pass

            # closing the post
            close_btn = self.driver.find_element_by_class_name('wpO6b')
            self.driver.execute_script("arguments[0].click();", close_btn)

    def simple_post_login_initializer(self):
        super().simple_post_login_initializer()
