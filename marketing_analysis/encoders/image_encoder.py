import requests
from PIL import Image
from io import BytesIO
from torchvision import transforms
import torch
import torch.nn.functional as F

class ImageEncoder():
    def __init__(self, size_index=2, transform=transforms.ToTensor()):
        self.size_index = size_index
        self.transform = transform

    def encode(self, samples):
        image_array = []  # creating an array for keeping all the images
        for i, sample in samples.iteritems():
            # Getting a clear link of an image
            if ',' in sample:
                link_href = sample.split(',')[self.size_index][:-5]
            else:
                link_href = sample
            image = self.get_img_from_remote_server(link_href)
            image = self.transform(image)

            # Downsampling the images with size other than 320
            image = F.interpolate(image, 320)
            image = image.permute(0, 2, 1)
            image = F.interpolate(image, 320)
            image = image.permute(0, 2, 1)

            image_array.append(image)

        return torch.stack(image_array)

    @staticmethod
    def get_img_from_remote_server(url):
        ''' Function gets an image from a remote server '''
        response = requests.get(url)
        return Image.open(BytesIO(response.content))