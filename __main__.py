from crawler import RedditNewsCrawler
from data_manager import DataManager
from database_handler import DatabaseHandler

if __name__ == '__main__':
    dm = DataManager()
    dm.next_batch()
