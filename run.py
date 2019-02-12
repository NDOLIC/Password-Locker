#!/usr/bin/env python3.6
from User import User
from Credentials import Credentials
def create_User(first_name,last_name,username,password):
    '''
    Function to create a new user
    '''
    new_User = User(first_name,last_name,username,password)
    return new_User

def create_Credentials(site,username,password):
    '''
    Function to create a new credentials
    '''
    new_Credentials = Credentials(site,username,password)
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
    print("Hello Welcome to your user list. What is your username?")
    username = input()
    print("Hello Welcome to your user list. What is your Password?")
    password = input()

    print(f"Hello {username}")
    print('\n')

    while True:
           print("Use these short codes : cc - create a new User,cd - Create a new Credentials dc - display Credentials,sv - Save a Credentials, fc -find a Credentials, ex -exit the Credentials list ")

           short_code = input().lower()

    if short_code == 'cc':
            print("New User")
            print("-"*10)

            print ("First_name ....")
            first_name = input()


            print("Last_name ...")
            last_name = input()

            print("User_Name ...")
            username = input()

            print("Password ...")
            password = input()

            save_User(create_User(first_name,last_name,username,password)) # create and save new user.
            print ('\n')
            print(f"New User {first_name} {last_name} created")
            print ('\n')


    elif short_code == 'cd':
            print("New Credentials")
            print("-"*10)

            print ("Website_Name ....")
            site = input()

            print("User_Name ...")
            username = input()

            print("Password ...")
            password = input()

            save_Credentials(create_Credentials(site,username,password)) # create and save new Credentials.
            print ('\n')
            print(f"New Credentials {site} { username} created")
            print ('\n')


    elif short_code == 'dc':

    if display_Credentials():
                            print("Your Credentials are:")
                            print('\n')

            for Credentials in display_Credentials():
                    print(f"{Credentials.site} {Credentials.username} {Credentials.password_}")

            print('\n')
        else:
            print('\n')
            print("You are not registered yet")
            print('\n')

    elif short_code == 'fc':

            print("Enter the site you want to search for")

            search_site = input()
    if check_existing_Credentials(search_site):
                search_Credentials = find_Credentials(search_site)
                print(f"{search_Credentials.username} {search_Credentials.password}")
                print('-' * 20)

                print(f"Website.......{search_Credentials.site}")
                print(f"Email address.......{search_Credentials.username}")
    else:
        print("That Credentials does not exist")

    elif short_code == "ex":
        print("Bye .......")
        break
    else:
        print("I really didn't get that. Please use the short codes")

    if __name__ == '__main__':
                main()