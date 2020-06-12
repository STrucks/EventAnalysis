from crawler import RedditNewsCrawler
from data_manager import DataManager
from database_handler import DatabaseHandler

if __name__ == '__main__':
    dm = DataManager()
    for i in range(5000):
        print(i)
        dm.next_batch()
