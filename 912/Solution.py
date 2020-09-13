class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
            
        def mergesort(nums):
            if len(nums) == 1 or not nums:
                return nums
            
            def helper(n1, n2):
                new_nums = []
                i, j = 0, 0
                while i < len(n1) and j < len(n2):
                    if n1[i] < n2[j]:
                        new_nums.append(n1[i])
                        i += 1
                    else:
                        new_nums.append(n2[j])
                        j += 1
                if i < len(n1):
                    new_nums += n1[i:]
                if j < len(n2):
                    new_nums += n2[j:]

                return new_nums
        
            return helper(mergesort(nums[:len(nums)//2]),mergesort(nums[len(nums)//2:]))
        
        return mergesort(nums)
        
                
                
    
    
    def sortArray1(self, nums: List[int]) -> List[int]:
        def partition(nums, left, right):
            pivot_val = nums[right]
            #nums[left], nums[right] = nums[right], nums[left]
            i, j = left, right - 1
            while i <= j:
                if nums[i] >= pivot_val:
                    nums[i], nums[j] = nums[j], nums[i]
                    j -= 1
                else:
                    i += 1
            
            nums[i], nums[right] = nums[right], nums[i]
            #print(nums)
            return i
            
        def partition1(nums, left, right):
            pivot_index = left
            pivot_val = nums[left]
            while left < right:
                while left < right and nums[right] >= pivot_val:
                    right -= 1
                while left < right and nums[left] <= pivot_val:
                    left += 1
                nums[left], nums[right] = nums[right], nums[left]

            nums[left], nums[pivot_index] = nums[pivot_index], nums[left]
            return left
        
        def quicksort(nums, left, right):
            if left >= right:
                return
            pivot = partition(nums, left, right)
            quicksort(nums, left, pivot-1)
            quicksort(nums, pivot+1, right)
            
            
        quicksort(nums, 0, len(nums)-1)
        return nums