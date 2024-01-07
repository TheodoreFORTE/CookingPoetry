from .poem import Poem
from .poem_shape import PoemShape
class Sonnet(Poem): 


    def __init__(self):

        super().__init__(type="Sonnet",number_of_verses=14,format=PoemShape([4,4,3,3]))
        self.lengths=[12]*14
        
