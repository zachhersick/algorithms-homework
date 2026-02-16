def largest_subarray_optimal(nums):
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