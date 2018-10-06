import multiprocessing as mp
import requests as rq
import json
import time
import multiProcessingTest

cntlock = mp.Lock()
filename = 'process_log'

#def multiUrl():


get = 100
if __name__ == '__main__':
    with open(filename, 'w') as f:
        pass
    st = time.time()
    q = mp.Queue()
    res = mp.Queue()
    url1 = 'http://httpbin.org/get'
    url2 = 'http://httpbin.org/post'
    for i in range(32):
        proc = mp.Process(target=multiProcessingTest.multi, args=(i, q, res))
        proc.daemon = True
        proc.start()
    cnt = 0
    re = 0
    while cnt < get:
        q.put(url2)
        ech = cnt
        while ech < get:
            q.put(url2)
            ech += 1

        while cnt < get:
            r = res.get()
            if r[1] == 'no':
                re += 1
            cnt += 1
        get += re
        re = 0

    ed = time.time()
    print(ed - st)