class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words)==0:
            return []
        word_dic={}
        for word in words:
            if word not in word_dic:
                word_dic[word]=1
            else:
                word_dic[word]+=1
        
        n,m,k=len(s),len(words[0]),len(words)
        res=[]
        
        for i in range(n-m*k+1):
            j=0
            cur_dic={}
            while j<k:
                cur_word = s[i+j*m:i+j*m+m]
                if cur_word not in word_dic:
                    break
                if cur_word not in cur_dic:
                    cur_dic[cur_word]=1
                else:
                    cur_dic[cur_word]+=1
                
                
                if cur_dic[cur_word]>word_dic[cur_word]:
                    break
                j+=1
            
            if j==k:
                res.append(i)
        
        return res