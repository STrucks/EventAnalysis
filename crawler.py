from datetime import datetime
import time

import requests
import urllib.request
from bs4 import BeautifulSoup

from configurations.config_loader import ConfigLoader
from models.reddit_post import RedditPost


class RedditNewsCrawler:
    """
    This class is designed to crawl posts from the fresh section of 9gag.com. It will save the posts (parts of it)
    in the DB.
    """

    def __init__(self):
        cl = ConfigLoader()
        self.base_url = cl.get("reddit_base_url")

        self.headers = {'User-Agent': 'Mozilla/5.0'}

    def crawl(self):
        """
        This function crawls the newest 5 posts on https://www.reddit.com/r/news/new/ and returns them as
        RedditPost object.
        :return:
        """
        session = requests.session()
        response = session.get(self.base_url, headers=self.headers)
        html = BeautifulSoup(response.text, 'html.parser')
        # find the current 5 newest post:
        newest_posts = html.find_all("h3", {"class": "_eYtD2XCVieq6emjKBH3m"})[0:5]
        newest_posts_text = [post.text for post in newest_posts]

        posts = [RedditPost(headline=text, date=datetime.today().strftime('%Y-%m-%d'),
                          time=datetime.today().strftime('%H:%M:%S'),
                          section="News") for text in newest_posts_text]
        return posts

