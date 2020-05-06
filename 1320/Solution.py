class Solution:
    def minimumDistance(self, word: str) -> int:
        if len(word)==2:
            return 0
        
        pos={}
        ch=ord('A')
        for i in range(5):
            for j in range(6):
                pos[chr(ch)]=(i,j)
                if ch==ord('Z'):
                    break
                ch+=1
        
        def distance(f1,f2):
            if f1==None:
                return 0
            return abs(pos[f1][0]-pos[f2][0])+abs(pos[f1][1]-pos[f2][1])
        
        mapx={}
        mapx[(word[0],None)]=0
        
        for cur in word[1:]:
            new_mapx={}
            for f1,f2 in mapx:   
                state1=(f1,cur)
                state2=(cur,f2)
                dis1=distance(f2,cur)
                dis2=distance(f1,cur)
                for new_state,dis in ((state1,dis1),(state2,dis2)):
                    if new_state not in new_mapx:
                        new_mapx[new_state]=mapx[(f1,f2)]+dis
                    else:
                        new_mapx[new_state]=min(mapx[(f1,f2)]+dis,new_mapx[new_state])
            mapx=new_mapx
        
        return min(mapx.values())