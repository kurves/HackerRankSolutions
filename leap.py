    
def leap(year):
    div_4 = year/4 == 0
    div_100 = year/ 100 == 0
    div_400 = year /400 ==0 
    
    if div_4  and div_400 and not div_100:
        print("t")
    elif div_4 or div_400:
        print("t")
    elif div_4 and div_100:
        print("f")
    
    
leap(2000)

