from .poem_shape import PoemShape

class Poem: 

    def __init__(self,type,number_of_verses,poem_shape):

        self.type=type
        self.verses=[None]*number_of_verses
        

        if(isinstance(poem_shape,PoemShape)):
            self.poem_shape=poem_shape

    

    def __repr__(self):

        counter=0
        output=""
       
        for verse in verse:

            if hasattr("poem_shape"):
                if counter in self.poem_shape.blank_indexes:
                    output+='\n'
            output+=verse+'\n'
            counter+=1
            
        return output
