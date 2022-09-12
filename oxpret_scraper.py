from facebook_scraper import get_posts
from itertools import islice
import json

postgen = get_posts(group = "522129019655282", pages = 10, cookies = r"C:\Users\44747\facebook cookies\cookies.txt")

def formatposts(x):
    #turn list to string w/ seperation between posts
    y = "\n\n".join(x)
    return y

def get_recent_post():
    #write most recent post to file
    recent_posts=[]
    i=1
    while i<=2:
        recent_posts.append(next(postgen)["text"].encode("ascii","ignore").decode())
        i+=1

    post=recent_posts[1:2][0]
    return post

def write_to_file(msg):
    with open("fb_posts.txt", "w") as f:
        f.write(msg)

write_to_file(get_recent_post())
