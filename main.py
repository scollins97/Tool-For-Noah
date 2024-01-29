from itertools import combinations
#creating a class to define and store number combinations
#saving all possible combinations is silly.  this class just saves the final score and the numbers of a combination 
#if the main method finds that it meets the users lot number ... or best case scenario
class Combination:
    #attributes of combination
    finalScore = 0
    theNumbers = []
    #methods of combination
    def __init__(self, finalScore, theNumbers):
        self.finalScore = finalScore
        self.theNumbers = theNumbers

#totally stole this. you put a list of numbers in and it returns a list of all combinations
def generate_combinations(numbers):
    all_combinations = []
    for r in range(1, len(numbers) + 1):
        # Generate combinations of length r
        combinations_r = combinations(numbers, r)
        all_combinations.extend(list(combinations_r))   
    return all_combinations
#turns the list of combinations into a list of classes of combinations
#this just adds a sum to make it user frienly...ish
def turnIntoInstancesOfCombinations(list):
    combinationList = []
    for each in list:
        #take the sum of the list and assign it to the final score and then list the numbers. "each" is a list 
        combinationList.append(Combination(sum(each), each))  
    #for each in combinationList:
    #    print(each.finalScore)
    #    print(each.theNumbers)
    return combinationList

'''
this method is going to take a list of "combinations" and sort their final scores
the scores that meet the users goal (or get the closest compared to the rest) should appear at top of list
sorting by list
'''
def sortMyCombos(theCombinations):
    sorted(theCombinations, key=lambda combination: combination.finalScore)
    for each in theCombinations:
        print(each.finalScore)
        print(each.theNumbers)
    return theCombinations

#the main thing
    
#this is the goal we're trying to reach    
goal = input("enter the amount you need in the work orders: ")
#a list to store the numbers of the different lots
numbers = []
#asking to user to enter in all the different lot amounts
print("type in each amount of your lots followed by 'enter'. \nenter 0 again when you're done" )
#this boolean statement will be turned false when the user enters a 0, ending the while loop
gatheringLots = True
#because there are any given number of different lots, a while statement seemed appropriate
while gatheringLots == True:
    #placeholder to save users input to later insert into the list
    nextNumber = input()
    #had to use int method to force input be seen as an integer
    if int(nextNumber) <= 0:
        gatheringLots = False
    else: 
        numbers.append(int(nextNumber))

#print out the list to make sure it works properly
print(numbers)
print("You goal is " + goal + ".")
print(generate_combinations(numbers))
sortMyCombos(turnIntoInstancesOfCombinations(generate_combinations(numbers)))