"""
Problem 1 (20):
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. 
In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

Constraints: 
nums[i] != nums[i + 1] for all valid i. (that means two consecutive numbers are never same)
Your program should contain a function that takes in the input (list of numbers) and returns the output (index of a peak).
"""
def find_peak_element(nums):
    low = 0
    high = len(nums)-1
    while (low < high):
        mid = low + (high - low)//2
        if (nums[mid] < nums[mid+1]):
            low = mid + 1
        else:
            high = mid
    return high
            
        
nums = [7]
result = find_peak_element(nums)
print("index: " + str(result))
print("value: " + str(nums[result]))
print("--------------------------------------")

nums = [1, 2]
result = find_peak_element(nums)
print("index: " + str(result))
print("value: " + str(nums[result]))
print("--------------------------------------")

nums = [2, 1]
result = find_peak_element(nums)
print("index: " + str(result))
print("value: " + str(nums[result]))
print("--------------------------------------")

nums = [1, 3, 2]
result = find_peak_element(nums)
print("index: " + str(result))
print("value: " + str(nums[result]))
print("--------------------------------------")

nums = [1, 4, 7, 6, 3, 2]
result = find_peak_element(nums)
print("index: " + str(result))
print("value: " + str(nums[result]))
    
