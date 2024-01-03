
import nltk
import json
from nltk.lm.vocabulary import Vocabulary

class VocabularyHandler: 
    
    def save_vocabulary(vocab,output_filename):

        if(isinstance(vocab,nltk.lm.Vocabulary)):

            vocab_data={}
            vocab_data["counts"]=vocab.counts
            vocab_data["unk_label"]=vocab.unk_label
            vocab_data["unk_cutoff"]=vocab._cutoff

            with open(f'vocabs/{output_filename}.json', 'w', encoding='utf-8') as file:
                json.dump(vocab_data, file, ensure_ascii=False)


    def load_vocabulary(filename):

            with open(f'vocabs/{filename}.json', 'r', encoding='utf-8') as file:
                    vocab_data = json.load(file)
                    vocab=Vocabulary([])
                    vocab.counts=vocab_data["counts"]
                    vocab.unk_label=vocab_data["unk_label"]
                    vocab._cutoff=vocab_data["unk_cutoff"]

                    return vocab

            