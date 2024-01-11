from .poem import Poem
from .poem_shape import PoemShape

class Sonnet(Poem): 


    def __init__(self):

        super().__init__(genre="Sonnet",number_of_verses=14,poem_shape=PoemShape([4,4,3,3]))
        self.lengths=[12]*14
        