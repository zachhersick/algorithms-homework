def largest_subarray(nums):
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
    print(sums)
    return max(sums.values())

nums = [1, -2, 3, 4, 5, -6]
print(largest_subarray(nums))