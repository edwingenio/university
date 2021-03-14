
alphabet = "abcdefghijklmnopqrstuvwxyz"   

test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"] 

test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"] 

# From Section 11.2 of: 

# Downey, A. (2015). Think Python: How to think like a computer scientist. Needham, Massachusetts: Green Tree Press. 
#this is the histogram that creates a dictionary with all the letters used and count on those letters
def histogram(s):
     d = dict()
     for c in s:
          if c not in d:
               d[c] = 1
          else:
               d[c] += 1
     return d
#has_duplicates sends the string to the histogram to get a dictionary abck and loop through it to determine if it has duplicates
def has_duplicates(str):
    histodic=histogram(str)
    keys=histodic.keys()
    for x in keys:
        
        if histodic[x]>1:
            return True
        else:
            return False
#test_dups_print is a function in charge of iterating through the test_dups and send them through has_duplicates which in turn returns false or true, booleans used to determine the print result
def test_dups_print():
    global test_dups
    for x in test_dups:
        if has_duplicates(x)== True:
            print(x+ " has duplicates")
        else:
            print(x+ " has no duplicates")
test_dups_print()
#missing letters takes in a str and turns the alpahabet into a list so it can then be turned into a dict, it iterates throguh the str and logs the letters into the dictionary and then it appends missing letters to a list and then returns a str with results
def missing_letters(str):
    global alphabet
    splited=list(alphabet)
    newdict=dict.fromkeys(splited,0)
    for x in str:
        if x==" ":
            continue
        newVal=newdict[x]+1
        newdict.update({x:newVal})
    missing=[]
    for y in newdict:
        if newdict[y]==0:
            missing.append(y)
    if len(missing)== 0:
        return str+" uses all the letters "
    else:
        return str+" is missing letters "+ "".join(missing)
        

#test_miss_print is in charge of iterating through test_miss and sending the test cases to missing_letters and printing the result 
def test_miss_print():
    global test_miss
    for x in test_miss:
        print(missing_letters(x))
test_miss_print()
