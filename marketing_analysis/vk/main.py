from parsers import VK
import json
login, password, = input("Логин: "), input("Пароль: ")
vk = VK(login, password)

vk.get_page_bio('https://vk.com/brandshop_ru')

# file = open('vk_posts_parsed.json', 'w')
# file.write(json.dumps(vk.get_all_posts('https://vk.com/brandshop_ru')))
# file.close()