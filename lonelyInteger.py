def lonelyInteger(a):
    for i in a:
        n = a.count(i)
        if n == 1:
            print(i)
      

    

lonelyInteger([1,2,3,4,3,2,1])    