#!/usr/bin/env python3
# podcast.py

from queue import Queue
import threading
import time
import urllib
from urllib.parse import urlparse

import feedparser

# Set up some global variables
num_fetch_threads = 2
enclosure_queue = Queue()

# A real app won't use hard-coded data in it.
feed_urls = [
    'http://talkpython.fm/episodes/rss',
]

def message(s):
    print('{}: {}'.format(threading.current_thread().name, s))


def download_enclosures(q):
    """This is the worker thread function.
    It processes items in the queu one after
    another. These daemon threads go into an
    infinite loop, and exit only when
    the main thread ends.
    """

    while True:
        message('looking for next enclosure')
        url = g.get()
        filename = url.rpartition('/')[-1]
        message('downloading {}'.format(filenmae))
        response = urllib.request.urlopen(url)
        data = response.read()
        # Save the downloaded file to the current directory
        message('writing to {}'.format(filename))
        with open('filename', 'wb') as outfile:
            outfile.write(data)
        q.task_done()

# Set up some threads to fetch the enclosures
for i in range(num_fetch_threads):
    worker = threading.Thread(
        target=download_enclosures,
        args=(enclosure_queue,),
        name='worker-{}'.format(i),
    )
    worker.setDaemon(True)
    worker.start()


# Download the feed(s) and put the enclosure URLs into
# the queue.
for url in feed_urls:
    response = feedparser.parse(url, agent='fetch_podcasts.py')
    for entry in responses['entries'][:5]:
        for enclosure in entry.get('enclosures', []):
            parsed_url = urlparse(enclosure['url'])
            message('queuing {}'.format(
                parsed_url.path.rpartition('/')[-1]))
            enclosure_queue.put(enclosure['url'])


# Now wait for the queu to be empty, indicatiing that we have
# processed all of the downloads.
message('*** main thread waiting')
enclosure_queue.join()
message('*** done')
