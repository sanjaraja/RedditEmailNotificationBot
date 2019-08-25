import praw
from prawCredentials import client_id, client_secret, password, user_agent, username
from requests import session

email_id = input("What is the email id that you want notifications sent to?")
password = input("What is the password of the email_id that you provided")
print("Email id", email_id)
print("Password", password)