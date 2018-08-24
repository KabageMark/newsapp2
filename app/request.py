from app import app
import urllib.request,json
from .models import NEWS,ARTICLES
News = NEWS
Articles =ARTICLES

# Getting api key
api_key = app.config['NEWS_API_KEY']
api_key2 = app.config['NEWS_API_KEY']
base_url = app.config["SOURCE_API_BASE_URL"]
base_url2 = app.config['ARTICLE_API_BASE_URL']

def get_source(category):
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_url.format( category, api_key)
    print(get_source_url)
    with urllib.request.urlopen(get_source_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        source_results = None

        if get_news_response['sources']:
            source_results_list = get_news_response['sources']
            source_results = process_source(source_results_list)
    return source_results