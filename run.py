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

