# Python-Linked-List
My first Linked List in Python. Check it out!

# Overview

Now further on my journey into trying to become a self-taught software engineer, I tackled linked lists. 
They're my first data structure outside of arrays that I've tackled, and I had no experience with this prior, and it was 
hard to wrap my head around it the first time around. I've coded this exact scheme maybe five times, and the fifth time 
I coded it was today when I did it and uploaded the repository.

## What This Repository Includes

This includes a linked list class, it includes a node class, and if you 
follow the formula that I put in, that is if you put a list into main and then you
do the for loop in there and you hit display, you can add nodes, you can delete nodes,
you can put any list in there, and it will create you a linked list.

## Next Steps

For my next project, I would like to implement other data structures or code a dynamic array 
from scratch in C++. I also have some projects coming up that I'm excited to post that I'm 
working on, and hopefully they come to fruition sooner rather than later.

## Future Additions

In the future, I'd like to write a mechanism for this repository to be able to
reverse any linked list, to display it and then reverse it, but that is going to come later.



---



# Linked List Breakdown and Reasoning

Now, if you know anything about linked lists and data structures, then this section might not be immediately applicable to you, but if you're new to the scene or just want to read it, I'm going to give my breakdown on why I did what I did and my reasoning behind the linked list.

## What a Node Is

Essentially, the first thing we've got to do is create a node, which is a container that holds data. The node has two parts: it has actual data that you'll store, and it has a pointer, like a little finger, that tells you where the next one in line is.

We can imagine a linked list as a bunch of nodes pointing to the next person in line. If we imagine we're at a store at Walmart with a line of five people, we'll assume the last person in line is the first person in our linked list. That last person in line has his finger up, pointing to the person in front of him, who is also pointing to the person in front of him, and so on, until you reach the person at the front, who is not pointing to anybody. This is how we can visualize a linked list.

## Linked Lists vs Arrays

Linked lists are good in that they can insert or delete nodes freely and easily in constant time, but they're not good at finding the actual information. This is in contrast with arrays, which are good at finding information with the indices in constant time, but not good at inserting or deleting things in the middle of the array.

## The Node Class

The first thing we have to do in LinkedList.py is create the actual node. Every time we create a node, we pass one parameter, the data. The other parameter is next, which will always be set to None.

## The LinkedList Class

We move on to the LinkedList class, which we can initialize without any parameters. The inside variable that we initialize is head, which is set to None because if we create a LinkedList, then there’s nothing. If we start a new line of people, there’s not going to be anybody at the front unless we add somebody.

## Adding a Node (add_node(data))

First we check:
if not self.head:
  self.head = Node(data)
  return

This checks if the LinkedList has a head. If it doesn’t, then the node that we're adding becomes the head.

If we’re adding the second node, now we have a head. We set a current variable equal to self.head. Current is essentially how we figure out which node does not have its finger up pointing to something. In the line example, it’s the person at the front of the line.

We run a while loop:

while current.next:

As long as the node we are on has something after it, we go inside the loop and reset current. We move from person one to person two to person three, and so on, until we reach the final person who is not pointing to anybody. When current.next is None, we escape the loop and add the new node there.

## Display Method (display())

The display method takes no parameters. We set a starting position:
current = self.head

We reinitialize a node_list, which is an empty list we’ll append to.

We run a while loop checking if we have a current node. If we do, we append the data of that current node, and then move our finger to the next node in the sequence. We go down the line the same way we did in add_node.

At the end, we define formatted_text, which joins every entry in node_list into one string, with an arrow between each entry. That’s the traditional way to view a linked list. Then we print out the formatted text.

## Delete Node(delete_node(data))

Delete node takes a data parameter because we have to compare it to see where the node we want to delete is. In a linked list, we’re not necessarily deleting the information; we’re acting as if it doesn’t exist. With a linked list [1, 2, 3], deleting 2 means telling 1 to point to 3.

We initialize current and previous. If current is the head and its data matches what we want to delete, we throw out the head and make the second entry the first.

If not, we enter a while loop that checks two conditions:

current must be a valid node

current.data must not equal the data we’re looking for

If we're looking for 2 in [1, 2, 3], and we’re on node 1, then inside the loop we set previous to current (1) and current to current.next (2). Then we check again. Now current.data equals what we want, so we exit the loop.

If we get to None, the data wasn’t found, so we print an error.

If the data was found, we set:
previous.next = current.next

This means node 1 now points to node 3. That is how we delete a node in a linked list.

# Closing

So that’s my pseudo explanation of all this. 
I hope you guys enjoy this, I hope that made at least a little bit 
of sense, and we're in week five of my self-taught coding journey.

### Started Journey: October 13th, 2025
