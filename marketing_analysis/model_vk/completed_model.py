from model_modules.submodels import *

class EnsembledModelPredictor(nn.Module):
    def __init__(self):
        super().__init__()
        self.text = DistilBERTAnalysis()
        self.images = InceptionV3Analysis()
        self.meta = MetaLinearAnalyzator(input_size=3)
        self.all_to_one = AllToOneContext()
        self.likes = nn.Linear(1, 512)
        self.lstmer = LSTMPredictor()
        self.predictor = nn.Linear(512, 1)

    def forward(self, x):
        # Getting information about text
        text, acc_description = x['text']
        text = text[:, :512]
        text_context = self.text(text)

        # Getting the information about images
        image = x['image']
        image_context = self.images(image)

        # Getting the information about the account meta data
        # Meta data - comments, likes, views, date
        total_posts = x['total_posts'], x['']
        total_posts, subscribers = x['total_posts'], x['subscribers']
        date, subscribed = x['date'], x['subscribed']
        meta_data_tensor = torch.cat([total_posts, subscribers, date, subscribed], dim=1)
        meta_context = self.meta(meta_data_tensor)

        # Getting the information about all the posts and likes
        context_vector = torch.cat([text_context, acc_description_context,
                                    image_context, meta_context], dim=1)
        context_vector = self.all_to_one(context_vector)
        likes_vector = self.likes(x['likes'])

        # Getting LSTM context and final prediction
        context_result = self.lstmer(context_vector, likes_vector)
        prediction = self.predictor(context_result)

        return prediction