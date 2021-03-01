class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        def dfs(kill_id, hashmap, res):
            res.append(kill_id)
            for child in hashmap[kill_id]:
                dfs(child, hashmap, res)
        
        hashmap = collections.defaultdict(set)
        res = []
        
        for i in range(len(pid)):
            hashmap[ppid[i]].add(pid[i])
        dfs(kill, hashmap, res)
        
        return res