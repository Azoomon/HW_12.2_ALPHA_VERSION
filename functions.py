import json

def load_posts_from_json(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def search_posts_by_key(post_key):
    posts = load_posts_from_json("posts.json")
    posts_list = []
    for post in posts:
        if post_key in post["content"]:
            posts_list.append(post)
    return posts_list

# search_posts_by_key("погулять")