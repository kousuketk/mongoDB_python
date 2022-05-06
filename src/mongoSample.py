from pymongo import MongoClient
from datetime import datetime


class mongoSample(object):
    def __init__(self):
        self.client = MongoClient("localhost", 27017)
        self.db = self.client["test"]

    def add_one(self, post):
        return self.db.test.insert_one(post)

    def add_many(self, posts):
        return self.db.test.insert_many(posts)

    def get_one(self):
        return self.db.test.find_one()

    def get_from_title(self, title):
        return self.db.test.find_one({"title": title})

    def update_content_by_title(self, title, content):
        return self.db.test.update_one({"title": title}, {"$set": {"content": content}})

    def update_created_at(self):
        return self.db.test.update_many({}, {"$set": {"created_at": datetime.now()}})

    def delete_by_title(self, title):
        return self.db.test.delete_one({"title": title})
