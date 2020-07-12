from instagram.instagram_parser import InstagramPageParser
from instagram.instagram_user_hashtag_parser import HashtagUserParser
import pandas as pd

tags = (
    'https://www.instagram.com/explore/tags/love/',
    'https://www.instagram.com/explore/tags/picoftheday/',
    'https://www.instagram.com/explore/tags/happy/',
    'https://www.instagram.com/explore/tags/life/',
    'https://www.instagram.com/explore/tags/motivation/',
    'https://www.instagram.com/explore/tags/lifestyle/',
    'https://www.instagram.com/explore/tags/gym/',
    'https://www.instagram.com/explore/tags/crossfit/',
    'https://www.instagram.com/explore/tags/personaltrainer/',
    'https://www.instagram.com/explore/tags/personaltrainingstudio/',
    'https://www.instagram.com/explore/tags/strengthcoach/',
    'https://www.instagram.com/explore/tags/buisness/',
    'https://www.instagram.com/explore/tags/entrepreneurism/',
    'https://www.instagram.com/explore/tags/entrepreneuress/',
    'https://www.instagram.com/explore/tags/businessmindset/',
    'https://www.instagram.com/explore/tags/millionairmindset/',
    'https://www.instagram.com/explore/tags/successinlife/',
    'https://www.instagram.com/explore/tags/coding/',
    'https://www.instagram.com/explore/tags/developerlife/',
    'https://www.instagram.com/explore/tags/github/',
    'https://www.instagram.com/explore/tags/fullstack/',
    'https://www.instagram.com/explore/tags/html/',
    'https://www.instagram.com/explore/tags/reactjs/',
    'https://www.instagram.com/explore/tags/history/',
    'https://www.instagram.com/explore/tags/medievalhistory/',
    'https://www.instagram.com/explore/tags/15thcentury/',
    'https://www.instagram.com/explore/tags/middleages/',
    'https://www.instagram.com/explore/tags/coatofarms/',
    'https://www.instagram.com/explore/tags/apple/',
    'https://www.instagram.com/explore/tags/nokia/',
    'https://www.instagram.com/explore/tags/miami/',
    'https://www.instagram.com/explore/tags/miamiliving/',
    'https://www.instagram.com/explore/tags/usa/',
    'https://www.instagram.com/explore/tags/4ofjuly/',
    'https://www.instagram.com/explore/tags/trump/',
    'https://www.instagram.com/explore/tags/homedecor/',
    'https://www.instagram.com/explore/tags/homedecorideas/',
    'https://www.instagram.com/explore/tags/livingroomdecor/',
    'https://www.instagram.com/explore/tags/homedecor/',
    'https://www.instagram.com/explore/tags/walldecor/',
    'https://www.instagram.com/explore/tags/chinatown/',
    'https://www.instagram.com/explore/tags/guangzhou/',
    'https://www.instagram.com/explore/tags/virus/',
    'https://www.instagram.com/explore/tags/pandemic/',
    'https://www.instagram.com/explore/tags/covi̇d19/'
)

user_parser = InstagramPageParser()
hashtag = HashtagUserParser()
df = pd.read_csv('instagram/instagram.csv', sep='|')

for tag in tags:
    print('Parsing hashtag: {}'.format(tag))
    hashtag(url=tag)
    print(hashtag.data)
    for user in set(hashtag.data):
        print('Parsing user: {}'.format(user))
        try:
            result = user_parser(url=user)
        except Exception as ex:
            print('An exception occured: {}'.format(ex.args))
            continue
        df = df.append(result)
        df.to_csv('instagram/instagram.csv', sep='|')

