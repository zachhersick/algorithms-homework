# by Zach Hersick (navigator) and Christian Vaikona (programmer)

def largest_subarray(nums):
    """
    uses nested loops to double loop through the list,
    check all possible subarrays, then finds the maximum
    subarray value
    """
    sums = {}
    for i in range(0, len(nums)):
        subarray = []
        sum = nums[i]
        subarray.append(nums[i])
        sums[tuple(subarray)] = (sum)
        for j in range(i+1, len(nums)):
            sum += nums[j]
            subarray.append(nums[j])
            sums[tuple(subarray)] = sum
    return max(sums.values())

nums = [1, -2, 3, 4, 5, -6]
print(largest_subarray(nums))