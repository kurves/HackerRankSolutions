#function to look for subset of a set


seta= set(map(int, input().split()))
setb = set(map(int, input().split()))
if seta.issubset(setb):
    print("True")
else:
    print("False")