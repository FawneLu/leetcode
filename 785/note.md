### 利用BFS的思路给点染色
使用一个visited数组来保存每个节点被染的颜色。0代表没染色，1代表染成蓝色，2代表染成红色。对图的每个顶点进行一个遍历，把和这个顶点相邻的顶点全部染成相反的颜色。如果相邻顶点已经染色，而且染色和当前顶点染色相同，则返回False。全部成功染色后返回True。