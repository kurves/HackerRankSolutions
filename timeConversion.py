# function to convert from 12 hour to 24hr
def timeConversion(s):
    clocksystem = s[-2:]
    if clocksystem == 'PM':
        clock24 = int(s[:2]) + 12 
        clock245 = str(clock24) + s[2:-2]
        print(clock24, clock245)
    print(clocksystem)
    #if s[-1]

timeConversion("07:05:45PM")