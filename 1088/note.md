### confusion number 2
backtrack。  
我们每次对函数传入三个参数（判断的数字num，rotation的数字rotation，位数digits）  
- 如果num!=rotation, 证明满足confusion number的条件，则count+1；  
- 否则继续判断下一个合法的数，例如，1之后就判断10，6之后就判断60。  
- 如果num* 10+i>N,则要break
- 注意继续进行backtrack的时候num=num* 10+i(i为合法的数)。rotation的数字则为i对应的rotation的数字乘以当前位数加上rotation；
- digits* 10  
计算backtrack(1,1,10),(6,9,10),(8,8,10),(9,6,10)