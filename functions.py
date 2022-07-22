import json
POST_PATH = "posts.json"

def load_posts_from_json(path=POST_PATH):
    """открываем джейсон на чтение"""
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        return "Файл не найден"
    except json.JSONDecoder:
        return "Не удалось преобразовать файл"
    else:
        return data

def dump_json(pic, content, path=POST_PATH):
    data = load_posts_from_json()
    post = {
        "pic": f"/uploads/images/{pic}",
        "content": content
    }
    data.append(post)
    with open(path, "w", encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    return post



def search_posts_by_key(post_key):
    """перебираем посты по совпадению"""
    posts = load_posts_from_json("posts.json")
    posts_list = []
    for post in posts:
        if post_key in post["content"]:
            posts_list.append(post)
    return posts_list

def is_filename_allowed(filename):
    """функция для проверки загружаемых файлов, проверяем по расширению"""
    ALLOWED_EXTENTIONS = {'png', 'jpeg', 'jpg'}
    extention = filename.lower().split('.')[-1]
    if extention in ALLOWED_EXTENTIONS:
        return True



# print(is_filename_allowed('filename.png'))