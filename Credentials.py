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


    def __init__(self,site,username,password):
        self.site = site
        self.Username = username
        self.Password = password
