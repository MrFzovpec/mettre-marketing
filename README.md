# mettre-marketing

## About new categories

The categories are parsed from the <a href = 'https://trends.google.ru/trends/trendingsearches/daily?geo=RU'>Google Trends</a> page. The queries with 500 000+ searches are getting to our model training and the labels

<b>cats_update/trends_google.py</b> - the file contains the GoogleTrends parse, availiable to set it up for different instance. On call 
starts to parse google trends page.
P.S right now it doesn't work, because the google page doesn't refresh after the button clicking
