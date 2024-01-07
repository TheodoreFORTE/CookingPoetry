from .corpus_handler import CorpusHandler
from .vocabulary_handler import VocabularyHandler
from nltk.util import ngrams 
from nltk.lm.counter import NgramCounter
from nltk.tokenize import word_tokenize


class DataPreparation: 

    '''
    The class that will have to contain all the elements to instantiate nltk language models, 
    such as : the vocabulary, the text to train the model, and the ngram counter.

    '''

    def __init__(self,corpus_label,vocab_label,ngram_ids=[1,2,3,4]):

        self.vocabulary=VocabularyHandler.load_vocabulary(vocab_label)
        self.corpus=CorpusHandler.load_corpus(corpus_label)
        self.sentences=[word_tokenize(sent) for sent in self.corpus]


        self.ngram_counter=self.fill_ngrams(ngram_ids)

    def fill_ngrams(self, ngram_ids):

        ngram_list = []
        for i in ngram_ids:
            ngram_list+=list(tuple(ngrams(sent, i)) for sent in self.sentences)
    
        return NgramCounter(ngram_list)

    def training_data_ngrams(sentence):

        return ngrams(sentence,3)
   