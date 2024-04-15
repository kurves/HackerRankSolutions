def pangrams(s):
    # pangram string that contains every letter of the alphabet
    new_s = ''.join(s.lower().split())
    char = set(s)

    for i in range(ord('a'), ord('z') + 1):
        for j in new_s:
            if chr(i) == j:
                print('true')
       
      


pangrams('This is a laxy fox dog')