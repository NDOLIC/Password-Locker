class User:
    """
    Class that generates new instances of details
    """

    pass

    User_list = []

    def save_User(self):

            '''
            save_User method saves User objects into User_list
            '''

            User.User_list.append(self)

    @classmethod
    def find_by_username(cls,username):
        '''
        Method that takes in a username and returns a User that matches that username.

        Args:
            username: username to search for
        Returns :
            User of person that matches the username.
        '''

        for User in cls.User_list:
            if User.username == username:
                return User


    @classmethod
    def User_exist(cls,username):
        '''
        Method that checks if a user exists from the user list.
        Args:
            username: username to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for User in cls.User_list:
            if User.username == username:
                    return True

    def __init__(self,first_name,last_name,username,password):

            
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
