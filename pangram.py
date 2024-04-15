def pangrams(s):
    # pangram string that contains every letter of the alphabet
    new_s = ''.join(s.lower().split())
    char = set(s)

    if  len(char) == 26:
        print('pangram')
    else:
        print('not pangram ')
       
       
      


pangrams('This is a laxy fox dog')