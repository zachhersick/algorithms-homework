# by Zach Hersick (programmer) and Christian Vaikona (navigator)

def largest_subarray_optimal(nums):
    """
    loops through the list once,
    resetting the start of the returned subarray
    if the sum so far is negative and finishing when it 
    finds the maximum value
    """
    bestSoFar = nums[0]
    bestEndingHere = nums[0]
    for i in range(1, len(nums)):
        if (bestEndingHere < 0):
            bestEndingHere = nums[i]
            if (bestEndingHere > bestSoFar):
                bestSoFar = bestEndingHere
        else:
            bestEndingHere += nums[i]
            if (bestEndingHere > bestSoFar):
                bestSoFar = bestEndingHere
    return bestSoFar

nums = [-3, -1, -2]
print(largest_subarray_optimal(nums))