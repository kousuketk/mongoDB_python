from datetime import datetime
from mongoSample import mongoSample


def add_sample(obj):
    post = {"title": "ハリネズミ2", "content": "かわいい", "created_at": datetime.now()}
    res = obj.add_one(post)
    print(res)
    posts = [
        {"title": "カワウソ", "content": "カワウソ可愛い~", "created_at": datetime.now()},
        {"title": "ハムスター", "content": "ハムスター可愛い~", "created_at": datetime.now()},
        {"title": "チンチラ", "content": "チンチラ可愛い~", "created_at": datetime.now()},
    ]
    res = obj.add_many(posts)
    print(res)


def get_sample(obj):
    res = obj.get_one()
    print(res)
    title = "カワウソ"
    res = obj.get_from_title(title)
    print(res)


def udpate_sample(obj):
    title = "カワウソ"
    content = "カワウソは楽しい"
    res = obj.update_content_by_title(title, content)
    print(res)
    res = obj.update_created_at()
    print(res.matched_count)


def delete_sample(obj):
    title = "チンチラ"
    res = obj.delete_by_title(title)
    print(res)


def main():
    obj = mongoSample()
    add_sample(obj)


if __name__ == "__main__":
    main()
