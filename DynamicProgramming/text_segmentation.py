# Input: A sequence of letters
# output: yes if it can be split into words, no otherwise

def isWord(string : str) -> bool:
    """ returns whether given string is a valid word"""
    return string in ["but","butt","butter","utter","fly"]
    
# recursion
#                       _
#                      |  True    if string is empty
# splittable(string) = |  True    if splittable(string[j:]) and string[:j] is a valid word
#                      |_ False   Otherwise
#                     

def splittable(string:str) -> bool:
    """returns true if the string can be segmented into meaningful words"""
    if not string: return True
    # check if the string can be splitted into meaningful words
    for j in range(1,string.__len__()+1):
        if splittable(string[j:]) and isWord(string[:j]):
            return True
    # if no good split is possible
    return False

# recursion
#                        _    
#                       |  True   if i>n-1
# splittable_util(i) =  |  True   if splittable_util(j) and isword(string[i:j])
#                       |_ False  otherwise


def splittable2(string: str) -> bool:
    """returns true if the string can be segmented into meaningful words"""
    length = string.__len__()
    def splittable_util(i:int) -> bool:
        """returns true if the string[i:] is splittable"""
        nonlocal string, length

        if i == length: return True

        for j in range(i,length):
            if splittable_util(j+1) and isWord(string[i:j+1]):
                return True
        return False
    return splittable_util(0)

# dynamic programming
# We need to understand what we are repeating, and how to store it
# for each i, we would be interested in finding splittable[j] where j>i
# We need not find it over and over again
# We can create a table (1d array) of size n+1 which contains
# the boolean value whether the substring after that is splittable or not

def dp(string: str)-> bool:
    """returns true if string can be separated into meaningful words"""
    length = string.__len__()
    table = [False]*(length+1)
    table[length] = True

    def splittable_util(i: int)->bool:
        nonlocal length, table, string
        for j in range(i,length):
            if table[j+1] and isWord(string[i:j+1]):
                table[i] = True
                break
    for i in range(length-1,-1,-1):
        splittable_util(i)
    return table[0]

if __name__ == "__main__":
    string = "butterfly"
    print(splittable2(string))
    print(dp(string))

        
        
        
