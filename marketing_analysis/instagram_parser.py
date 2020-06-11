import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import InvalidArgumentException
from secret import get_username, get_password
import time


class InstagramPageParser():
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

    def __call__(self, max_posts=None):
        self.driver.get(self.url)

        # Login into Instagram in order to parse the page
        login_div = self.driver.find_element_by_class_name('eLAPa')
        self.driver.execute_script("arguments[0].click();", login_div)
        self.driver.implicitly_wait(10)
        self.login()
        time.sleep(5)

        # Relocating back to the searchable page
        self.driver.get(self.url)

        # Getting metadata about account
        posts_countable = self.driver.find_element_by_css_selector('ul.k9GMp > li.Y8-fY > span.-nal3 > span.g47SY')
        subscribers = self.driver.find_elements_by_css_selector('ul.k9GMp > li.Y8-fY > a.-nal3 > span.g47SY')[0]
        subscribed = self.driver.find_elements_by_css_selector('ul.k9GMp > li.Y8-fY > a.-nal3 > span.g47SY')[1]

        # Getting data about posts
        if max_posts:
            posts_div = self.driver.find_elements_by_class_name('eLAPa')[:max_posts]
        else:
            posts_div = self.driver.find_elements_by_class_name('eLAPa')

        # Starting a loop in order to scrap info from posts
        for post_div in posts_div:
            # Getting images urls
            image_urls = post_div.find_element_by_css_selector('.KL4Bh > img')

            # Getting countable of comments

            # opening the post and getting the essential info out of it
            self.driver.execute_script("arguments[0].click();", post_div)

            # collecting data
            opened_post = self.driver.find_element_by_class_name('PdwC2')
            post_text = self._get_the_text(opened_post)
            try:
                likes_per_post = self._get_likes_countable(opened_post)
            except selenium.common.exceptions.NoSuchElementException:
                continue

            date_per_post = self._get_datetime(opened_post)

            # closing the post
            close_btn = self.driver.find_element_by_class_name('wpO6b')
            self.driver.execute_script("arguments[0].click();", close_btn)

            # saving a data as a dictionary
            post = {
                'total_posts': posts_countable.text,
                'text': post_text.text,
                'likes': likes_per_post.text,
                'date': date_per_post.get_attribute('datetime'),
                'subscribers': subscribers.get_attribute('title'),
                'subscribed': subscribed.text,
                'image_urls': image_urls.get_attribute('srcset'),
            }
            self.data.append(post)

    @staticmethod
    def _get_the_text(post):
        ''' The function gets the text from the !OPENED! post'''
        post_text_block = post.find_element_by_class_name('C4VMK')
        post_text = post_text_block.find_elements_by_tag_name('span')[1]

        return post_text

    @staticmethod
    def _get_likes_countable(post):
        likes_block = post.find_element_by_css_selector('section.EDfFK.ygqzn > div > div.Nm9Fw > button > span')
        return likes_block

    @staticmethod
    def _get_datetime(post):
        time_block = post.find_element_by_css_selector('div.eo2As > div.k_Q0X.NnvRN > a > time')
        return time_block


page_parse = InstagramPageParser(url='https://www.instagram.com/instagram/')
page_parse(max_posts=5)
print(page_parse.data)
