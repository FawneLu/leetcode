- Easy Question
For this question, we only need to know that how many invalid parentheses left in the string.  
1. If we meet the (, then we append it in the stack;
2. If we meet the ), then we decide whether the last parentheses is (.  
1）If so, it proves that the new parenthese has its pair, then we pop the last one.  
2）If not, we append the ) in the stack.
