import tweepy
import config
import time
from oxpret_scraper import get_recent_post, write_to_file,read_from_file

consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token
access_token_secret = config.access_token_secret
bearer_token = config.bearer_token

client = tweepy.Client(bearer_token,consumer_key, consumer_secret,access_token, access_token_secret)

intro_msg = "!! OXPRET UPDATE !!:\n"

def publish_post(msg):
    client.create_tweet(text=intro_msg+f"\"{msg}\"")   

def check_and_update():
    web_post= get_recent_post()
    local_post= read_from_file()
    if web_post != local_post:
        print("New post found!")
        write_to_file(get_recent_post())
        publish_post(web_post)
    else:
        print("No new posts.")

while True:
    check_and_update()
    time.sleep(30)
    print("checking again...")
