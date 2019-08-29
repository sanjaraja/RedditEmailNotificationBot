import praw #Importing the praw wrapper
from prawCredentials import client_id, client_secret, password, user_agent, username #Importing bot credentials from prawCredentials.py
from requests import Session #Need to import this for bot credentials
import smtplib, ssl
import time

def streamProcess(bot, key_words): #Need to pass in the instantiated bot and the key words that need to be searched
    return_dic = {}
    for submission in bot.new(limit=1):
        for word in key_words:
            if word.lower() in submission.title.lower():
                item = [submission.title, submission.score, submission.shortlink, submission.subreddit, word]
                return_dic["submission"] = item

    return return_dic

def send_email(arr, mail_address, password):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = mail_address
    receiver_email = "rajasekaran.sanjay@gmail.com"
    message = """\
    Subject: Notfication of {key_word} in {subreddit}


    You are receiving this message from the reddit notification
    email bot because your desired key word from a desired subreddit
    has appeared on a new post. Check it out! 

    This is the title of the post: {title}
    This is the submission score: {score}
    This is the link to the post: {link}
    This is the subreddit: {subreddit}

    """.format(title=arr[0], score=arr[1], link=arr[2], subreddit=arr[3], key_word=arr[4])

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


def main():
    """ Asking for input from user as to which email id the bot needs to notify and what key words to look for in which subreddits"""
email_id = input("What is the email id that you want notifications sent to?").strip() #Asking for email id
password = input("What is the password of the email_id that you provided").strip() #Asking for password for email id
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

subredditString = "+".join(subreddits).replace(" ", "").strip()#Joining subreddits that need to be searched with a + 
#subredditString = subredditString.strip()
print(subredditString)
bot = reddit.subreddit(subredditString) #Creating a subreddit instance with the subreddits that need to be traversed
check_arr = []
while True:
    dic = streamProcess(bot, key_words)
    for key in dic.keys():
        if(dic[key][2] in check_arr):
            print("Already here")
        else:
            print("The notification is being sent to email", dic[key])
            send_email(dic[key], email_id, password)
            print("Email has been sent")
            check_arr.append(dic[key][2])
    print("Resting")
    time.sleep(0.5)
    print("Rest Over")


if __name__ == "__main__":
    main()

