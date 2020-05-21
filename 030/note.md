### 滑动窗口
先搞一个words的字典word_dic，记录words。  
然后利用一个大小为k滑动窗口在s里进行遍历，并用一个cur_dic记录遍历的word。  
如果cur_word不在word_dic里，直接略过，如果在的话再对cur_dic进行操作。  
每对一个起始位置i进行遍历的最后要比较cur_dic和word_dic，看是否超出范围。