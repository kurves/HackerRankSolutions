def matchingStrings(strings,queries):
    for i in strings:
        for j in queries:
            if strings[i] == queries[j]:
                print(strings[i])
matchingStrings(['ab','ab','abs'],['ab','abc','bc'])