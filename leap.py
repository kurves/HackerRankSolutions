    
def leap(year):
    div_4 = (year % 4 == 0)
    div_100 = (year % 100 == 0)
    div_400 = (year % 400 == 0)
    if div_4 and (div_400 or div_100):
        return True
    else:
        return False

        

leap(1990)
    



    



