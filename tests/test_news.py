import unittest
from app.models import NEWS,ARTICLES
class testNews(unittest.TestCase):
    def setUp(self):
            '''
            Set up method to run before each test cases.
            '''
            self.new_news = NEWS(1,"BBC","Michael Cohen prosecuted","http://www.aljazeera.com","us") 


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_news.id,1)
        self.assertEqual(self.new_news.name,"BBC")
        self.assertEqual(self.new_news.description,"Michael Cohen prosecuted")
        self.assertEqual(self.new_news.url,"http://www.aljazeera.com")
        self.assertEqual(self.new_news.country,"us")


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