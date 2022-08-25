import sys
from threading import Thread
from queue import Queue

import crawler.crawler_vk as cr


concurrent = 20
count_tab_chrome = int(input())
q = Queue(concurrent * 2)


def doWork():
    while True:
        cr.open_video()
        q.task_done()


for i in range(concurrent):
    t = Thread(target=doWork)
    t.daemon = True
    t.start()
try:
    for item in range(count_tab_chrome):
        q.put(item)
    q.join()
except KeyboardInterrupt:
    sys.exit(1)
