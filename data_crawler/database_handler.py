import logging

from pymongo import MongoClient

from data_crawler.configurations.config_loader import ConfigLoader
from data_crawler.models.reddit_post import RedditPost


class DatabaseHandler:

    def __init__(self):
        cl = ConfigLoader()
        logging.basicConfig(level=cl.get_logging_level())
        client = MongoClient(cl.get("mongo_db_ip"))
        self.db = client[cl.get("database_name")]

    def upload_post(self, table_name, post: RedditPost):
        result = self.db[table_name].insert_one(post.to_dict())
        logging.debug("--Inserted object with text %s..." % post.headline)

    def find(self, table_name, post: RedditPost):
        post = self.db[table_name].find_one({"headline": post.headline,
                                             "section": post.section,
                                             "date": post.date})
        if post is not None:
            post = RedditPost(headline=post['headline'], section=post['section'], date=post['date'], time=post['time'])
        return post

    def summary(self, table_name):
        count = self.db[table_name].count_documents({})
        print("Number of documents: %d" % count)

