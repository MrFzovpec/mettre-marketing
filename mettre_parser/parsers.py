import vk_api
import requests


class VK:
    def __init__(self, login, password):
        self.vk_session = vk_api.VkApi(login, password)
        self.vk_session.auth()
        self.vk = self.vk_session.get_api()

    def preprocess(self, url):
        url = url.replace('https://vk.com/', '')
        if '/' in url:
            url = url.replace('/')
        page_info = self.vk.utils.resolveScreenName(screen_name=url)
        if page_info['type'] == "group":
            return page_info['object_id'] * (-1)
        else:
            return page_info['object_id']

    def get_last_post(self, url):
        # Получаем ID группы
        group_id = self.preprocess(url)

        # Получаем последнюю запись из группы
        last_post = self.vk.wall.get(owner_id=f'{group_id}')['items'][0]

        return {
            'comments': last_post["comments"]["count"],
            'likes': last_post["likes"]["count"],
            'views': last_post['views']["count"],
            'text': last_post['text'],
            'type': last_post['post_type'],
            'date': last_post["date"]
        }

    def get_all_posts(self, url):
        # Получаем ID группы
        group_id = self.preprocess(url)

        # Получаем информацию о записях в группе, кол-во всех записей
        posts_body = self.vk.wall.get(owner_id=f'{group_id}')
        posts_count = posts_body['count']

        all_posts = {}
        for offset in range(0, posts_count, 100):
            posts = self.vk.wall.get(owner_id=f'{group_id}', count=100, offset=offset)['items']
            for i, post in enumerate(posts):
                try:
                    all_posts[i + offset] = {
                        'comments': post["comments"]["count"],
                        'likes': post["likes"]["count"],
                        'views': post['views']["count"],
                        'text': post['text'],
                        'type': post['post_type'],
                        'date': post["date"]
                    }
                except KeyError:
                    break

        return all_posts

    def get_page_bio(self, url):
        group_id = self.preprocess(url)

        # Получаем описание группы и информацию о ней
        meta_info = self.vk.groups.getById(group_id=abs(group_id), fields="description,members_count,activity")[0]

        return {
            'name': meta_info['name'],
            'subs': meta_info['members_count'],
            'description': meta_info['description'],
            'category': meta_info['activity'],
            'is_closed': meta_info["is_closed"],
            'type': meta_info["type"],
        }


class Facebook:
    def test_p(self):
        return requests.get('http://graph.facebook.com/v7.0/CrocIncorporated/feed').content
