# function to convert from 12 hour to 24hr
def timeConversion(s):
    clocksystem = s[-2:]
    if clocksystem == 'PM' and s[:2] != "12":
        clock24 = int(s[:2]) + 12 
        clock245 = str(clock24) + s[2:-2]
        return clock245
    elif clocksystem == 'AM' and s[:2] == '12':
        clock12 = int(s[:2]) - 12
        fomClock12 = "{:02}".format(clock12)
        clock124 = str(fomClock12) + s[2:-2]
        return clock124
    elif s[:2] == '12':
        return s[:-2]
    elif clocksystem == 'AM' and int(s[:2]) < 12:
        return s[:-2]
  

  

timeConversion("07:05:45PM")
timeConversion("12:01:00AM")
timeConversion("12:01:00PM")
timeConversion("06:40:03AM")