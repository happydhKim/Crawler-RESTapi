import threading
import logging
from time import time
import requests


class kakaoClass(threading.Thread):

    def __init__(self, idx, url, lock, threadpool):
        super().__init__()
        #global url
        self.url = url
        self.idx = idx
        self.lock = lock
        self.threadpool = threadpool

    def run(self):
        response = requests.get(self.url)
        #global threadpool


        self.lock.acquire()
        self.threadpool.remove(self.idx)
        self.lock.release()
        print('id ', self.idx, ' end')