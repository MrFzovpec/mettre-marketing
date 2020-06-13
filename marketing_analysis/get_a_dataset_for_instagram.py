from instagram_parser import InstagramPageParser
from instagram_user_hashtag_parser import HashtagUserParser
import pandas as pd

tags = (
    'https://www.instagram.com/explore/tags/программирование/',
    'https://www.instagram.com/explore/tags/работавдекрете/',
    'https://www.instagram.com/explore/tags/бизнесвсети/',
    'https://www.instagram.com/explore/tags/разработкасайтов/',
    'https://www.instagram.com/explore/tags/продвижениесайтов/',
    'https://www.instagram.com/explore/tags/контекстнаяреклама/',
    'https://www.instagram.com/explore/tags/блоггеры/',
    'https://www.instagram.com/explore/tags/вайнер/',
    'https://www.instagram.com/explore/tags/sketchingart/',
    'https://www.instagram.com/explore/tags/penartwork/',
    'https://www.instagram.com/explore/tags/fashion/',
    'https://www.instagram.com/explore/tags/beautiful/',
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
    'https://www.instagram.com/explore/tags/coatofarms/'
)

df = pd.read_csv('instagram.csv')

for tag in tags:
    print('Parsing hashtag: {}'.format(tag))
    hastag = HashtagUserParser(tag)
    hastag()
    print(hastag.data)
    for user in hastag.data:
        print('Parsing user: {}'.format(user))
        user_parser = InstagramPageParser(user)
        try:
            user_parser()
        except Exception as ex:
            print('An exception occured: {}'.format(ex.args))
        df = df.append(user_parser.data)
        df.to_csv('instagram.csv')

