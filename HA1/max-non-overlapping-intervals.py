def max_non_overlapping_intervals(nums):
    
    def build_subsets(current_index, current_subset):
        if current_index == len(nums):
            sorted_subset = sorted(current_subset, key=lambda nums: nums[0])
            for i in range(len(sorted_subset)-1):
                if sorted_subset[i][1] > sorted_subset[i+1][0]:
                    return 0
            return len(current_subset)
        
        include_result = build_subsets(current_index+1, current_subset + [nums[current_index]])
        
        exclude_result = build_subsets(current_index+1, current_subset)
        
        return max(include_result, exclude_result)
        
    return build_subsets(0, [])

nums = [(1,3), (3,5), (5,7), (2,4)]
print(max_non_overlapping_intervals(nums))
            