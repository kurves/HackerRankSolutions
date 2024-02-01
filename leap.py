    
def leap(year):
    div_4 = (year % 4 == 0)
    div_100 = (year % 100 == 0)
    div_400 = (year % 400 == 0)
    if div_4 and (div_400 or not div_100):
        print("t")
        return True
    elif div_4 and div_100:
        print("f")
    elif div_400 and (div_4):
        print("t")
    else:
        print("f")
        return False

        

leap(2400)
    



    



