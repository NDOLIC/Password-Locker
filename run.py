#!/usr/bin/env python3.6
from User import User
from Credentials import Credentials


    def create_User(,,,):
        '''
        Function to create a new user
        '''
        new_User = User(,,,)
        return new_User

    def create_Credentials(,,):
        '''
        Function to create a new credentials
        '''
        new_Credentials = Credentials(,,)
        return new_Credentials


    def save_User(User):
        '''
        Function to save user
        '''
        User.save_User()

    def save_Credentials(Credentials):
        '''
        Function to save credentials
        '''
        Credentials.save_Credentials()

    def del_Credentials(Credentials):
        '''
        Function to delete a Credentials
        '''
        Credentials.delete_Credentials()

    def find_User(username):
        '''
        Function that finds a user by username and returns the user
        '''
        return User.find_by_username(username)
    

    def find_Credentials(site):
        '''
        Function that finds a credentials by site and returns the credentials
        '''
        return Credentials.find_by_site(site)


    def check_existing_User(username):
        '''
        Function that check if a user exists with that username and return a Boolean
        '''
        return User.User_exist(username)


    def check_existing_Credentials(username):
        '''
        Function that check if a credentials exists with that username and return a Boolean
        '''
        return Credentials.Credentials_exist(username)


    def display_Credentials():
        '''
        Function that returns all the saved Credentials
        '''
        return Credentials.display_Credentials()


    def main():
    print("Hello Welcome to your user list. What is your first_name?")
    print("Hello Welcome to your user list. What is your last_name?")
    
            username = input()
            password = input()

            print(f"Hello {username}")
            print('\n')

            while True:
                    print("Use these short codes : cc - create a new Credentials, dc - display Credentials, fc -find a contact, ex -exit the contact list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New Contact")
                            print("-"*10)

                            print ("First name ....")
                            f_name = input()

                            print("Last name ...")
                            l_name = input()

                            print("Phone number ...")
                            p_number = input()

                            print("Email address ...")
                            e_address = input()


                            save_contacts(create_contact(f_name,l_name,p_number,e_address)) # create and save new contact.
                            print ('\n')
                            print(f"New Contact {f_name} {l_name} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_contacts():
                                    print("Here is a list of all your contacts")
                                    print('\n')

                                    for contact in display_contacts():
                                            print(f"{contact.first_name} {contact.last_name} .....{contact.phone_number}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any contacts saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the number you want to search for")

                            search_number = input()
                            if check_existing_contacts(search_number):
                                    search_contact = find_contact(search_number)
                                    print(f"{search_contact.first_name} {search_contact.last_name}")
                                    print('-' * 20)

                                    print(f"Phone number.......{search_contact.phone_number}")
                                    print(f"Email address.......{search_contact.email}")
                            else:
                                    print("That contact does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")

