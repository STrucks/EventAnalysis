from data_crawler.data_manager import DataManager

if __name__ == '__main__':
    dm = DataManager()
    for i in range(5000):
        print(i)
        dm.next_batch()
