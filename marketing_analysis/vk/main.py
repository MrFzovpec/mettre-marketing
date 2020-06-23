from parsers import VK
import json
vk = VK()

#vk.get_page_bio('https://vk.com/brandshop_ru')

print(vk.get_all_posts('https://vk.com/brandshop_ru', max_posts_in_hundreds=1))