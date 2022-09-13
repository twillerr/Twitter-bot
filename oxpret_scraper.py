from facebook_scraper import get_posts

group_id = "522129019655282"
cookies_path=r"C:\Users\44747\Twitter-bot\cookies.txt"

#generator for facebook group posts
postgen = get_posts(group = group_id, pages = 2, cookies = cookies_path)

def get_recent_post():
    recent_posts=[]
    i=1
    while i<=2:
        recent_posts.append(next(postgen)["text"].encode("ascii","ignore").decode())
        i+=1
    post=recent_posts[1]
    return post

def write_to_file(msg):
    with open("fb_posts.txt", "w") as f:
        f.write(msg)
