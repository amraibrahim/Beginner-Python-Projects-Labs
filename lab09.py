def makeDictionary(name_list, score_list):
    """    
Function takes two lists and returns a dictionary with the
names as the keys and the scores as the values.
    """
    student_scores = dict()
    for x in range (len(name_list)):
        student_scores[name_list[x]]=score_list[x]
    return student_scores

def getScore (name, dictionary) :
    """
    Function takes a string name and a dictionary as parameters
    and returns the score for that name if it is in the dictionary.
    If the name is not in the cidctionary, return the error message
    "Name not found"
    """

    if name in dictionary:
        return dictionary[name]
    else:
        return 'Name not found'
if __name__ == "__main__": 
    names = ['bart', 'nikki', 'lisa', 'nelson', 'ralph']
    scores = [10,23,13,18,12]
    dic = makeDictionary(names, scores)
    print(getScore('bart', dic))
    print(dic)
              
# Assign the result of makeDictionary to the variable scoreDict
# Using scoreDict, print the score for 'lisa'
# Add a score of 19 for 'maggie' to scoreDict
# Display a sorted list of all the scores in scoreDict
# Calculate the average of all the scores in scoreDict
# Update the score for nelson to be 13
# Nikki has just dropped the course. Delete 'nikki' and their score from
# Print a table of students and their scores with the students listed
# Check the score for Milhouse in scoreDict
# Check the score for Bart in scoreDict