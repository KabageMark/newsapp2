from ..request import get_source
from ..request import get_articles
from flask import render_template,request,redirect,url_for
from . import main
                  
@main.route('/sources')
def sources():

    '''
    View root page function that returns the index page and its data
    '''
    
    source_news_general = get_source('general')
    source_news_sports = get_source('sports')
    source_news_technology = get_source('technology')
    source_news_business = get_source('business')
    source_news_url = get_source('Url')
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('sources.html', title = title,general = source_news_general,Url = source_news_url,sports = source_news_sports,technology = source_news_technology,business = source_news_business)

@main.route('/sources/articles/<id>')
def articles(id):
    articles_args = get_articles(id)
    return render_template('articles.html',articles = articles_args) 