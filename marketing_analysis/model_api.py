from flask import Flask, request
from flask_restful import Resource, Api
from instagram.instagram_parser import InstagramPageParser

app = Flask(__name__)
api = Api(app)

class UserDealer(Resource):
    def __init__(self):
        self.url = None
        self.parser = InstagramPageParser

    def post(self):
        ''' The post data must contain the user profile url with name "url", his new post-text with a name "text" and link
        to his image with name "image" '''
        user_info = request.get_json()
        self.url = user_info['url']
        data = self.parse_previous_posts()
        return {'Data': data}

    def parse_previous_posts(self, num=4):
        self.parser = self.parser(self.url)
        self.parser(max_posts=num)
        return self.parser.data



api.add_resource(UserDealer, '/')