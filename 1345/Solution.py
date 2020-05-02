class Solution:
    def minJumps(self, arr: List[int]) -> int:
        queue=collections.deque()
        dic=collections.defaultdict(list)
        for i,x in enumerate(arr):
            if (i and arr[i-1]!=arr[i]) or (i!=len(arr)-1 and arr[i+1]!=arr[i]):
                dic[x].append(i)
        
        queue.append([0,0])
        visited=set([0])
        
        while queue:
            pos,step=queue.popleft()
            
            if pos==len(arr)-1:
                return step
            
            for p in [pos-1,pos+1]+dic[arr[pos]]:
                if p not in visited and len(arr)>p>=0:
                    queue.append([p,step+1])
                    visited.add(p)