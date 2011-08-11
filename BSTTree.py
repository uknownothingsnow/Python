class Node:
	"node fo tree"
	def __init__(self,data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right
	
class Tree:
	"tree definition"
	def __init__(self, node=None):
		self.root = node
	
	def left_insert_node(self, node):
		if self.root is None:
			self.root = node
		else:
			node.left = self.root.left
			self.root.left = node
	
	def insert(self, value):
		if self.root is None:
			self.root = Node(value)
		else:
			node = self.root
			parent = node
			while(node is not None):
				if(value < node.data):
					parent = node
					node = node.left
				else: 
					if(value > node.data):
						parent = node
						node = node.right
			if(value < parent.data): 
				parent.left = Node(value)
			else:
				parent.right = Node(value)

	def delete(self, key):
		self.__search_binary_tree_delete(self.root, key)

	def __search_binary_tree_delete(self, node, key):
		if key < node.data:
			self.__search_binary_tree_delete(node.left, key)
		elif key > node.data:
			self.__search_binary_tree_delete(node.right, key)
		else:
			if node.left and node.right:
				successor = self.__find_mini_right(node)
				node.data = successor[1].data
				if(successor[1].right is not None):
					successor[0].left = successor[1].right
			elif node.left or node.right:
				parent = self.__get_parent(self.root, node)
				if(parent.left and parent.left.data == key):
					parent.left = (node.left or node.right)
				else:
					parent.right = (node.left or node.right)
			else:
				parent = self.__get_parent(self.root, node)
				if(parent.left and parent.left.data == key):
					parent.left = None
				else:
					parent.right = None
				
	def __find_mini_right(self, node):
		temp = node
		while temp and temp.left:
			if temp.left.data == node.data:
				return (node, temp)
			temp = temp.left
	
	def __get_parent(self, start, node):
		if((start.left and start.left.data == node.data) or (start.right and start.right.data == node.data)):
			return start
		elif(node.data < start.data):
			return self.__get_parent(start.left,node)
		else:
			return self.__get_parent(start.right, node)

	def search_binary_tree(self,key):
		if(self.root is not None):
			return self.__search_binary_tree(self.root, key)
	def __search_binary_tree(self, node, key):
		if(node is None):
			return None
		elif key == node.data:
			return node.data
		else:
			return (key < node.data and  self.__search_binary_tree(node.left, key) or self.__search_binary_tree(node.right, key))

	def traverse(self):
		self.__traverse(self.root)

	def __traverse(self, node):
		if(node is not None):
			print node.data
			if(node.left is not None):
				self.__traverse(node.left)
			if(node.right is not None):
				self.__traverse(node.right)

if __name__ == "__main__":
	node = Node(4)
	tree = Tree(node)
	#print tree.root.data
	#tree.left_insert_node(Node(2))
	tree.insert(2)
	#print tree.root.left.data
	#tree.left_insert_node(Node(3))
	tree.insert(5)
	#print tree.root.left.data
	tree.insert(1)
	tree.insert(6)
	tree.insert(3)
	tree.traverse()
	ret = tree.search_binary_tree(3)
	if(ret is not None):
		print "3 find in binary search tree"
	tree.insert(7)
	tree.traverse()
	tree.delete(7)
	tree.traverse()
