from facebook_scraper import get_posts
import json

def formatposts(x):
    #turn list to string w/ seperation between posts
    y = "\n\n".join(x)
    return y

n = int(input("How many posts to get: "))
postdict=dict()
i=0

#generator for posts from pret group
postgen = get_posts(group = "522129019655282", pages = 10, cookies = r"C:\Users\44747\facebook cookies\cookies.txt")

while i < n:
    #list of n most recent posts in reverse time, no weird symbols
    postdict[i]=(next(postgen)["text"].encode("ascii","ignore").decode())
    print("Getting post {x} of {y}...".format(x=i+1,y=n)) 
    i+=1


niceposts = postdict

with open("fb_posts.json", "w") as f:
    #write to txt file "fb_posts_lists"
    json.dump(niceposts,f)

print("Written to file")





