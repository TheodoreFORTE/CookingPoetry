

class PoemShape: 

    """ 
    This "simple" class handles the format of the poem. Basically : how many strophes and when you must print an empty line.
    Can contain a mapping of the rhymes too
    
    """

    def __init__(self,shape,rhymes=None):

        self.shape=shape
        self.rhymes=rhymes

    @property
    def blank_indexes(self):

        indexes=self.shape.copy()
        for i in range(1,len(indexes)):
            indexes[i]+=indexes[i-1]
        return indexes

        


if __name__=='__main__':

    my_shape=PoemShape([4,4,3,3])
    print(my_shape.blank_indexes)
    
