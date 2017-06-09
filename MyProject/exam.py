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
        print(finish - start)

        return result

    return wrapper


class Donwloader(threading.Thread):
    def __init__(self, ids):
        super().__init__()
        self.ids = ids

    @timer
    def run(self):
        for id in self.ids:
            self._download_page(id)

    def _download_page(self, id):
        url = 'https://stackoverflow.com/questions/' + str(id)
        file_name = 'SomeFile' + str(id) + '.html'

        with open(file_name, 'w') as file:
            file.write(requests.get(url).text)


# parser = argparse.ArgumentParser()
# parser.add_argument('-s', '--start', dest='start')
# parser.add_argument('-f', '--finish', dest='finish')
# parser.add_argument('-p', '--process_count', dest='pr_count')
# args = parser.parse_args()

# print(args)
# for i in range(0, int(args.pr_count)):
#     dwnl = Donwloader(str((args.start + str(i), args.finish, args.pr_count)))
#     dwnl.start()
dwnl = Donwloader(range(1, 10, 10))
dwnl.start()
