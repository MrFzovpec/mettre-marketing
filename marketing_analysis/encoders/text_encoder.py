import torch
from transformers import DistilBertTokenizer
import torch.nn.functional as F


class TextEncoder:
    def __init__(self, tokenizer=DistilBertTokenizer.from_pretrained('distilbert-base-multilingual-cased')):
        self.tokenizer = tokenizer

    def encode(self, samples):
        text_array = []  # creating a text array for keeping all the texts
        for i, sample in samples.iteritems():
            text_tensor = torch.tensor(self.tokenizer.encode(sample))
            text_array.append(text_tensor)

        return self.pad_and_stack(text_array)

    @staticmethod
    def get_largest_elem(array, dim=0):
        ''' The function identyfies the largest tensor over particular dimension '''
        max_len = 0
        for elem in array:
            # Runs over thought the array to identify the largest one
            if elem.shape[dim] > max_len:
                max_len = elem.shape[dim]

        return max_len

    def pad_and_stack(self, array, dim=0):
        ''' Function pads and stacks array over a new axis '''

        if dim == 0:
            largest = self.get_largest_elem(array)  # gets the largest to pad
            array_for_stack = []
            for elem in array:
                # Pad the elements to get equal shapes
                elem = F.pad(elem, [0, largest - elem.shape[dim]])
                array_for_stack.append(elem)

        return torch.stack(array_for_stack)
