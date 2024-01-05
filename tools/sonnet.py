from .poem import Poem

class Sonnet(Poem): 


    def __init__(self):

        super().__init__(type="Sonnet",number_of_verses=14)
        self.lengths=[12]*14
        
