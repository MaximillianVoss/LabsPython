import unittest
import time
from pathlib import Path

from MyProject.downloader import Donwloader
from os import listdir
from os.path import isfile, join
import os


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        count = 25
        url = 'https://stackoverflow.com/questions/'
        fileName = 'Question_'
        folder = 'Pages/'
        Donwloader(url, folder, fileName, range(count)).start()
        time.sleep(10)

    def testDownload(self):
        onlyfiles = [f for f in listdir(os.getcwd() + "\Pages") if isfile(join(os.getcwd() + "\Pages", f))]
        for i in range(0, len(onlyfiles) - 1):
            my_file = Path(os.getcwd() + "\Pages" + onlyfiles[i])
            if my_file.is_file():
                self.assertEqual(onlyfiles[i], 'Question_' + str(i) + '.html')


if __name__ == '__main__':
    unittest.main()
