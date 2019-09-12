For this question, we use a stack to store every char in the string. 
If we meet C, we pop the last element in the stack. If we meet D, we append stack[-1]*2.
If we meet +, we append the sum of last two elements.
Else, we append char in the stack.
Lastly, we return the sum of the stack.