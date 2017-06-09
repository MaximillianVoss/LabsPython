import threading
import requests
import sys

import time
import argparse


def timer(method):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = method(*args, **kwargs)
        finish = time.time()
        print('Download time:' + str(finish - start))
        return result

    return wrapper


class Donwloader(threading.Thread):
    def __init__(self, url, folder, fileName, ids):
        super().__init__()
        self.url = url
        self.folder = folder
        self.ids = ids
        self.fileName = fileName

    @timer
    def run(self):
        for id in self.ids:
            try:
                self._download_page(id)
            except BaseException:
                print('exception during download page!')

    def _download_page(self, id):
        fileName = self.folder + self.fileName + str(id) + '.html'
        with open(fileName, 'w') as file:
            file.write(requests.get(self.url + str(id)).text)
