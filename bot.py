import praw #Importing the praw wrapper
from prawCredentials import client_id, client_secret, password, user_agent, username #Importing bot credentials from prawCredentials.py
from requests import Session #Need to import this for bot credentials

def main():
    """ Asking for input from user as to which email id the bot needs to notify and what key words to look for in which subreddits"""
email_id = input("What is the email id that you want notifications sent to?") #Asking for email id
password = input("What is the password of the email_id that you provided") #Asking for password for email id
key_words = input("Enter the key words that you want to search for as comma seperated values.").split(",") #Generating array of key words
subreddits = input("Enter the subreddits that you want to search these key_words for").split(",") #Generating array of subreddits

""" Instantiating the bot which will search for key words within the subreddits mentioned """
session = Session()
reddit = praw.Reddit(client_id= client_id,
                     client_secret= client_secret,
                     password= password,
                     requestor_kwargs={'session': session},  # pass Session
                     user_agent= user_agent,
                     username= username)

if __name__ == "__main__":
    main()

