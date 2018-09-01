from .import main
import urllib.request,json
from .models import NEWS,ARTICLES
News = NEWS
Articles = ARTICLES

def configure_request(app):
    # Getting api key
    global api_key,base_url,base_url2
    api_key = app.config['NEWS_API_KEY']
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

def process_source(source_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

        Args:
    news_list: A list of dictionaries that contain movie details

        Returns :
    news_results: A list of news objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        Url = source_item.get('Url')
        description = source_item.get('description')
        country = source_item.get('country')
        category = source_item.get('category')

        source_object = News(id,name,country,description,Url,category)
        source_results.append(source_object)
    return source_results

def get_articles(id):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = base_url2.format( id, api_key)
    print(get_articles_url)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)
    return articles_results


def process_articles(articles_list):
        '''
        Function  that processes the news result and transform them to a list of Objects

            Args:
        news_list: A list of dictionaries that contain movie details

            Returns :
        news_results: A list of news objects
        '''
        articles_results = []
        for article_item in articles_list:
            id = article_item.get('id')
            author = article_item.get('author')
            description = article_item.get('description')
            url = article_item.get('url')
            urlToImage = article_item.get('urlToImage')
            publsihedAt = article_item.get('publishedAt')
            title = article_item.get('title')

            article_object = Articles(id,title,author,urlToImage,description,url,publsihedAt)
            articles_results.append(article_object)

        return articles_results    