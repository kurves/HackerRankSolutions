def pangrams(s):
    # pangram string that contains every letter of the alphabet
    new_s = ''.join(s.lower().split())
    print(new_s)

    for i in range(ord('a'), ord('z')):
        
        print(chr(i))

        for j in new_s:
            print(j)
            if i == j:
                print('true')
       
      


pangrams('This is a laxy fox dog')