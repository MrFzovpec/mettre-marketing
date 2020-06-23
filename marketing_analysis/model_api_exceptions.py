class NotValidSocialNetworkIndex(Exception):
    def __init__(self, index):
        self.message = 'The index {} is not valid.' \
                       'Possible indexes - 0 (for Instagram) and 1 (for VK)'.format(index)
        super().__init__(self.message)