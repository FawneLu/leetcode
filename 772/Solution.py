class Solution:
    def calculate(self, s: str) -> int:
        s=s+'$'
        def helper(stack,i):
            num = 0
            pre_op = '+'
            while i<len(s):
                c=s[i]
                if c ==' ':
                    i+=1
                    continue
                    
                elif c.isdigit():
                    num = num*10+int(c)
                    i+=1
                    
                elif c == '(':
                    num,i = helper([] , i+1)
                
                else:
                    if pre_op == '+':
                        stack.append(num)
                    if pre_op == '-':
                        stack.append(-num)
                    if pre_op == '*':
                        stack.append(stack.pop()*num)
                    if pre_op == '/':
                        top=stack.pop()
                        if top<0:
                            stack.append(int(top/num))
                        else:
                            stack.append(top//num)
                    num = 0
                    i += 1
                    
                    if c == ')':
                        return sum(stack),i
                    
                    pre_op=c
            return sum(stack)
            
        return helper([],0)