from collections import Counter
def matchingStrings(strings,queries):
    counts  ={}
    for i in strings:
        if i in queries:
            print(i)
            c = strings.count(i)
        print(c)
       
           
matchingStrings(['ab','ab','abc'],['ab','abc','bc'])