# mettre-marketing

## Main task

Marketing analysis

## About new categories

The categories are parsed from the <a href = 'https://trends.google.ru/trends/trendingsearches/daily?geo=RU'>Google Trends</a> page. The queries with 500 000+ searches are getting to our model training and the labels

<b>cats_update/trends_google.py</b> - the file contains the GoogleTrends parse, availiable to set it up for different instance. On call 
starts to parse google trends page.<br>
P.S right now it doesn't work, because the google page doesn't refresh after the button clicking <br>

<b>cats_update/model.py</b> - the file contains a class of the model <i>DistilBERTClassification</i> and the function <i>get_the_model</i> which uploads the model with its trained weights

## About marketing analysis

<b>marketing_analysis/instagram/</b> - the directory with an Instagram analysis<br>

<b>markeing_analysis/instagram/instagram_parser.py</b> - the file contains a class of an Instagram Page parser, which on call parses a particular page. In order to get it work you need to make a copy of secret.txt, change its format to .py and write down your login and password<br>

<b>marketing_analysis/instagram/instagram_user_hashtag_parser.py</b> - the file contains a class of the Instagram parser by hashtag. On call parses the hashtag page and gives users list (for data collection)

## About Flask API for the Marketing Analysis

The API works with a <b>POST</b> requests in the format: <br>
{
    'url': user account urls (from this url the users data would be parsed (in the future we would somehow avoid this step or parse the data more efficiently as far as parsing takes way to much time (already have some thought about it)),
    'text': the text user wrote for their post,
    'image': link to the image user want to post for his post,
    'social': social network user want to post their post (instagram for Instagram, vk for VK, facebook for Facebook)
}