def interval_scheduling_optimal(nums):
    nums_sorted = sorted(nums, key=lambda x: x[1])
    last_end_time = nums_sorted[0][1] 
    sum = 1
    for i in range(1, len(nums_sorted)):
        if nums_sorted[i][0] >= last_end_time:
            last_end_time = nums_sorted[i][1]
            sum +=1
    return sum

nums = [(1,10), (2,3), (3,4), (4,5)]
print(interval_scheduling_optimal(nums))