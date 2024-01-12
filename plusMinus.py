def plusMinus(arr):
    """funcion to calculate the ratios of integers that are positive negative and zero"""
    numElements = len(arr)
    posNumber = len([ i for i in arr if i >0])
    negNumber = len([i for i in arr if i < 0])
    zeroNumber = len([i for i in arr if i ==0])
    print(posNumber)
    print(numElements)

plusMinus([1,2,3])