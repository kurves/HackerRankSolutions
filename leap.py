    
def leap(year):
    div_4 = (year % 4 == 0)
    div_100 = (year % 100 == 0)
    div_400 = (year % 400 == 0)
    if div_4 and (div_400 or not div_100):
        return True
    elif div_4 and div_100:
        return False
    elif div_400 and (div_4):
        return True
        
    else:
       
        return False

        

leap(2400)
    



    



