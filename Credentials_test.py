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
        self.assertEqual(self.new_Credentials.Username,"")
        self.assertEqual(self.new_Credentials.Password,"")


    def test_save_Credentials(self):
        '''
        test_save_Credentials test case to test if the Credentials object is saved into
         the Credentials list
        '''
        self.new_Credentials.save_Credentials() # saving the new Credentials
        self.assertEqual(len(Credentials.Credentials_list),1)

if __name__ == '__main__':
    unittest.main()