class Environment:
    URL = 'https://fintender.ru/'

    def __init__(self):
        self.env = 'PROD'

    def get_base_url(self):
        return self.URL

host = Environment()