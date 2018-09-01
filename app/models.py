class NEWS:
    '''
    NEWS class to define NEWS Objects
    '''

    def __init__(self,id,name,description,url,country,category):
        self.id =id
        self.name = name
        self.description = description
        self.url = url
        self.country = country
        self.category = category

class ARTICLES:
    '''
    NEWS class to define NEWS Objects
    '''

    def __init__(self,id,publishedAt,title,author,description,Url,urlToImage):
        self.id = id
        self.publishedAt = publishedAt
        self.title = title
        self.author = author
        self.description = description
        self.Url = Url
        self.urlToImage = urlToImage 
                 