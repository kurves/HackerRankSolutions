def matchingStrings(strings,queries):
    listResults = [strings.count(x) for x in queries]
    print(listResults)
       
    
       
           
matchingStrings(['ab','ab','abc'],['ab','abc','bc'])