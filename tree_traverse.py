#递归
##前序
def recursion_preorder(self,node):
	if not node:
		return
	else:
		print(node.elem,end=' , ')
	    self.recursion_preorder(node.left)
	    self.recursion_preorder(node.right)

##中序
def recursion_inorder(self,node):
	if not node:
		return
	else:
		self.recursion_inorder(node.left)
		print(node.elem,end=' , ')
		self.recursion_inorder(node.right)

##后序
def recursion_postorder(self,node):
	if not node:
		return
	else:
		self.recursion_postorder(node.left)
		self.recursion_postorder(node.right)
		print(node.elem,end=' , ')

#非递归
##前序
def nonrecursion_preorder(self,node):
	if not node:
		return
	
	stack.append(node)
	while stack:
		curr_node=stack.pop()
		if not curr_node:
			continue
		else:
			print(curr_node,end=' ')
			stack.append(node.right)
			stack.append(node.left)


def nonrecursion_preorder(self,node):
	if not node:
		return

	stack=[]
	while stack or node:
		while node:
			print(node,end=' , ')
			stack.append(node)
			node=node.left

		node=stack.pop()
		node=node.right

##中序遍历
def nonrecursion_inorder(self,node):
	if not node:
		return

	while stack or node:
		while node:
			stack.append(node)
			node=node.left

		node=stack.pop()
		print(node,end=' , ')
		node=node.right

##后序遍历
def nonrecursion_postorder(self,node):
	if not node:
		return

	stack,res,last_visit=[],[],None
	while stack or node:
		while node:
			stack.append(node)
			node=node.left

		curr_node=stack[-1]
		if not curr_node.right or curr_node.right==last_visit:
			item=stack.pop()
			res.append(item.value)
			last_visit=item

		elif curr_node.right:
			node=curr_node.right

	return res


























