def matchingStrings(strings,queries):
    matchingMap ={}

    for string in strings:
        if string in matchingMap:
            matchingMap[string] += 1
        else:
            matchingMap[string] = 1
    
       
           
matchingStrings(['ab','ab','abc'],['ab','abc','bc'])