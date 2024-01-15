from collections import Counter
def matchingStrings(strings,queries):
    counts  ={}
    for i in strings:
        if i in  queries:
            counts[i] += 1
        else:
            print(counts =0)
           
matchingStrings(['ab','ab','abc'],['ab','abc','bc'])