#function to look for subset of a set


seta= set(map(int, input).split())
setb = set(map(int, input).split())
if seta.issubset(b):
    print("True")
else:
    print("False")