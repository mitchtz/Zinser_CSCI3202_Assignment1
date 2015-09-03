#Mitch Zinser
#Assignment 1 for CSCI 3203 - Intro to Artificial Intelligence
import random
import queue
'''Problem 1'''
#Create custom queue class (FIFO)
class custom_queue:
	#Initialize the object with an empty queue
	def __init__(self):
		self.q = queue.Queue()
	#Push a number onto the queue, turn number into an int if it isn't already
	def push(self, num_in):
		self.q.put(int(num_in))
	#Pop a number off the queue if not empty
	def pop(self):
		#If queue isn't empty, pop off an item
		if not self.q.empty():
			return self.q.get()
'''Problem 2'''
#Create custom stack using a list (LIFO)
class custom_stack:
	#Initialize the object with an empty stack
	def __init__(self):
		self.stack = []
	#Push an integer onto the stack, if not an int, make input an int
	def push(self, num_in):
		self.stack.insert(0, int(num_in))
	#Pop the last input number off the stack if possible
	def pop(self):
		if len(self.stack) > 0:
			#Get number on top of stack
			num_out = self.stack[0]
			#Remove first item from list
			self.stack = self.stack[1:]
			return num_out
	#Return the size of the stack
	def checkSize(self):
		return len(self.stack)


'''Problem 3'''
class custom_node():
	#Initialization, takes in key value and parent value
	def __init__(self, value, parent):
		self.key = value
		self.left = None
		self.right = None
		self.parent = parent
	#Function to set key value
	def set_key(self, value):
		self.key = value
	#Function to set right child, takes in node to be set as child
	def set_right_child(self, child):
		self.right = child
	#Function to set left child, takes in node to be set as child
	def set_left_child(self, child):
		self.left = child
	#Function to get node value
	def get_key(self):
		return self.key
	#Function to get children and parent nodes
	def get_left_child(self):
		return self.left
	def get_right_child(self):
		return self.right
	def get_parent(self):
		return self.parent
class custom_tree():
	#Initialization, takes in root node value
	def __init__(self, value):
		self.root = custom_node(value,None)
	#Function to add a node, takes in value to add to parentValue
	#Add to left child of parentValue first, then right. If full, don't add. If parentValue not found, don't add
	def add(self, value, parentValue):
		#Look for node in the tree
		#Store all nodes in a row
		row = [self.root]
		cur_node = None
		done = False
		#Check if root is desired ParentValue
		if self.root.get_key() == parentValue:
			cur_node = self.root
			done = True
		#Otherwise run the breadth first search
		while not done:
			#Build list of children of previously searched row
			children = []
			for i in row:
				#Get left child if it exists
				if i.get_left_child() != None:
					children.append(i.get_left_child())
				#Get right child if it exists
				if i.get_right_child() != None:
					children.append(i.get_right_child())
			#Set children as current row to search
			row = children
			#Look through row for desired parentNode key value
			for i in row:
				#If the key is correct, set cur_node as node and mark done
				if i.get_key() == parentValue:
					cur_node = i
					done = True
			#Check if the row is empty, which means tree was exhausted with no solution
			if len(row) == 0:
				cur_node = None
				done = True
		#Now cur_node should have the desired node with parentValue, or will be None if the node wasn't found
		#If cur_node is None, parent couldn't be found
		if cur_node == None:
			print("Parent not found")
		#If the node has no left child, add node to the left
		elif cur_node.get_left_child() == None:
			cur_node.set_left_child(custom_node(value,cur_node))
		#If the node has a left child but no right child, add node to the right
		elif cur_node.get_right_child() == None:
			cur_node.set_right_child(custom_node(value,cur_node))
		#Otherwise the parent node has both children
		else:
			print("Parent has two children, node not added")
	#Function to delete a node, takes in value of node to delete
	#Only delete if node has no children
	def delete(self, value):
		#Look for node in the tree
		#Store all nodes in a row
		row = [self.root]
		cur_node = None
		done = False
		#Check if root is desired ParentValue
		if self.root.get_key() == value:
			cur_node = self.root
			done = True
		#Otherwise run the breadth first search
		while not done:
			#Build list of children of previously searched row
			children = []
			for i in row:
				#Get left child if it exists
				if i.get_left_child() != None:
					children.append(i.get_left_child())
				#Get right child if it exists
				if i.get_right_child() != None:
					children.append(i.get_right_child())
			#Set children as current row to search
			row = children
			#Look through row for desired parentNode key value
			for i in row:
				#If the key is correct, set cur_node as node and mark done
				if i.get_key() == value:
					cur_node = i
					done = True
			#Check if the row is empty, which means tree was exhausted with no solution
			if len(row) == 0:
				cur_node = None
				done = True
		#Now cur_node should have the desired node with value
		#Check if node was found
		if cur_node == None:
			print("Node not found")
		#Then check if node has no children, if so, delete node by removing from child list of parent
		elif (cur_node.get_left_child() == None) and (cur_node.get_right_child() == None):
			#Remove node from parent, check if node is left child, if so, reset parent left child to None
			if cur_node.get_parent().get_left_child() == cur_node:
				cur_node.get_parent().set_left_child(None)
			#Otherwise node is right child of parent:
			else:
				cur_node.get_parent().set_right_child(None)
		#Else the node has children
		else:
			print("Node not deleted, has children")

	#Function to print the tree, print in format of parent value:left child value, right child value
	def print_tree(self, node = None):
		#Reassign node as root if none passed in
		if node == None:
			node = self.root
		#Depth first, left child first
		#Check if left child exists, if not print None
		if node.get_left_child() == None:
			left_child = None
		else:
			left_child = node.get_left_child().get_key()
		#Check if right child exists, if not print None
		if node.get_right_child() == None:
			right_child = None
		else:
			right_child = node.get_right_child().get_key()
		#Print out data
		print(node.get_key(),":",left_child,",",right_child)
		#Recursively call on left child if it exists
		if left_child != None:
			self.print_tree(node.get_left_child())
		#Call recursively on right child if it exists
		if right_child != None:
			self.print_tree(node.get_right_child())

