from .poem_shape import PoemShape
from .verse import Verse

class Poem: 

    def __init__(self,genre,number_of_verses,poem_shape):

        self.genre=genre
        self.verses=[Verse() for _ in range(number_of_verses)]
        

        if(isinstance(poem_shape,PoemShape)):
            self.poem_shape=poem_shape

    

    def __repr__(self):

        counter=0
        output=""
       
        for verse in self.verses:

            if hasattr(self,"poem_shape"):
                if counter in self.poem_shape.blank_indexes:
                    output+='\n'

            output+=" ".join(verse.content)+'\n'
            counter+=1
            
        return output

    def context(self,index,number_of_words):

        verse=self.verses[index]
        if len(verse.content)>=number_of_words:
            print("last context",verse.content[-4:])
            return(verse.content[-4:])
        else: 
            if len(verse.content)>0:
                last_words=verse.content
            else:
                last_words=[]
                iterator=index-1
                while iterator>=0 and len(last_words)<number_of_words:
                    curr_verse=self.verses[iterator]
                    word_count_need=number_of_words-len(last_words)
                    if len(curr_verse.content)>word_count_need:
                        word_to_add=curr_verse.content[-word_count_need:]
                        for word in reversed(word_to_add):
                            last_words.insert(0,word)
                    else:
                        word_to_add=curr_verse.content
                        for word in reversed(word_to_add):
                            last_words.insert(0,word)
                    iterator-=1

                return last_words


        
                


