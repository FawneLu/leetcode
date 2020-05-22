### string乘法
两个string相乘，不能强制转型。  
就按照乘法特性，从后往前，每次用num2的一位乘以num1，用first和second记录两数相乘的第一位和第二位，pre用来记录进位，cur用来记录当前的和。  