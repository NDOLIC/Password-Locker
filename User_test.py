import unittest # Importing the unittest module
from User import User # Importing the User class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the User class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_User = User("","","","") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_User.first_name,"")
        self.assertEqual(self.new_User.last_name,"")
        self.assertEqual(self.new_User.Username,"")
        self.assertEqual(self.new_User.Password,"")
        
def __init__(self,first_name,last_name,username,password):

        
        self.first_name = first_name
        self.last_name = last_name
        self.Username = username
        self.Password = password


    def test_save_User(self):
        '''
        test_save_contact test case to test if the User object is saved into
         the User list
        '''
        self.new_User.save_User() # saving the new contact
        self.assertEqual(len(User.User_list),1)

    def test_save_multiple_User(self):
            '''
            test_save_multiple_User to check if we can save multiple User
            objects to our User_list
            '''
            self.new_User.save_User()
            test_User = User("","","","") # new contact
            test_User.save_User()
            self.assertEqual(len(User.User_list),2)



if __name__ == '__main__':
    unittest.main()