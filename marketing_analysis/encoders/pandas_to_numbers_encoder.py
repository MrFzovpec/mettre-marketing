from encoders.image_encoder import ImageEncoder
from encoders.text_encoder import TextEncoder
from encoders.numeric_encoder import DateEncoder, MetaDataEncoder
import random

class DatasetManager():
  def __init__(self, df, text_encoder=TextEncoder(),
               image_encoder=ImageEncoder(), meta_data_encoder=MetaDataEncoder(),
               date_encoder=DateEncoder()):
    self.df = df

    # Encoders for different data
    self.text_encoder, self.account_description_encoder = text_encoder, text_encoder
    self.image_encoder = image_encoder
    self.date_encoder = date_encoder
    self.likes_encoder, self.comments_encoder = meta_data_encoder, meta_data_encoder
    self.total_posts_encoder, self.subscribers_encoder = meta_data_encoder, meta_data_encoder
    self.subscribed_encoder = meta_data_encoder

  def __getitem__(self, index):
    sample_data = self.data[index]

    return {
        'total_posts': self.total_posts_encoder.encode(sample_data['total_posts']),
        'text': self.text_encoder.encode(sample_data['text']),
        'likes': self.likes_encoder.encode(sample_data['likes']),
        'date': self.date_encoder.encode(sample_data['date']),
        'image': self.image_encoder.encode(sample_data['image_urls']),
        'subscribers': self.subscribers_encoder.encode(sample_data['subscribers']),
        'subscribed': self.subscribed_encoder.encode(sample_data['subscribed']),
        'account_description': self.account_description_encoder.encode(sample_data['account_description']),
    }

  def __len__(self):
    return len(self.data)