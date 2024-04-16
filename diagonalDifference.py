def diagonalDifference(arr):
    """function to get diagonal difference of left-right and rigth-left"""

    left_diagonal_sum =0
    right_diagonal_sum =0

    for i in range(len(arr)):
        left_diagonal_sum += arr[i][i]

        right_diagonal_sum += arr[i][len(arr) - i - 1]

        diagonal_difference = abs(left_diagonal_sum - right_diagonal_sum)

        return diagonal_difference