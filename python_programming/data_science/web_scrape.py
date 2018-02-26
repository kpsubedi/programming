__author__ = 'null'

import urllib2
import re

class WebScrape:
    def __init__(self, input_url):
        """

        :type self: url input
        """
        self.url = input_url
        self.html_text = ''
        self.text = ''
        
    def get_text(self):
        return self.text

    def process_html(self):

        multiple_space_regx = re.compile(r'\s\s+')
        url_text_afterspace = multiple_space_regx.sub(' ', self.html_text)

        remove_comment_regx = re.compile(r'<!--(.|\s)*?-->')
        url_text_aftercomment = remove_comment_regx.sub('', url_text_afterspace)

        remove_htmltag_regx = re.compile(r'<[^>]*>')
        url_text_afterhtml = remove_htmltag_regx.sub('',url_text_aftercomment)

        remove_punctuation_regx = re.compile(r'[,\'\"!=\$\.\-\|:;~\*\\@\/%\#\?\_\{\}\+\&>]+')
        url_text_afterpunctuation = remove_punctuation_regx.sub(' ',url_text_afterhtml)

        remove_digits = re.compile(r'[0-9]')
        url_text_digitsremove = remove_digits.sub('', url_text_afterpunctuation)

        remove_parenthesis = re.compile(r'[\(\)]+')
        url_text_parenthesis_reomove = remove_parenthesis.sub('',url_text_digitsremove)

        remove_nonascii = re.compile(r'[^\x00-\x7F]+')
        url_text_after_nonascii = remove_nonascii.sub(' ',url_text_parenthesis_reomove)

        remove_extra1 = re.compile(r'&gt')
        url_text_afterextra1 = remove_extra1.sub('', url_text_after_nonascii)

        remove_extra2 = re.compile(r'&nbsp')
        url_text_afterextra2 = remove_extra2.sub('', url_text_afterextra1)

        remove_extra3 = re.compile(r'&amp')
        url_text_afterextra3 = remove_extra3.sub('', url_text_afterextra2)

        remove_opening_closing_bracket = re.compile(r'[\[\]]+')
        url_text_removing_brackets = remove_opening_closing_bracket.sub('', url_text_afterextra3)

        url_text_space_removal = multiple_space_regx.sub(' ', url_text_removing_brackets)

        remove_leading_trailing_whitespace = re.compile(r'^\s+|\s+$')
        url_text_leading_trailing_space = remove_leading_trailing_whitespace.sub('', url_text_space_removal)

        remove_newline_tab = re.compile(r'\n\r\t')
        url_text_final = remove_newline_tab.sub(' ', url_text_leading_trailing_space)
        self.text = url_text_final
        #print url_text_final

    def fetch_html(self):
        headers = {}
        headers['User-Agent'] = 'Googlebot'
        request = urllib2.Request(self.url, headers=headers)
        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError as e:
            if e.code == 404:
                print '404 Error', e.msg
            else:
                print 'Id onot know', e.msg
        except urllib2.URLError as e:
            print 'Url Error:', e.msg
        else:
            print response.getcode()
            url_text = response.read()
            print response.info()
            print response.geturl()
            #print url_text
            self.html_text = url_text
            #self.process_html(url_text)
            response.close()

#def main():
    #url = 'https://www.microsoft.com'
    #url = 'http://www.cs.ucsb.edu/~vigna/research.html'
    #url = 'https://www.memphis.edu/psychology/'
    #get_html(url)
    #webScraper = WebScrape(url)
    #webScraper.fetch_html()
    #webScraper.process_html()
    #print webScraper.get_text()

#if __name__=='__main__':
    #main()