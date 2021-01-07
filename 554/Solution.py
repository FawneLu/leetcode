import collections
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        left_counter = collections.Counter()
        count = 0
        
        for bricks in wall:
            left = 0
            for brick in bricks[:-1]:
                left += brick
                left_counter.update([left])
                count = max(count, left_counter[left])
        
        return len(wall) - count