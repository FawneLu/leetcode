class Solution:
    def calculate(self, s: str) -> int:
        pre_op, num ="+", 0
        stack = []
        
        for i, each in enumerate(s):
            
            if each.isdigit():
                num = num*10+int(each)
                
            if i==len(s)-1 or each in "+-*/":
                
                if pre_op == "+":
                    stack.append(num)
                elif pre_op == "-":
                    stack.append(-num)
                elif pre_op == "*":
                    stack.append(stack.pop()*num)
                elif pre_op == "/":
                    top = stack.pop()
                    if top < 0:
                        stack.append(int(top/num))
                    else:
                        stack.append(top//num)
                
                pre_op=each
                num=0
        
        return sum(stack)