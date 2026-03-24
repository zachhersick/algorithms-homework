# by Zach Hersick (navigator) and Christian Vaikona (programmer)

def interval_scheduling_optimal(nums):
    """
    sorts the list by end value of the interval,
    then sums the amount of intervals whose start value
    is greater than the end value of the previous index
    returns the number of non-overlapping intervals
    """
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