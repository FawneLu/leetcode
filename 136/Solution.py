class Solution:
    def singleNumber(self, nums: List[int]) -> int:  
         nums_dict = {}  
         for num in nums:  
             if num not in nums_dict:  
                 nums_dict[num] = 1  
             else:  
                 nums_dict[num] += 1  
