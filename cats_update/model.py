import torch
from torch import nn


class DistilBERTClassification(nn.Module):
    def __init__(self, first: bool, dataloader, train_dataset, test_dataset):
        '''
          Initializes a model
          @param: first. If True - than its the first training and the model is going
          to use an AllenNLP dataset
        '''
        super().__init__()
        # Training configurations
        self.first = first
        self.dataloader = dataloader
        self.train_dataset = train_dataset
        self.test_dataset = test_dataset

        # Model itself
        self.transformer = DistilBertModel.from_pretrained('distilbert-base-multilingual-cased')
        self.linear = nn.Linear(3072, 3)
        self.softmax = nn.Softmax(dim=1)

    def forward(self, x):
        ''' Forward method '''
        x = self.transformer(x)
        x = x[0][:, :4, :]
        x = x.view(x.shape[0], -1)
        x = self.linear(x)
        x = self.softmax(x)
        return x


def get_the_model(filepath):
    '''
        The function returns an object of DistilBERTClassification instance
    '''
    model = DistilBERTClassification
    with open(filepath, 'rb') as f:
        model.load_state_dict(torch.load(f))
