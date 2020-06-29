import torch
from datetime import datetime

class MetaDataEncoder:

  @staticmethod
  def encode(samples):
    meta_array = [] # creating an array for keeping all the metadata
    for i, sample in samples.iteritems():
      sample = str(sample)
      meta_array.append(torch.tensor([int(sample.replace(',',''))], dtype=torch.float))

    return torch.stack(meta_array)


class DateEncoder:
  @staticmethod
  def encode(samples):
    date_array = []

    for i, sample in samples.iteritems():
      date = datetime.strptime(sample, '%Y-%m-%dT%H:%M:%S.%fZ')
      date = date.timestamp()
      date_array.append(torch.tensor([date], dtype=torch.float))

    return torch.stack(date_array)