class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start=newInterval[0]
        end=newInterval[1]
        
        left,right=[],[]
        
        for interval in intervals:
            if interval[1]<start:
                left.append(interval)
            elif interval[0]>end:
                right.append(interval)
            else:
                start=min(start,interval[0])
                end=max(end,interval[1])
        
        return left+[[start,end]]+right