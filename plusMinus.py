def plusMinus(arr):
    """funcion to calculate the ratios of integers that are positive negative and zero"""
    numElements = len(arr)
    posNumberAve = len([ i for i in arr if i >0]) / numElements
    negNumberAve = len([i for i in arr if i < 0]) / numElements
    zeroNumberAve = len([i for i in arr if i ==0])  / numElements
    print(posNumber)
    print(negNumber)
    print(zeroNumber)
    print(numElements)

plusMinus([1,2,3, -5, -6, 0, 0])