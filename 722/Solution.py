# 722 Remove Comments
def removeComments(self, source: List[str]) -> List[str]:
    flag = False #代表是不是block
    res = [] # 每一行的元素
    line = ""
    for s in source: # 岁每一个元素都要进行循环
        i = 0
        while i < len(s):
            if not flag:
                if s[i] == "/" and i < len(s)-1 and s[i+1] =="*":
                    flag = True
                    i += 1
                elif s[i] == "/" and i < len(s)-1 and s[i+1] =="/":
                    break
                else:
                    line += s[i]
            
            else:
                if s[i] == "*" and i < len(s)-1 and s[i+1] =="/":
                    flag = False
                    i += 1
            
            i += 1
            
        
        if not flag and line:
            res.append(line)
            line = ""
    
    return res

#Time Complexity:O(len(source))
#Space Complexity:O(len(source))