'''Problem 4'''
#Custom graph, unweighted, using a dictionary to store data
class custom_graph():
	#Initialize with an empty dictionary
	def __init__(self):
		self.dict = {}
	#Function to add a vertex, checks to see if node exists already, if not, adds it
	def addVertex(self, value):
		#Check if vertex already exist
		if value in self.dict:
			print("Vertex already exists")
		#If vertex doesn't exist, initialize (to None)
		else:
			self.dict[value] = None
	#Function to add en edge between two vertices
	def addEdge(self, value1, value2):
		#Check if both entries exist
		if (value1 in self.dict) and (value2 in self.dict):
			#Add edges to both entries
			#If this is the first edge for value`
			if self.dict[value1] == None:
				#Add edge from value1 to value2
				self.dict[value1] = [value2]
			else:
				#Add edge from value1 to value2
				self.dict[value1].append(value2)
			#If this is the first edge for value2
			if self.dict[value2] == None:
				#Add edge from value2 to value1
				self.dict[value2] = [value1]
			else:
				#Add edge from value2 to value1
				self.dict[value2].append(value1)
		#Else both entries do not exist
		else:
			print("One or more vertices not found")
	#Function to find a vertex and print key values of it's adjacent vertices
	def findVertex(self, value):
		#If vertex is in graph
		if value in self.dict:
			#Print adjacent vertices key values
			print(self.dict[value])



'''Problem 5'''
#Tester Functions
#Function to test the queue class
def test_queue():
	print("--------Test queue--------")
	test_q = custom_queue()
	print("----Push ints 0-9----")
	for i in range(10):
		print(i)
		test_q.push(i)
	print("----Try push non int----")
	test_q.push(11.2)
	print("----Try pop 20 from queue----")
	for i in range(20):
		print(test_q.pop())

#Function to test the stack class
def test_stack():
	print("--------Test stack--------")
	test_s = custom_stack()
	print("----Get size while empty----")
	print(test_s.checkSize())
	print("----Push ints 0-9----")
	for i in range(10):
		print(i)
		test_s.push(i)
	print("----Try push non int----")
	test_s.push(11.2)
	print("----Get size while full----")
	print(test_s.checkSize())
	print("----Try pop 20 from stack----")
	for i in range(20):
		print(test_s.pop())
#Function to test the binary tree class
def test_tree():
	print("--------Test Tree--------")
	print("----Initialize tree with root value of 5----")
	test_t = custom_tree(5)
	print("----Add 0-9 values----")
	test_t.add(2,5)
	test_t.add(1,2)
	test_t.add(6,5)
	test_t.add(4,5) #Should print parent full
	test_t.add(8,6)
	test_t.add(10,6)
	test_t.add(15,2)
	test_t.add(4,1)
	test_t.add(16,1)
	test_t.add(50,10)
	test_t.add(60, 50)
	test_t.add(20,80) #Should print not found
	print("----Print tree----")
	test_t.print_tree()
	print("----Remove 2,5, and 9----")
	test_t.delete(2) #Should say has children
	test_t.delete(12) #Should say not found
	test_t.delete(8) #Should delete successfully
	test_t.delete(60)
	print("----Print tree----")
	test_t.print_tree()

#Function to test the graph class
def test_graph():
	print("--------Test Graph--------")
	test_g = custom_graph()
	print("----Adding vertices 0-9----")
	for i in range(10):
		print(i)
		test_g.addVertex(i)
	print("----Adding edge not in graph----")
	test_g.addEdge(10,5)
	print("----Adding random edges----")
	for i in range(25):
		test_g.addEdge(random.randint(0,9),random.randint(0,9))
	print("----Finding vertices----")
	for i in range(10):
		print(i)
		test_g.findVertex(i)
#If this file is being run a the main file
if __name__ == "__main__":
	test_queue()
	test_stack()
	test_tree()
	test_graph()