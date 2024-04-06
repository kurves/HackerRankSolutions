def matchingStrings(strings,queries):
    matchingMap ={}

    for string in strings:
        if string in matchingMap:
            matchingMap[string] += 1
        else:
            matchingMap[string] = 1
    results =[]

    for query in queries:
        if query in matchingMap:
            results.append(matchingMap[query])
        else:
            results.append(0)

    return results
    
       
           
matchingStrings(['ab','ab','abc'],['ab','abc','bc'])