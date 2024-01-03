import nltk
from nltk.corpus import shakespeare
import xml.etree.ElementTree as ET
from nltk.tokenize import word_tokenize
from nltk.lm.vocabulary import Vocabulary

from tools.vocabulary_handler import VocabularyHandler



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

all_text = ' '.join(full_corpus)
tokens = word_tokenize(all_text)
vocabulary=Vocabulary(tokens,unk_cutoff=2)


VocabularyHandler.save_vocabulary(vocabulary,"shakespearian")

