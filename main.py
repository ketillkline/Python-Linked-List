from LinkedList import Node, LinkedList

number_list = [
    '1', '2', '3', '4', '5', '6'
]

numbers = LinkedList()
for number in number_list:
    numbers.add_node(number)

numbers.delete_node('3')
numbers.display()