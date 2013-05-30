#!/usr/bin/python -O

class Node():
	left = None
	right = None
	value = "0"

	def __init__(self, value="0", left=None, right=None):
		self.value = value
		self.right = right
		self.left = left
		pass


def printTree(root, depth=0):
	if root != None:
		if root.right != None:
			printTree(root.right, depth + 1)
		print "\t"*depth + root.value
		if root.left != None:
			printTree(root.left, depth + 1)
	pass


def serialize(root):
	left = "/"
	right = "/"
	if root.left != None:
		left = serialize(root.left)
	if root.right != None:
		right = serialize(root.right)
	return root.value + "," + left + right
	pass


def deserialize(data):
	value = data[ :data.find(',') ]
	data = data[ data.find(',') + 1: ]
	root = Node(value)

	if len(data) > 0 and data[0] != "/":
		left, data = deserialize(data)
		root.left = left
	else:
		data = data[ 1: ]

	if len(data) > 0 and data[0] != "/":
		right, data = deserialize(data)
		root.right = right
	else:
		data = data[ 1: ]
	
	return root, data
	pass


def main():
	root = Node("99", Node("75", Node("1", Node("0")), Node("2")), Node("135", Node("100"), Node("200")))

	printTree(root)
	pickled = serialize(root)
	print pickled
	root, _ = deserialize(pickled)
	printTree(root)
	pass


if __name__ == "__main__":
	main()
	pass
