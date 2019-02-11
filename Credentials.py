class Credentials:
    """
    Class that generates new instances of pass-word and site
    """

    pass

    Credentials_list = []

    def save_Credentials(self):

            '''
            save_Credentials method saves Credentials objects into Credentials_list
            '''

            Credentials.Credentials_list.append(self)

    def delete_Credentials(self):

        '''
        delete_credentials method deletes a saved credentials from the credentials_list
        '''

        Credentials.Credentials_list.remove(self)

    # @classmethod
    # def find_by_username(cls,username):
    #     '''
    #     Method that takes in a username and returns a credentials that matches that username.

    #     Args:
    #         usename: username to search for
    #     Returns :
    #         Credentials of person that matches the username.
    #     '''

    #     for Credentials in cls.Credentials_list:
    #         if Credentials.username == username:
    #             return Credentials

    @classmethod
    def Credentials_exist(cls,username):
        '''
        Method that checks if a Credentials exists from the Credentials list.
        Args:
            username: username to search if it exists
        Returns :
            Boolean: True or false depending if the Credentials exists
        '''
        for Credentials in cls.Credentials_list:
            if Credentials.username == username:
                    return True

        return False

    def __init__(self,site,username,password):
        self.site = site
        self.username = username
        self.password = password
