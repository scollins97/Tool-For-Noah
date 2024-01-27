#creating a class to define and store number combinations
#saving all possible combinations is silly.  this class just saves the final score and the numbers of a combination 
#if the main method finds that it meets the users lot number ... or best case scenario
class combination:
    #attributes
    finalScore = 0
    theNumbers = []

    #methods
    def __init__(self, finalScore, theNumbers):
        self.finalScore = finalScore
        self.theNumbers = theNumbers