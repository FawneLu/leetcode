### greedy
根据贪心的思想，要把最长的棒留到最后加。  
用一个最小顶堆，每次把最小的两个棒相加的结果push到sticks里， 并叠加到res上。