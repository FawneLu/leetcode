### BST
返回K个离target最近的点。用BST的性质，如果res为空就把root.val添加进去，否则判断res的第一个点的大小和root.val的大小。如果大于，就把第一个点pop出来，再把最后一个点添加进去。