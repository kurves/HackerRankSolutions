from collections import Counter
def matchingStrings(strings,queries):
    counts  ={}
    for i in strings:
        if i in counts:
            count = queries.count(i)
            counts[i] += count
            print(count)
       
           
matchingStrings(['ab','ab','abc'],['ab','abc','bc'])