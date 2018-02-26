__author__ = 'null'

from load_data import *
from gensim import corpora, models, similarities
from stop_words import get_stop_words
from collections import defaultdict
from matplotlib import pyplot as plt

def main():
    loadData = LoadData('data')
    #loadData.readfiles()
    loadData.file_lists()
    loadData.read_files()
    file_content_list = loadData.get_file_content_list()
    #print type(file_content_list), len(file_content_list)

    # remove common words and tokenize using space as a separator
    stop_word_list = get_stop_words('en')
    #print type(stop_word_list), len(stop_word_list), stop_word_list
    #print type(stop_word_list)
    texts = [[word for word in doc.lower().split() if word not in stop_word_list] for doc in file_content_list]
    #for text in texts:
        #print text
    # remove words that appear only once
    frequency = defaultdict(int)
    for text in texts:
        for token in text:
            frequency[token] += 1
    texts = [[token for token in text if frequency[token] >= 1]
             for text in texts]

    # remove token with length one or two
    n_texts = []
    for text in texts:
        n_text = []
        for item in text:
            if len(item) > 2:
                n_text.append(item)
        n_texts.append(n_text)

    #for t in n_texts:
       #print t
    dictionary = corpora.Dictionary(n_texts)
    #print dictionary
    #print dictionary.token2id
    corpus = [dictionary.doc2bow(new_text) for new_text in n_texts]
    #for c in corpus:
        #print c
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    #for d in corpus_tfidf:
        #print d
    # LSI Model
    lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=10)
    corpus_lsi = lsi[corpus_tfidf]
    for topic in lsi.print_topics(num_topics=10, num_words=5):
        print topic
    #
    x = []
    y = []
    for doc1 in corpus_lsi:
        x.append(doc1[0][1])
        y.append(doc1[1][1])
    ###################################

    plt.figure(figsize=(10,8))
    plt.plot(x,y,'or')
    plt.title('document in the new space')
    plt.xlabel('topic 1')
    plt.ylabel('topic 2')
    s = 0.01
    for i in range(len(x)):
        plt.text(x[i]+s, y[i] + s, "doc "+str(i+1))
    plt.show()

if __name__=='__main__':
    main()
