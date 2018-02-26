__author__ = 'null'

import os
import sys

class LoadData:
    def __init__(self, dirname):
        self.dirname = dirname
        self.file_name_list = []
        self.file_content_list = []
    def file_lists(self):
        file_path = os.getcwd() + "/" + self.dirname +"/"
        if os.path.isdir(self.dirname):
            for file1 in os.listdir(self.dirname):
                if file1.endswith('.txt'):
                    #print file_path + file1
                    self.file_name_list.append(file_path + file1)
    def get_file_lists(self):
        return self.file_name_list
    def read_files(self):
        for f in self.get_file_lists():
            #print 'Name:',f
            try:
                fd = open(f, 'r')
                #print fd.readlines()
                self.file_content_list.append(fd.read())
            except IOError as e:
                print "I/O error({0}): {1}".format(e.errno, e.strerror)
            else:
                fd.close()
    def get_file_content_list(self):
        return self.file_content_list
