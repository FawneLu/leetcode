### dfs
递归函数增加一个变量，表示当前节点的父亲节点是否用过。根节点没有父亲节点，所以其父亲节点肯定没用过。然后我们判断在某个节点的父亲用过和没用过的情况下，当前节点能不能用，最优的结果分别是多少。