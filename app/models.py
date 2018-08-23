class NEWS:
    '''
    NEWS class to define NEWS Objects
    '''

    def __init__(self,id,name,description,url,country):
        self.id =id
        self.name = name
        self.description = description
        self.url = url
        self.country = country

class ARTICLES:
    '''
    NEWS class to define NEWS Objects
    '''

    def __init__(self,id,author,description,Url,urlToImage,publishedAt):
        self.id =id
        self.author = author
        self.description = description
        self.Url = Url
        self.urlToImage = urlToImage 
        self.publishedAt = publishedAt         