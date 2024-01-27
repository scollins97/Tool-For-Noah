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

'''
this method is going to take a list of "combinations" and sort their final scores
the scores that meet the users goal (or get the closest compared to the rest) should appear at top of list
sorting by list
'''
def sortMyCombos():
