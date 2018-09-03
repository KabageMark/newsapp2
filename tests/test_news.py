import unittest
from app.models import NEWS,ARTICLES
class testNews(unittest.TestCase):
    def setUp(self):
            '''
            Set up method to run before each test cases.
            '''
            self.new_news = NEWS(1,"BBC","Michael Cohen prosecuted","https://www.nytimes.com/by/ernesto-londono","us","general") 


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_news.id,1)
        self.assertEqual(self.new_news.name,"BBC")
        self.assertEqual(self.new_news.description,"Michael Cohen prosecuted")
        self.assertEqual(self.new_news.url,"https://www.nytimes.com/by/ernesto-londono")
        self.assertEqual(self.new_news.country,"us")

class testArticles(unittest.TestCase):
    def setUp(self):
            '''
            Set up method to run before each test cases.
            '''
            self.new_articles = ARTICLES(1,"2018-09-02T16:20:37Z","Fire Engulfs a Brazilian Museum,Threatening Hundreds of Years of History","https://www.nytimes.com/by/ernesto-londono","Michael Cohen prosecuted","http://www.aljazeera.com","https://static01.nyt.com/images/2018/09/03/world/03xp-brazil/03xp-brazil-facebookJumbo.jpg") 


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_articles.id,1)
        self.assertEqual(self.new_articles.publishedAt,"2018-09-02T16:20:37Z")
        self.assertEqual(self.new_articles.title,"Fire Engulfs a Brazilian Museum,Threatening Hundreds of Years of History")
        self.assertEqual(self.new_articles.author,"https://www.nytimes.com/by/ernesto-londono")
        self.assertEqual(self.new_articles.description,"Michael Cohen prosecuted")
        self.assertEqual(self.new_articles.Url,"https://www.nytimes.com/by/ernesto-londono")
        self.assertEqual(self.new_articles.urlToImage,"https://static01.nyt.com/images/2018/09/03/world/03xp-brazil/03xp-brazil-facebookJumbo.jpg")

    # def test_save_Account(self):
    #     '''
    #     test_save_contact test case to test if the contact object is saved into
    #     the contact list
    #     '''
    #     self.new_account.saveaccount() # saving the new contact
    #     self.assertEqual(len(Account.account_list),1)

    # def tearDown(self):
    #     '''
    #     tearDown method that does clean up after each test case has run.
    #     '''
    #     Account.account_list = []    
    
    # def test_save_multiple_Account(self):
    #     '''
    #     test_save_contact test case to test if the contact object is saved into
    #     the contact list
    #     '''
    #     self.new_account.saveaccount() 
    #     test_account = Account("Test","user","test@user.com") 
    #     test_account.saveaccount()
    #     self.assertEqual(len(Account.account_list),2)

# if __name__ == '__main__':
#     unittest.main() 