import multiprocessing as mp
import requests as rq
import json
import time

filename = 'process_log'

def multi(idx, q, res):
    while True:
        url = q.get()
        # print('id : {id} something doing...'.format(id = idx))
        try:
            response = rq.get(url)
            with open(filename, 'a') as f:
                f.write(response.text + '\n\n')
            res.put((1, url))
        #    print("id : {id} task complete!".format(id=idx))

        except Exception as err:
            print(err)
            res.put((1, 'no'))