### tricky的一道题
这道题其实很简单，但是为了降低时间复杂度我们需要做的就是找规律。  
用一个dictionary存储每一个cells对应的天数，如果cells在dict里面，正面有循环，那天数对循环次数取余就可以降低时间复杂度。