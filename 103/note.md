### BFS
BFS就是用queue。  
用两个数组node和level, node用来存放node节点, level用来存放每一层的值, oredrleft用来判断是从左到右还是从右到左。  
每次从node里popleft一个节点, 如果不为空就判断是不是orderleft, 是的话就append, 不是的话就appendleft, 然后把左右子树append到node里。  
用一个None来判断当前level是否遍历完。  
如果当前节点是None, orderleft= not orderleft, res.append(level), level=deque(), 如果node不为空, 则在append一个None