def maxSubarray(arr):
    max = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            if sum > max:
                max = sum
    return max