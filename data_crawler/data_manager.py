import logging
import time

from data_crawler.crawler import RedditNewsCrawler
from data_crawler.database_handler import DatabaseHandler


class DataManager:
    """
    This class manages the crawling of new posts and the uploading to the db. It will set up a schedule for the
    Crawler and upload every new post.
    """

    def __init__(self):
        self.crawler = RedditNewsCrawler()
        self.dbh = DatabaseHandler()

    def next_batch(self):
        # get the 5 newest posts:
        posts = self.crawler.crawl(amount=5)
        # try to upload them into DB:
        for post in posts:
            _post = self.dbh.find("REDDITPOSTS", post)
            if _post is None:
                # the post is not in the DB, we can insert them:
                self.dbh.upload_post("REDDITPOSTS", post)

            else:
                logging.debug("Post with headline %s already exists..." % _post.headline)
        self.dbh.summary("REDDITPOSTS")
        self.wait()

    def wait(self):
        time.sleep(30)
