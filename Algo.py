def maxSubarray(arr): # complexity : O(n^2)
    max = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i,len(arr)):
            sum += arr[j]
            if sum > max:
                max = sum
    return max

if __name__ == "__main__":
    a = [1,-3,2,1,-1]
    print(maxSubarray(a))