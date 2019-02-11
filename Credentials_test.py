import unittest # Importing the unittest module
from Credentials import Credentials # Importing the contact class

class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the Credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''


    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_Credentials = Credentials("","","") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_Credentials.site,"")
        self.assertEqual(self.new_Credentials.username,"")
        self.assertEqual(self.new_Credentials.password,"")


    def test_save_Credentials(self):
        '''
        test_save_Credentials test case to test if the Credentials object is saved into
         the Credentials list
        '''
        self.new_Credentials.save_Credentials() # saving the new Credentials
        self.assertEqual(len(Credentials.Credentials_list),1)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.Credentials_list = []


    def test_save_multiple_Credentials(self):
        '''
        test_save_multiple_Credentials to check if we can save multiple Credentials
        objects to our Credentials_list
        '''
        self.new_Credentials.save_Credentials()
        test_Credentials = Credentials("","","") # new contact
        test_Credentials.save_Credentials()
        self.assertEqual(len(Credentials.Credentials_list),2)


    
    def test_delete_Credentials(self):
            '''
            test_delete_Credentials to test if we can remove a credentials from our credential list
            '''
            self.new_Credentials.save_Credentials()
            test_Credentials = Credentials("","","") 
            test_Credentials.save_Credentials()

            self.new_Credentials.delete_Credentials()
            self.assertEqual(len(Credentials.Credentials_list),1)


    def test_find_Credentials_by_site(self):
        '''
        test to check if we can find a Credentials
        '''

        self.new_Credentials.save_Credentials()
        test_Credentials = Credentials("","","") 
        test_Credentials.save_Credentials()

        found_Credentials = Credentials.find_by_site("")

        self.assertEqual(found_Credentials.site,test_Credentials.site)

    def test_Credentials_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''

        self.new_Credentials.save_Credentials()
        test_Credentials = Credentials("","","")
        test_Credentials.save_Credentials()

        Credentials_exists = Credentials.Credentials_exist("")

        self.assertTrue(Credentials_exists)

if __name__ == '__main__':
    unittest.main()