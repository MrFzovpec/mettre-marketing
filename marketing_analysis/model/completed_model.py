from model.submodels import *
from torch import nn


class EnsembledModelPredictor(nn.Module):
    def __init__(self):
        super().__init__()
        self.text = DistilBERTAnalysis()
        self.images = InceptionV3Analysis()
        self.meta = MetaLinearAnalyzator()
        self.all_to_one = AllToOneContext()
        self.likes = nn.Linear(1, 512)
        self.lstmer = LSTMPredictor()
        self.predictor = nn.Linear(512, 1)

    def forward(self, x):
        ''' Needs to rethink the architecture of the model '''

        # Getting information about text
        text, acc_description = x['text'][0], x['account_description'][0]
        text, acc_description = text[:, :512], acc_description[:, :512]
        text_context, acc_description_context = self.text(text), self.text(acc_description)

        # Getting the information about images
        image = x['image'][0]
        image_context = self.images(image)

        # Getting the information about the account meta data
        total_posts, subscribers = x['total_posts'][0], x['subscribers'][0]
        date, subscribed = x['date'][0], x['subscribed'][0]
        meta_data_tensor = torch.cat([total_posts, subscribers, date, subscribed], dim=1)
        meta_context = self.meta(meta_data_tensor)

        # Getting the information about all the posts and likes
        context_vector = torch.cat([text_context, acc_description_context,
                                    image_context, meta_context], dim=1)
        context_vector = self.all_to_one(context_vector)
        likes_vector = self.likes(x['likes'][0])

        # Getting LSTM context and final prediction
        context_result = self.lstmer(context_vector, likes_vector)
        prediction = self.predictor(context_result)

        return prediction
