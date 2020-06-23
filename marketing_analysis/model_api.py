from flask import Flask, request
from flask_restful import Resource, Api
from instagram.instagram_parser import InstagramPageParser
from datetime import datetime
from pandas import DataFrame
from encoders.pandas_to_numbers_encoder import DatasetManager
from model.completed_model import EnsembledModelPredictor
from vk.parsers import VK

app = Flask(__name__)
api = Api(app)

# There's a section for uploading the external modules
vk_parser = VK
predictive_model = EnsembledModelPredictor()

class UserDealer(Resource):
    def __init__(self):
        self.url = None
        self.data_encoder = DatasetManager()
        self.parser = InstagramPageParser
        self.model = predictive_model

    def post(self):
        ''' The post data must contain the user profile url with name "url", his new post-text with a name "text" and link
        to his image with name "image" '''
        user_info = request.get_json()
        self.url = user_info['url']

        # Getting the data including new post
        data = self.parse_previous_posts()
        new_text, new_image = user_info['text'], user_info['image']
        # Making up the data, so it's ready to create a prediction
        data = self.make_up_data_for_the_prediction(text=new_text, image=new_image, previous_data=data)
        # Encoding the data
        data = self.convert_data_to_tensors(data)
        # Passing it into the model to get prediction
        data = self.feed_into_model(data)
        data = data.data.tolist()[0]

        return {'likes': data}

    @staticmethod
    def make_up_data_for_the_prediction(text, image, previous_data, date=datetime.now()):
        ''' Function makes up the data and makes it to be appropriate for the predicting '''
        new_post_data = {
            'text': text,
            'image_urls': image,
            'subscribed': previous_data[0]['subscribed'],
            'subscribers': previous_data[0]['subscribers'],
            'date': date.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
            'likes': 0,
            'account_description': previous_data[0]['account_description'],
            'total_posts': previous_data[0]['total_posts']
        }

        previous_data.append(new_post_data)

        return previous_data

    def parse_previous_posts(self, num=4):
        self.parser = self.parser(url=self.url)
        self.parser(max_posts=num)
        return self.parser.data

    def convert_data_to_tensors(self, array_of_data):
        df = DataFrame(data=array_of_data)
        return self.data_encoder(df)

    def feed_into_model(self, data):
        return self.model(data)




api.add_resource(UserDealer, '/')