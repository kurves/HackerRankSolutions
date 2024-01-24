    
def leap(year):
    div_4 = year/4 == 0
    div_100 = year/ 100 == 0
    div_400 = year /400 ==0 
    
    if div_4 and not div_100 and div_400:
        print("t")
        return True
    else:
        print("f")
        return False
    
leap(2000)

