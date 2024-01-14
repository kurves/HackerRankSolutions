# function to convert from 12 hour to 24hr
def timeConversion(s):
    clocksystem = s[-2:]
    if clocksystem == 'PM':
        clock24 = int(s[:2]) + 12 
        clock245 = str(clock24) + s[2:-2]
        print(clock245)
    elif clocksystem == 'AM':
        clock12 = int(s[:2]) - 12
        fomClock12 = "{:02}".format(clock12)
        clock124 = str(clock12) + s[2:-2]
        print(clock124)

    #if s[-1]

timeConversion("07:05:45PM")
timeConversion("12:01:00AM")