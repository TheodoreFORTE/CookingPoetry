from nltk.corpus import cmudict
from .vocabulary_handler import VocabularyHandler


class Verse:
    
    punct = set(['.', ',', '!', ':', ';','\'','?'])
    pron_dict=cmudict.dict()


    def __init__(self,text=None,allow_end_of_sentence=False,could_be_end_by_dot=True):

        if(text):
            self.content=text.split()
        else:
            self.content=[]
        self.allow_end_of_sentence=allow_end_of_sentence

    @property
    def to_wordpunct_token(self):
        filtered=[w for w in self.content if w not in Verse.punct]
        return filtered

    @property 
    def number_of_syllables(self):
        filtered=self.to_wordpunct_token
        number=0
        for word in filtered: 
            if word.lower() in Verse.pron_dict:
                number+=max([len(list(y for y in x if y[-1].isdigit())) for x in Verse.pron_dict[word.lower()]])
            else:
                print(word,"is unknown")
        return number
    
    @property
    def rhyme(self):
        filtered=self.to_wordpunct_token
        last_word=filtered[-1]
        if last_word.lower() in Verse.pron_dict:
            rhyme=Verse.pron_dict[last_word.lower()][-1][-2:]
            return rhyme
        else: 
            print(f"{last_word}'s pronunciation not found")
    

    def add(self,text):

        list=text.split()       
        for text in list:
            self.content.append(text)

    def check_integrity(self):

        if(self.allow_end_of_sentence==False):
            for token in self.content: 
                if token in [".","?","!"]:
                    return False
        return True

    def empty(self):

        self.content=[]


        
