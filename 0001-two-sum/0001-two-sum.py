class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}  # Dictionary to store numbers and their indices: {num: index}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # If the complement is already in our dictionary, we found our pair!
            if complement in seen:
                return [seen[complement], i]
            
            # Otherwise, add the current number and its index to the dictionary
            seen[num] = i