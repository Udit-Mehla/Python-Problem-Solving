# Problem: Two Sum
# Link: https://leetcode.com/problems/two-sum/

def twoSum(nums, target):
    prev_map = {}  # Our notebook
    
    # range(len(nums)) gives us [0, 1, 2, .so on]
    for i in range(len(nums)):
        n = nums[i]           # Manually grab the number at index i
        diff = target - n     # Calculate what we need
        
        if diff in prev_map:
            return [prev_map[diff], i]
        
        prev_map[n] = i       # Store number:index in our notebook

#Let Assume We Have
nums=[2,4,6,77,36,20]
target=10
result= twoSum(nums,target)
print(f'the value will be {result}')