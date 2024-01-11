from .sonnet import Sonnet
from .verse import Verse
class PoemBuilder: 

    '''
    Given an a nltk model that has been fitted,  this class must be able to generate 
    poems following theirs constraints (rhymes, shape, length of verses) for every type supported.
        
    '''



    def __init__(self,data_prep):

        self.data_prep=data_prep
        self.model=data_prep.model


    '''
    Reminder of all the nltk.lm.models method that can be used :
    entropy(text_ngrams)
    fit(text, vocabulary_text=None)
    generate(num_words=1, text_seed=None, random_seed=None)
    logscore(word, context=None)
    perplexity(text_ngrams)
    score(word, context=None)

    unmasked_score(word, context=None) (abstract method, only if implemented)    
    
    '''
    
    def fill_poem(self,poem=Sonnet(),start=None):
        
        #To be implemented

        if(start):
            
            start_verse=Verse(start)            
            poem.verses[0].add(start)
            
            if start_verse.number_of_syllables>poem.lengths[i]:
                print("This start is way too long")
            else: 
                poem.verses[0]=start_verse

        for i in range(len(poem.verses)):
                poem.verses[i]=self.generate_verse(poem,i)

        return(poem)
    
    def generate_verse(self,poem,index_verse):

        verse=poem.verses[index_verse]
        length=poem.lengths[index_verse]
        while(True):           
            
            while verse.number_of_syllables<length:
                word=self.model.generate(1,text_seed=poem.context(index_verse,4))
                verse.add(word)
            
            if verse.check_integrity():
                
                print(self.model.perplexity(" ".join(verse.content)))
                return verse
            else: 
                verse.empty()
            
            





        





        





        