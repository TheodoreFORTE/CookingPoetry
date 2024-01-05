from nltk.corpus import cmudict
from .vocabulary_handler import VocabularyHandler
from nltk.tokenize import wordpunct_tokenize

class Verse:
    
    punct = set(['.', ',', '!', ':', ';','\''])
    pron_dict=cmudict.dict()


    def __init__(self,content):

        self.content=content
    
    @property
    def to_wordpunct_token(self):
        tokens=wordpunct_tokenize(self.content)
        filtered=[w for w in tokens if w not in Verse.punct]
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
        
