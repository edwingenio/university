path=r"C:\Users\Owner\Documents\University\CS1101\input-file-7.txt"
dictionary={}
with open(path, "r") as f:
    current=f.readlines()
    for line in current:
        templs=line.strip().split(",")
        newls=[templs[1],templs[2]]
        dictionary[templs[0]]=newls

    
# From Section 11.5 of: 
# Downey, A. (2015). Think Python: How to think like a computer scientist. Needham, Massachusetts: Green Tree Press. 
#In here we invert the key for the values and make sure that each element of the list has its own reference to the same value which used to be the key 
def invert_dict(d):
     inverse = dict()
     for key in d:
          val = d[key]
          for x in val:
              inverse[x]=key
          
     return inverse 
inverted=invert_dict(dictionary)

    
print(list(inverted))
with open(r"C:\Users\Owner\Documents\University\CS1101\output-file-7.txt","w") as out:
    for key in inverted:
        out.write(f"{key}:{inverted[key]}\n")
        print("This is the old dict ", dictionary)
        print("This is the new dict ",invert_dict(dictionary))
