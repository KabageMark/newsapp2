import os

class Config:

    SOURCE_API_BASE_URL ='https://newsapi.org/v2/sources?category={}&apiKey={}'
    ARTICLE_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?q=business&apiKey=c0ccbdb1740d4e6990dc52150c79dfd6'
    NEWS_API_KEY = os.environ.get('c0ccbdb1740d4e6990dc52150c79dfd6')
    SECRET_KEY = os.environ.get('KabageMark')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}