import threading
import logging
from time import time
import requests
import threadTest

url1 = 'http://httpbin.org/get'
url2 = 'http://httpbin.org/post'

count = 0
lock = threading.Lock()
thread = 64
get = 100
tid = 0

logging.basicConfig(filename='success.log', level=logging.DEBUG)
logging.info('url = ' + url1 + '\n')
logging.info('get : ' + str(get) + '번')
logging.info('멀티 쓰레딩\n\n')
logging.info('쓰레드 개수 \t|\t시간초\n')

threadpool = set()

count = 0
tid = 0
st = time()
while count < get:
    lock.acquire()
    if len(threadpool) < thread:
        print(tid, 'was created')
        th = threadTest.kakaoClass(tid, url1, lock, threadpool)
        th.start()
        threadpool.add(tid)
        tid += 1
        count += 1
    lock.release()
while len(threadpool) > 0:
    continue
ed = time()
logging.info('\t' + str(thread) + '\t|\t' + str(ed - st))
logging.info('\n')