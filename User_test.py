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
        self.assertEqual(self.new_User.username,"")
        self.assertEqual(self.new_User.password,"")
        


    def test_save_User(self):
        '''
        test_save_contact test case to test if the User object is saved into
         the User list
        '''
        self.new_User.save_User() # saving the new contact
        self.assertEqual(len(User.User_list),1)


    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.User_list = []

    def test_save_multiple_User(self):
        '''
        test_save_multiple_User to check if we can save multiple User
        objects to our User_list
        '''
        self.new_User.save_User()
        test_User = User("","","","") 
        test_User.save_User()
        self.assertEqual(len(User.User_list),2)


    # def test_find_User_by_username(self):
    #     '''
    #     test to check if we can find a user by username and display information
    #     '''

    #     self.new_User.save_User()
    #     test_User = User("","","","")
    #     test_User.save_User()

    #     found_User = User.find_by_username("")
    #     self.assertEqual(found_User.username,test_User.username)


if __name__ == '__main__':
    unittest.main()