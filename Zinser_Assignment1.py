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
	#initialize the object with an empty stack
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
'''Problem 4'''
'''Problem 5'''

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
if __name__ == "__main__":
	test_queue()
	test_stack()