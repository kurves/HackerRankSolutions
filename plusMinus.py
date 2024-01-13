def plusMinus(arr):
    """funcion to calculate the ratios of integers that are positive negative and zero"""
    numElements = len(arr)
    posNumberAve = len([ i for i in arr if i >0]) / numElements
    negNumberAve = len([i for i in arr if i < 0]) / numElements
    zeroNumberAve = len([i for i in arr if i ==0])  / numElements
    print(f"{posNumberAve:.6f}")
    print(f"{negNumberAve:.6f}")
    print(f"{zeroNumberAve:.6f}")
 

plusMinus([1,1,0,-1,-1])