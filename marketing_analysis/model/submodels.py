from torch import nn
from transformers import DistilBertModel
import torchvision.models as models
import torch.nn.functional as F
import torch


class DistilBERTAnalysis(nn.Module):
  def __init__(self):
    super().__init__()
    self.transformer = DistilBertModel.from_pretrained('distilbert-base-multilingual-cased')
    self.linear = nn.Linear(3072, 64)

  def forward(self, x):
    x = self.transformer(x)
    x = x[0][:, :4, :]
    x = x.view(x.shape[0], -1)
    x = self.linear(x)

    return x


class InceptionV3Analysis(nn.Module):
  def __init__(self):
    super().__init__()
    self.imager = models.vgg19_bn(pretrained=False)
    self.imager.classifier = nn.Linear(25088, 64)

  def forward(self, x):
    return self.imager(x)


class MetaLinearAnalyzator(nn.Module):
  def __init__(self):
    super().__init__()
    self.linear1 = nn.Linear(4, 32)
    self.linear2 = nn.Linear(32, 64)

  def forward(self, x):
    x = self.linear1(x)
    x = F.leaky_relu(x)
    x = self.linear2(x)
    x = F.leaky_relu(x)

    return x


class AllToOneContext(nn.Module):
  def __init__(self):
    super().__init__()
    self.linear1 = nn.Linear(256, 512)

  def forward(self, x):
    x = self.linear1(x)

    return x


class LSTMPredictor(nn.Module):
  def __init__(self, memory_depth=512):
    super().__init__()
    self.memory_depth = memory_depth
    self.lstm_cell = nn.LSTMCell(512, self.memory_depth)

  def forward(self, x, likes_context):

    # This one gets a first memory cell vector
    c_0 = self.get_first_cell_state(1)
    h_0 = self.get_first_cell_state(1)

    for i, vector in enumerate(x):
      vector = torch.reshape(vector, (1, 512))
      h_0, c_0 = self.lstm_cell(vector, (h_0, c_0))

      # Checks if it's the last tensor => no likes plusage
      if len(x) - 1 == i:
        break

      h_0 += likes_context[i]

    return h_0

  def get_first_cell_state(self, samples_countable):
    return torch.zeros((samples_countable, self.memory_depth))