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

    def __init__(self,first_name,last_name,username,password):

            
        self.first_name = first_name
        self.last_name = last_name
        self.Username = username
        self.Password = password
