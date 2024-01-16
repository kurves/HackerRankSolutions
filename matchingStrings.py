from collections import Counter
def matchingStrings(strings,queries):
    counts  ={}
    for i in queries:
        if i in strings:
            c = strings.count(i)
            print(c)
        elif i not in strings:
            c = 0    
    
       
           
matchingStrings(['ab','ab','abc'],['ab','abc','bc'])