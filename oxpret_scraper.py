from facebook_scraper import get_posts

group_id = "522129019655282"
cookies_path=r"C:\Users\44747\Twitter-bot\cookies.txt"

def get_recent_post():
    #get latest post from generator and add to list
    postgen = get_posts(group = group_id, pages = 2, cookies = cookies_path)
    recent_posts=[]
    i=1
    while i<=2:
        recent_posts.append(next(postgen)["text"].encode("ascii","ignore").decode())
        i+=1
    post=recent_posts[1]
    #first item yielded by generator is pinned post, skips this
    return post

def write_to_file(msg):
    with open("fb_posts.txt", "w") as f:
        f.write(msg)

def read_from_file():
    with open("fb_posts.txt", "r") as f:
        text = f.read()
    return text

