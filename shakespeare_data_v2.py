import nltk
from nltk.corpus import shakespeare
import xml.etree.ElementTree as ET
from nltk.tokenize import sent_tokenize,word_tokenize
import string

from nltk.lm.vocabulary import Vocabulary
from tools.vocabulary_handler import VocabularyHandler
from tools.corpus_handler import CorpusHandler



#Setting up the data collection
fileids=shakespeare.fileids()
full_corpus=[]

#Looping over all the files found
for xml_file in fileids: 

    filepath = shakespeare.abspath(xml_file)
    tree = ET.parse(filepath)
    
    #Staying focus on Shakespeare lines of dialogue    
    elements_line = tree.findall(".//LINE")
    
    for element in elements_line:    
        if element.text is not None:  #Tokenizing cannot work on empty text
            full_corpus.append(element.text)

all_text = ' '.join(full_corpus).lower()
#print(all_text)

string.punctuation = string.punctuation
string.punctuation = string.punctuation.replace('.', '').replace('?','').replace('!','').replace('\'','')

clean_text = "".join([char for char in all_text if char not in string.punctuation])
clean_text="".join([f" {char}" if char in [".","?","!"] else char for char in clean_text])

print(clean_text)

sents = nltk.sent_tokenize(clean_text)
print("The number of sentences is", len(sents)) 
#prints the number of sentences
words = nltk.word_tokenize(clean_text)
print("The number of tokens is", len(words)) 
#prints the number of tokens
average_tokens = round(len(words)/len(sents))
print("The average number of tokens per sentence is",
average_tokens) 
#prints the average number of tokens per sentence
unique_tokens = set(words)
print("The number of unique tokens are", len(unique_tokens)) 
#prints the number of unique tokens


#VocabularyHandler.save_vocabulary(vocabulary,"shak-2")
CorpusHandler.save_corpus(sents,"shak-2")

tokens = word_tokenize(clean_text)
vocabulary=Vocabulary(tokens,unk_cutoff=2)
VocabularyHandler.save_vocabulary(vocabulary,"shak-2")

















'''
tokens = word_tokenize(all_text)

vocabulary=Vocabulary(tokens,unk_cutoff=2)
'''