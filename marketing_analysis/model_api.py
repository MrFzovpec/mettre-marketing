from flask import Flask, request
from flask_restful import Resource, Api
from instagram.instagram_parser import InstagramPageParser
from datetime import datetime
from pandas import DataFrame
from encoders.pandas_to_numbers_encoder import DatasetManager
from model.completed_model import EnsembledModelPredictor
from vk.parsers import VK
from model_api_exceptions import NotValidSocialNetworkIndex

app = Flask(__name__)
api = Api(app)

# There's a section for uploading the external modules
VK_PARSER = VK()
PREDICTIVE_MODEL = EnsembledModelPredictor()
INSTAGRAM_PARSER = InstagramPageParser

class UserDealer(Resource):
    def __init__(self):
        self.url = None
        self.data_encoder = DatasetManager()
        self.instagram_parser = INSTAGRAM_PARSER

    def post(self):
        ''' The post data must contain the user profile url with name "url", his new post-text with a name "text" and link
        to his image with name "image" '''
        user_info = request.get_json()
        self.url = user_info['url']

        # Getting the data including new post
        data = self.check_the_social_network_and_treat_accordingly(user_info['social'])
        new_text, new_image = user_info['text'], user_info['image']
        # Making up the data, so it's ready to create a prediction
        data = self.make_up_data_for_the_prediction(text=new_text, image=new_image, previous_data=data)
        # Encoding the data
        data = self.convert_data_to_tensors(data)
        # Passing it into the model to get prediction
        data = self.feed_into_model(data)
        data = data.data.tolist()[0]

        return {'likes': data}

    def check_the_social_network_and_treat_accordingly(self, social_number):
        ''' This function parses the data from the users social network accordingly '''
        if social_number == 0: # For the Instagram
            data = self.parse_previous_posts_from_instagram()
        elif social_number == 1: # For the VK
            data = VK_PARSER.get_all_posts(self.url)
        else:
            raise NotValidSocialNetworkIndex(social_number)

        return data


    def parse_previous_posts_from_instagram(self, num=4):
        self.instagram_parser = self.instagram_parser(url=self.url)
        self.instagram_parser(max_posts=num)
        return self.instagram_parser.data

    def convert_data_to_tensors(self, array_of_data):
        df = DataFrame(data=array_of_data)
        return self.data_encoder(df)

    def feed_into_model(self, data):
        return PREDICTIVE_MODEL(data)

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




api.add_resource(UserDealer, '/')