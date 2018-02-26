__author__ = 'null'

import sys
import os

class CreateFile:
    def __init__(self, inputtext, filename):
        self.text = inputtext
        self.fname = filename

    def create_file(self):

        #if not os.listdir("data"):
        try:
            f = open('data/'+self.fname, 'w+')
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
        except ValueError:
            print "Could not convert data to an integer."
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise
        else:
            f.write(self.text)
            print "File Created"
            f.close()

