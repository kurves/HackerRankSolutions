# function to convert from 12 hour to 24hr
def timeConversion(s):
    clocksystem = s[-2:]
    if clocksystem == 'PM':
        clock24 = int(s) + 12
        print(clock24)
    print(tme)
    #if s[-1]

timeConversion("07:05:45PM")