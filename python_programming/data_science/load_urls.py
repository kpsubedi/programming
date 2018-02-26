__author__ = 'null'

import sys

class LoadUrls:
    def __init__(self, url_file_path):
        self.path = url_file_path
        self.urls = []
    def get_urls(self):
        try:
            f = open(self.path,'r')
            for uri in f:
                self.urls.append(uri)
                #print uri
        except IOError as e:
            print e.message
        return self.urls




