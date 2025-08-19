#stack-stores data in the format of(LIFO) or (FILO)
#while is used when we know stopping condition
#for loop is used when we know how many times we need to execute the loop body
# if we take return in if condition then we no need to write the else condition
#Array:-group of same types of values ,its size is fixed
#it is not built in datastructure so we need to import it
#module is nothing but .py
#array can store char,int,float

"""
1. Arrays are sequence types and behave very much like lists,but arrays can have elements of limited types.
we need to store homogenous data
syntax:- from array import *
a1= array(typecode,[,elements])
methods:-append()-add value at last
count()-count the particular element accurance,
extend(),fromlist(),index(),insert(),pop()-delete the last element and retrun it,and it also uses index
remove()-we use value in remove method to delete the value,reverse(),tolist()-convert array to list
dynamic array is resizable ex is list
mathematics calculations then we should use numpy

from array import *
a1=array('i',[23,56,11])
type(a1)
 
import numpy as np
a=np.array([1,2,3])
print(a)
b=np.array([[1,2,3],[10,20,30]])
print(b)


"""


'''
stack=[]
def push():
    if len(stack)==n:
        print("list is full")
    else:
        ele=input("Enter the element:-")
        stack.append(ele)
        print(stack)
def pop():
    if not stack:
        print("stack is empty")
    else:
        e=stack.pop()
        print("removed element",e)
        print(stack)
n=int(input("enter the number of elements"))
while True:
    print("Enter your choice 1.push/2.pop/3.quit")
    choice=int(input("Enter the value:-"))
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        break
    else:
        print("Enter correct value")    



#queue-front-removed from here rear-added here and wice versa-firist in first out
#add- enqueue
#remove - dequeue
#isfull,isempty
#insert(0,element) then we will use pop
#else we use append and pop(0)

queue=[]
def enque():
    ele=input("Enter the element:-")
    queue.append(ele)
    print(queue)
def deque():
    if not queue:   #not queue means length is zero or not for checking this 
        print("Queue is empty:!!!")
    else:
        e=queue.pop(0)
        print("deleted element",e)
        print(queue)
def display():
    print(queue)
while True:
    #highest value has highest priority
    queue.sort(reverse=True)#if we have priority then we need to use this reverse function
    print("Enter your choice 1.enque/2.deque/3.display/4.exit")
    choice=int(input("Enter your choice:-"))
    if choice==1:
        enque()
    elif choice==2:
        deque()
    elif choice==3:
        display()
    elif choice==4:
        exit()
    else:
        print("Choose correct option!!!")

import collections
queue=collections.deque()
queue.append(10)
queue.append(20)
queue.append(30)   #or we use appendleft and pop also same as that
queue.popleft()
print(queue)


#LINKED LIST
it contains two fields data or head and link of node2 and so on and last node contains NULL
NODE:elements of linked list
in linked list data is stored in contiguos memory
types:
singly linked list or simple linked list-one link -forward direction
doubly linked list-two link
circular linked list-

adding elements-begining,end,or in between,when ll is empty
delete
traverse

adding element:-
at starting:-
1.create node
2.new_next=head
3.head=new 
at ending:-
1.create node
2.if node(left==null) then we will reach last node
3.new next=null
4.prev_node left=new
at between: two types after the node and before the node
1.create node
2.prev_nede next=new
3.new_node next=new node


delete element:-
at starting:-
head=curr_node
at ending:-
reach last_node prev
prev_node_next=NULL
at between:
1.ele->before
cur_node prev_next=

Traversal:-start with head if head is not NULL access the info and goto next node access the info and continue this
process unitill you reach last node


#singly Linked List
class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class linkedlist:
    def __init__(self):
        self.head=None
    def print_linkedlist(self):
        if self.head==None:
            print("Linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n=n.ref

    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    
    def add_atend(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref = new_node
    
    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if x == n.data:
                break
            n=n.ref
        if n is None:
            print("Node is present in ll")
        else:
            new_node = Node(data)
            new_node.ref=n.ref
            n.ref=new_node

    def add_before(self,data,x):
        if self.head is None:
            print("Linked list is empty!")
            return
        if self.head.data ==  x:
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n=n.ref
        if n.ref is None:
            print("Node is Not Found!")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node

    def insertat_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head=new_node
        else:
            print("Linked list is Not Empty")
    def del_begin(self):
        if self.head is None:
            print("Deleting the node is Not possible")
        else:
            self.head=self.head.ref

    def del_ending(self):
        if self.head is None:
            print("Deleting the node is Not possible")
        elif self.head.ref is None:
            self.head=None
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None
    def del_middle(self,x):
        if self.head is None:
            print("Deleting the node is Not possible")
            return
        if x==self.head.data:
            self.head=self.head.ref
            return
        n=self.head
        while n.ref is not None:
            if x==n.ref.data:
                break
            n=n.ref
        if n.ref is None:
            print("Node is not present")
        else:
            n.ref=n.ref.ref

LL1 = linkedlist()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_begin(30)
LL1.del_middle(20)
LL1.print_linkedlist()


#doubly linked list-backward and forward is possible
class Node:
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None
class doublyLL:
    def __init__(self):
        self.head= None
    def print_LL_forw(self):
        if self.head==None:
            print("Linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n=n.nref
    def print_LL_reverse(self):
        print()
        if self.head==None:
            print("Linked list is empty")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data,"-->",end=" ")
                n=n.pref

    def insert_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print("linked list is not empty")
    
    def insert_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node
    def insert_atend(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.nref=new_node
            new_node.pref=n

    def add_after(self,data,x):
        if self.head is None:
            print("LL is empty !")
        else:
            n=self.head
            while n is not None:
                if x==n.data:
                    break
                n=n.nref
            if n is None:
                print("Given node is present in the LL")
            else:
                new_node=Node(data)
                new_node.nref=n.nref
                new_node.pref=n
                if n.nref is not None:
                    n.nref.pref=new_node
                n.nref=new_node
                
    def add_before(self,data,x):
        if self.head is None:
            print("LL is empty !")
        else:
            n=self.head
            while n is not None:
                if x==n.data:
                    break
                n=n.nref
            if n is None:
                print("Given node is present in the LL")
            else:
                new_node=Node(data)
                new_node.nref=n
                new_node.pref=n.pref 
                if n.pref is not None:
                    n.pref.nref=new_node
                else:
                    self.head=new_node
                n.pref=new_node  
    def del_begin(self):
        if self.head is None:
            print("Deleting is not possible")
            return
        if self.head.nref is None:
            self.head=None
        else:
            self.head = self.head.nref
            self.head.pref= None
    def del_end(self):
        if self.head is None:
            print("Deleting is not possible")
            return
        if self.head.nref is None:
            self.head=None
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.pref.nref=None

    def del_byvalue(self,x):
        if self.head is None:
            print("Deleting is not possible")
            return
        if self.head.nref is None:
            if x==self.head.data:
                self.head=None
            else:
                print("X is not present in the ll")
            return
        if self.head.data ==x:
            self.head=self.head.nref
            self.head.pref=None
            return
        n=self.head
        while n.nref is not None:
            if x==n.data:
                break
            n=n.nref
        if n.nref is not None:
            n.nref.pref = n.pref
            n.pref.nref=n.nref
        else:
            if n==x:
                n.pref.nref == None
            else:
                print("x is not present in LL!")


ddll=doublyLL()
ddll.insert_empty(10)
ddll.insert_begin(100)
ddll.insert_atend(20)
ddll.del_byvalue(10)
ddll.print_LL_reverse()



#circular linked list- it is linear data structure  
#circular sll, circular dll
# if we take last in place of start then we can not traverse at all method
# we need to traverse only on the del_last method 
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=None
class CLL:
    def __init__(self,last=None):
        self.last=None
    def is_empty(self):
        if self.last==None:
            print("Circular Linked list is empty")
            
    def insert_at_start(self,data):
        new_node=Node(data)
        if self.is_empty():
            new_node.next=new_node
            self.last=new_node
        else:
            new_node.next=self.last.next
            self.last.next=new_node
    
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.is_empty():
            new_node.next=new_node
            self.last=new_node
        else:
            new_node.next=self.last.next
            self.last.next=new_node
            self.last=new_node
    def search(self,data):
        if self.is_empty():
            return None
        n=self.last.next
        while n!=self.last:
            if n.item==data:
                return n
            n=n.next
        if n.item==data:
            return n
        return None
    def insert_after(self,n,data):
        if n is not None:
            new_node=Node(data,n.next)
            n.next=new_node
            if n==self.last:
                self.last=new_node
    def print_list(self):
        if not self.is_empty():
            n=self.last.next
            while n!=self.last:
                print(n.item,end=" ")
                n=n.next
        
            print(n.item)


    def del_first(self):
        if not self.is_empty():
            if self.last.next==self.last:
                self.last=None
            else:
                n=self.last.next
                self.last.next=n.next

    def del_last(self):
        if not self.is_empty():
            if self.last.next==self.last:
                self.last=None
            else:
                n=self.last.next
                while n!=self.last:
                    n=n.next
                n=next=self.last.next
                self.last=n
                    
    def del_item(self,data):
        if not self.is_empty():
            if self.last.next==self.last:
                if self.last.item==data:
                    self.last=None
            else:
                if self.last.next.item==data:
                    self.del_first()
                else:
                    n=self.last.next
                    while n!=self.last:
                        if n.next==self.last:
                            if self.last.item==data:
                                self.del_last()
                            break
                        if n.next.item==data:
                            n.next=n.next.next
                            break
                            n=n.next
l=CLL()
l.insert_at_start(10)
l.insert_at_start(20)
l.insert_at_end(30)
l.insert_at_end(40)
l.insert_after(l.search(10),50)
'''
"""
Tree is a non linear ds which represents the relationship b/w the nodes
collection of entities called nodes 
nodes are connected by edges
ex:-organization structure
tree terminilogies:-
1.node
2.root node-top most node
3.edge or link-connection b/w two nodes
4.parent node-the node has childern 
5.child-except root node all are child
6.sibling nodes
7.leaf node-node without child
8.internal node-the node has atleast one child
9.path-

Characterisstics:-
1.Root node-top most node a tree contain only one root node
2.in A tree if we have N nodes then we will have N-1 edges/link
3.every child will have only one parent but parent can have multliple child
4.tress is a recursive data structure
properties of trees:-
1.Degree of a node-total no .of childeren of that node
2.Degree of the tree-calculate degree of all the nodes and which has highest degree then it is the degree of the tree
3.Level-level count starts-0
4.height of the node-
5.Height of the tree-height of the root node
6.Depth-total  no of edges from root node to particular node
7.Depth of the tree-total  no of edges from root node to leaf node in the longest path

Apllication of trees:-
binary search
heap

Types of Trees:-
1.general tree-there is no limitations on the no.of childs
2.Binary tree structure-at most 2 children must be there-0,1,2 allows only this no.of childs
->Full binary tree
->comlete
->perfect
->balanced
->pathlogical/degenerate 


->Full/strict/strictly binary tree:-every node can have 0,2 child nodes only
 is a type of binary tree in which every node other than leaf nodes has 2 children
 all internal nodes-2 children
 leaf node -in any level

 ->comlete binary tree:-all levels except last_level completely filled
 last level completely filled from left to right

->perfect binary tree:-in which all internal nodes contain 2 children and al leaf nodes are present in same level
 all internal nodes-2 children
 leaf node -in same level

->balanced binary tree:-is a binary tree in which height of the left sub tree and right sub tree of every 
nodes may differ by atmost 1 if it is >1 then it is not a balanced BT
diff = height of left sub tree- height of right sub tree(<1 or =1)
height of empty tree is -1

->pathlogical/degenerate binary tree:-every parent node has only one child node


Binary search tree is a binary tree with following properties:-
1.the left subtree of a node contains only nodes with keys lesser than node's key
2.the right subtree of a node contains only nodes with keys greather than node's key
3.the left subtree and right sub tree each must also be a BST

Binary search tree with duplicate values:-
1.suplicate values are not allowed
2.left <= root/node < right
2.left < root/node <= right

binary search operations:-
1.check bst is empty :if yes :print a message : no:compare root key with given value 
2.root==given value:yes:then print key found
no:check where to search for key{you can search in different way}
3.guven vakue<root key:tes:search left subtree,start from step 1 no:search right subtree:start from step 1


2.insertion:-
you can compare root key and new node key in different ways
1.root key<new node key / new node key>root key: go to right subtree
2.root key>new node key / new node key>root key: go to left subtree

3.deletion:-
1.bst->empty->yes->can't delete
if no
2.search mentioned key if postive->node found else:->node is not found
3.delete node

case 1:-deleting the node that has 0 child
case 2:-deleting the node that has 1 child node
case 3:-deleting the node that has 2 child node
in case 3 replace deleted value with biggest value in the left sub tree 
                        or
replace deleted value with smallest value in the right sub tree

4.traversal opreation:-
1.pre order:-
to traverse a non-empty BST in pre-order ,the following operations are performed recursively at each node.
1.visit the root node
2.traversing the left sub-tree and finally
3.traversing the right sub-tree
pre order-root,left,right

2.in order:-
to traverse a non-empty BST in pre-order ,the following operations are performed recursively at each node.
1.traversing the left sub-tree
2.visit the root node and finally
3.traversing the right sub tree
in-order:-left,root,right

3.post order:-
to traverse a non-empty BST in pre-order ,the following operations are performed recursively at each node.
1.traversing the left sub-tree
2.visit the root node and finally
3.traversing the right sub tree
in-order:-left,right,root

4.level-order traversal:-starts from 0 to n

find min and max:-
min=left sub tree
max=right sub tree
total no.of nodes=no.nodes LST+no.of nodes RST + 1
#self is used to represent the instanse of the class

class binarysearchtree:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
    
    def insert(self,data):
        if self.key is None:
            self.key=data
            return
        if self.key==data:
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=binarysearchtree(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=binarysearchtree(data)

    def search(self,data):
        if self.key==data:
            print(" Node is found")
            return
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is Not present")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is Not present")

    def pre_order(self):
        print(self.key,end=" ")
        if self.lchild:
            self.lchild.pre_order()
        if self.rchild:
            self.rchild.pre_order()
    def in_order(self):
        if self.lchild:
            self.lchild.in_order()
        print(self.key,end=" ")
        if self.rchild:
            self.rchild.in_order()
    def post_order(self):
        if self.lchild:
            self.lchild.post_order()
        if self.rchild:
            self.rchild.post_order()
        print(self.key,end=" ")

    def deletion(self,data,curr):
        if self.key==None:
            print("Tree is empty")
            return
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.deletion(data)
            else:
                print("given node is not prensent in the tree")
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.deletion(data)
            else:
                print("given node is not prensent in the tree")
        else:
            if self.lchild is None:
                temp=self.rchild
                if data == curr:
                    self.key = temp.key
                    self.lchild=temp.lchild
                    self.rchild= temp.rchild
                    temp=None
                    return
                self=None
                return temp
            if self.rchild is None:
                temp=self.lchild
                if data == curr:
                    self.key = temp.key
                    self.lchild=temp.lchild
                    self.rchild= temp.rchild
                    temp=None
                    return
                self=None
                return temp
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.deletion(node.key)
        return self
    def min_node(self):
        current = self
        while current.lchild:
            current = current.lchild
        print("min value is:-",current.key)

    def max_node(self):
        current = self
        while current.rchild:
            current = current.rchild
        print("max value is:-",current.key)

# def count(node):
#     if node is None:
#         return 0
#     return 1+count(node.lchild)+count(node.rchild)

root=binarysearchtree(10)
list1=[6,3,1,6,98,3,7]
root.min_node()
root.max_node()
for i in list1:
    root.insert(i)
# if count(root)>1:
#     root.deletion(10,root.key)
# else:
#     print("cant perform del operation")
print()

"""
"""
# BINARY HEAP-complete binary tree which statisfies the heap property
heap property:-property of a node in which key of every parent node need to be lesser than or equal to
                                OR
greather than or equal to the child node's key

 TYPES OF HEAP DATA STRUCTURES:-
 1.binary heap
 2.binomial heap
 3.fibonacci heap

MIN HEAP/MIN BINARY HEAP:-complete binary tree ,where the key of every parent node is lesser than or equal to
the child node's key
MAX HEAP/MAX BINARY HEAP:-complete binary tree ,where the key of every parent node is greather than or equal to
the child node's key
uses:-
to implement priority key
in heap sort algorithm
to find kth largest or smallest element in list of numbers

operations of heap:-create binary heap from a given complete binary tree
    it is a process to rearrange the elements of the heap in order to maintain the heap property
    make sure that every node of tree follows heap property
    used to create binary heap from a complete binary tree

uses:-
insertion operation
deletion operation
while creating a binary heap from a given array

operations:-
1.heapify_up:-/up_heap/bubble_up/percolate_up/sift_up/trickle_up/swim_up/cascade_up
2.heapify_down:-/down_heap/bubble_down/percolate_down/sift_down,extract_win/extract_max/sink_down

Insertion:-inserting a new node to binary heap by maintaining its properties
1.add the new node to first open spot available in the lower level
2.heapify the new node

Deletion:-removing the node from binary heap by maintaining its properties
deletion method for all nodes except root node:-
1.swap the node you want to delete with the last node
2.delete the last node
3.heapify replacement node:
if replacement node follows heap property:don't worry stop
elif replacement node is less than parent node{for min heap} then swap and repeat step 3
else:swap replacement node with smallest child{for min heap} and repeat step 3

Binary heap:-max heap/min heap
1st method
take empty heap insert element of list to heap one by one
after inserting one element check whether it is following heap properties or not

2nd method
first create complete binary tree using given list of numbers
then start heapifying tree:start from last internal node

level1:- if it is last level it can have 2 or less than 2 nodes
ith->list[i]
parent->(i-1)/12
lchild-> (2*i)+1
rchild->(2*i)+2

Heapq:-import heapq
heapq.heappush(heap,item)
push item onto heap,maintaining the heap property
heapq.heappop(heap)
will return the smallest value and also it will delete that from heap,maintaining the heap property
heapq.heapify(heap)
will convert the given list to binary heap
heapq.heappushpop(heap,item)
heapq.heapreplace(heap,item)
heapq.nsmallest(n,iterable,key=none)
heapq.nlargest(n,iterable,key=none)

import heapq
list1 = [1,3,4,2,4,6]
heapq.heapify(list1)
heapq.heappushpop(list1,89)
heapq.heapreplace(list1,100)
print(heapq.nsmallest(2,list1))
print(heapq.nlargest(2,list1))
print(list1)

import heapq
list1 = [(1,"ria"),(4,"sia"),(3,"gia")]
heapq.heapify(list1)
print(list1)
for i in range(len(list1)):
    print(heapq.heappop(list1))

"""

"""
GRAPH:-graph is a non linear data structure consisting of nodes and edges
nodes/edges
G=(V,E)
g=graph
v=set of vertices
e=set of edges
():-ordered pair
{}:-unordered pair
uses:-google maps and gps
facebook and linkdin
e-commerce websites

TYPES OF GRAPHS:-
1.directed graph:-A graph in which all the edges are unidirectional(when direction mentioned)
Example:twitter
if i follow you there is no rule that you need to follow me

2.undirected graph:- a graph in which all the edges are bi-directional(when direction is not mentioned)
ex:-facebook
when i accept your friend request, me and you are friends now,we both can like or comment on each others 
story or photo
3.weighted graph:-a graph in which each edge is assigned with some weight/cost/value
4.unweighted graph:-a graph where there is no value or weight associated with the edge
5.cyclic graph:-if graph contain cycle then that graph is called cyclic graph
6.acyclic graph:-(tree is acyclic graph)  if graph doesn't contain cycle then that graph is called cyclic graph

TERMINOLOGIES OF NODES:-
1.Adjacent nodes/neighbour nodes:-node x is adjacent node y if there is an edge from node x to node y
2.path:-it is a sequence of vertices in which each pair of successive nodes is conncted by an angle
->simple path:-a path is simple if all of its vertices are distinct
->closed path:-a path is closed if the first and last node of that path is same
->cycle:-cycle is path in which first and last node need to be same and also all the other nodes need to be distinct
3.Connected graph:-a graph is said to be connected if there is a path from any node to any other node
->strongly connected graph:-we have path from any node to any other node
    according to these definition every strongly connected graph is also a weakly connected graph
->weakly connected graph:-if i remove directions now it will become undirected graph then it is a connected graph
that's it is weakly connected graph
4.Degree:-degree of a node=number of edges connected to it
->in degree:-in degree of a node = no.of edges coming to that node
->out degree:-out degree of a node = no.of edges going outside from that node
5.complete graph:-if any node in the graph adjacent to all the nodes of the class /there is an edge b/w every 
pair of graphs in a node
6.complete binary tree:-All levels must be filled 
l0=1
l1=2
l2=4
ln=2n
Almost complete binary tree:-All the levels must be completely filled exceprt possibly the last level and all
the nodes in the last level must be left aligned

GRAPH REPRESENTATION:-
1.Adjacency matrix:-Represents the connection between the nodes in matrix form
->create k*k matrix
->row and column represents the nodes of a graph
->if edge is present then store 1 otherwise store 0

2.Adjacent list:-{a:[b,c,d]
b:[a,d,e]
c=[a,d]
d=[a,b,c,e]
e=[b,d] }

GRAPH OPERATIONS:-
1.Insertion:-we can add a node to the graph
->add_node/add_vertex:-add new node to graph
->add_edge(v1,v2)
graph[v1][v2] = 1
graph[v2][v1] = 1
indireted graph:-
add_edge(v1,v2)
graph[v1][v2] = 1
in the nested list append a zero to every inner list
2.Deletion:-
delete_node(v)-it will delete node and also remove all the connections it have
Adj matrix:-delete the row and column of index v
graph[index(v1)][index(v2)] = 0{for directed graph} }
graph[index(v2)][index(v1)] = 0                     }       ->for undirected graph

Adj list:-delete key and value pair of v and chek the value of all key in dictionary for v,if it is present remove
that from the list
in graph[v1] remove v2{for directed graph}      }       ->for undirected graph
in graph[v2] remove v1                          }

delete_edge(v1,v2)-will del the edge b/w v1 and v2
3.Traversal:-
->DFS:-depth first search
1.consider starting node as current node and visit that node
2.visit the unvisited adjacent node of current node,make that node as current node
3.follow step 2 until we reach dead end
4.if unvisited nodes are present in the graph then back track take recent visited node as current node repeat step 2
stack implementation using DFS:-
1.visit starting node
2.select adj node of starting node
3.visit one of the unvisited node of starting node
4.search for adj node of selected node
->BFS:- breadth first search-it will access it in a level wise
A boolean visited array is used to mark the visited vertices
BFS uses a Queue data structure for traversal
traversing begin from a node called source node

#pseudo code
bfs(g,s):
    let Q be the queue 
    q.inset(s)
    v[s]=True
    while(!Q.isEmpty())
    {
    n=Q.getFront()
    Q.del()
    for all the neighbours u of n
    if v[u]==false
    q.insert(u)
    v[u]=True
    }


#program 
nodes=[]
graph= []
node_count = 0
#insertion
# function to add a new node using adjacency matrix representation
def add_node(v):
    global nodes,node_count,graph
    if v in nodes:
        print(v,"The node is already present")
    else:
        node_count +=1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp=[]
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)

# function to add an edge using adjacency matrix representation
def add_edge(v1,v2):
    if v1 not in nodes:
        print(v1,"is not present in the graph")
    elif v2 not in nodes:
        print(v2,"is not present in the graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 1 #for unweighted directed graph we use 1 inplace of cost
        # graph[index2][index1] = cost

#deletion
# function to delete a new node using adjacency matrix representation
def  delete_node(v):
    global node_count
    if v not in nodes:
        print(v,"is not prsent in the graph")
    else:
        index1 = nodes.index(v)
        node_count =node_count-1
        nodes.remove(v)
        graph.pop(index1)
        for i in graph:
            i.pop(index1)
# function to delete an edge using adjacency matrix representation
def delete_edge(v1,v2):
    if v1 not in nodes:
        print(v1," is not prsent in graph")
    elif v2 not in nodes:
        print(v2," is not prsent in graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 0
        graph[index2][index1] = 0

def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j],"<3"),end=" ")
        print()


add_node("A")
add_node("B")
add_node("C")
add_edge("A","B")
delete_edge("A","C")
print(nodes)
print_graph()



# function to add a new node using adjacency list representation
def add_node(v): #v is new_node
    if v in graph:
        print(v,"is already in graph")
    else:
        graph[v]=[]

# function to add an edge using adjacency list representation
def add_edge(v1,v2,cost):    #if you write for weighted graph then we to add cost parameter here
    if v1 not in graph:
        print(v1,"is not present in the graph")
    elif v2 not in graph:
        print(v2,"is not present in the graph")
    else:
        list1 = [v2,cost]
        list2 = [v1,cost]   #for directed graph make this line and line+2 as comment
        graph[v1].append(list1)
        graph[v2].append(list2)

def delete_node(v):
    if v not in graph:
        print(v,"is not present in the graph")
    else:
        graph.pop(v)
        for i in graph:
            list1 = graph[i]
            if v in list1:
                list1.remove(v)

def delete_edge(v1,v2,cost):
    if v1 not in graph:
        print(v1,"is not present in the graph")
    elif v2 not in graph:
        print(v2,"is not present in the graph")
    else:
        temp = [v1,cost]
        temp1 = [v2,cost]
        if temp in graph[v1]:
            graph[v1].remove(temp1)
            graph[v2].remove(temp)        #undirected graph and unweighted


graph={}
add_node("A")
add_node("B")
add_node("C")
add_edge("A","B",10)
add_edge("A","C",5)
delete_edge("A","B",1)
print(graph)



# DFS IMPLEMENTATAION USING RECURION METHOD
def add_node(v): #v is new_node
    if v in graph:
        print(v,"is already in graph")
    else:
        graph[v]=[]

def add_edge(v1,v2,cost):    
    if v1 not in graph:
        print(v1,"is not present in the graph")
    elif v2 not in graph:
        print(v2,"is not present in the graph")
    else:
        list1 = [v2,cost]
        list2 = [v1,cost]   
        graph[v1].append(list1)
        graph[v2].append(list2)

# def DFS(node,visited,graph):
#     if node not in graph:
#         print("Node is not present in the graph")
#         return
#     if node not in visited:
#         print(node)
#         visited.add(node)
#         for i in graph[node]:
#             DFS(i,visited,graph)

def DFSiterative(node,graph):
    visited = set()
    if node not in graph:
        print("Node is not present in the graph")
        return
    stack =[]
    stack.append(node)
    while stack:
        current = stack.pop()
        if current not in visited:
            print(current)
            visited.add(current)
            for i in graph[current]:
                stack.append(i)



# visited = set()
graph={}
add_node("A")
add_node("B")
add_node("C")
print(graph)
DFSiterative("B",graph)

"""
"""
RECURSION:-function calling itself is called recursion
In recurion problems is sloved in terms of problems itself
each time recursive function call to itself for little simpler version of the original problem
1.f1(n) 1+2+3+4+....+n
2.recursion case f1(n-1) +n 1+2+3+4+....+n-1+n
3.base case n==1 

# program for first n natural numbers
def f1(n):
    if n==1:
        return 1
    return n+f1(n-1)
    
r=f1(5)
print(r)

#print first N natural numbers 1 2 3 4 ... N
def printN(n):
    if n>0:
        printN(n-1)
        print(n,end=" ")
printN(10)

#for reverse order
def printrev(n):
    if n>0:
        print(n,end=" ")
        printrev(n-1)
printrev(10)

#for printing first 10 odd numbers
def printodd(n):
    if n>0:
        printodd(n-1)
        print(2*n-1,end=" ")
printodd(10)

#for printing first 10 even numbers
def printeven(n):
    if n>0:
        printeven(n-1)
        print(2*n,end=" ")
printeven(10)

def printevenrev(n):
    if n>0:
        print(2*n,end=" ")
        printevenrev(n-1)
printevenrev(10)

def printoddrev(n):
    if n>0:
        print(2*n-1,end=" ")
        printoddrev(n-1)
printoddrev(10)

#calculate sum of 1st n numbers
def sumN(n):
    if n==0:
        return 1
    return n+sumN(n-1)
print(sumN(10))

#calculate sum of 1st n odd numbers
def sumNodd(n):
    if n==1:
        return 1
    return 2*n-1+sumNodd(n-1)
print(sumNodd(10))

#calculate sum of 1st n even numbers
def sumNeven(n):
    if n==1:
        return 2
    return 2*n+sumNeven(n-1)
print(sumNeven(10))

#calculate the factorial
def fact(n):
    if n==0:
        return 1
    return n* fact(n-1)
print(fact(5))

#sum of squares of first N natural numbers
def sum(n):
    if n==0:
        return 1
    return n*n+sum(n-1)
print(sum(3))

f1(1) = 1
f1(2) = 1+2
f1(3) = 1+2+3
f1(4) = 1+2+3+4
f1(n) = 1+2+3+4+...+n
f1(100) = 100+f1(99)
            99 + f1(98)
            98 + f1(97) ....n

"""
"""
sorting:-
arranging data elements in some logical order(ascending or descending) is known as sorting
->internal sorting 
->external sorting-data is stored externaly
when elements are numbers,sorting means arranging numbers in "ascending order(by default)"
when elements are strings sorting means arranging strings in "dictionary order(alphabet) order by default"
VARIOUS SORTING ALGORITHMS:-

1.Bubble sort:-
Ex:-
    0  1  2  3  4  5 
    24 58 11 67 92 43
1.(0,1) (1,2)(2,3)(3,4)(4,5)
    24   11   58   67 43 92
2.(0,1) (1,2)(2,3)(3,4)
    11 24 58 43 67 92
3.(0,1) (1,2)(2,3)
    11 24 43 58 67 92
4.(0,1) (1,2)
    11 24 43 58 67 92
5.(0,1) 
    11 24 43 58 67 92


2.modified bubble sort:-
n elements round-k  0<k<n
no swapping in kth round means elements are sorted now no more rounds to be executed
3.selection sort:-noramly select small number and place at first place and place the first place element in small number index
    0   1   2   3   4   5   6   7   8
    38  90  47  69  52  88  71  18  20
    18                          38
        20                          90
            38                  47
                47              69
                    52  69      88
                            71
    18  20  38  47  52  68  71  88  90
4.Insertion sort:-
    0   1   2   3   4   5   6   7   8   9
    50  20  37  91  64  18  43  59  72  81
    20  50
    20  37  50
                91  
                64  91  
    18  20  37  50  64  91
                43  50  64  91
                        59  61  91
                                72  91
                                    81  91
    18  20  37  43  50  59  61  72  81  91
5.Quick sort:-
        0   1   2   3   4   5   6   7   8   9
        58  62  91  43  29  37  88  72  16  30
left=0          while l[loc]<l[right]
right=9             right-=1
loc=0           swap
                while l[left]<l[loc]
                    left+=1
                swap

lesser=[43,29,37,16,30]  lesser than 58
greather=[62,91,88,72]  greather than 58

6.Merge sort:-
1.divide list into two lists
divide the sub list into sub lists
7.Heap sort:-
Heap is a data sstructure
heap is used in a sorting algorithm known as heap sort and it also used in priority queue
heap are of two types
->max heap(default)
->min heap
HEAP PROPERTIES:-
The value at node N is greather than or equal to value at each children or equal to value at each childreb of node N
1.heap must be an almost complete binary tree 
2.for max heap:-n0>=n1 and n0>=n2
3.for min heap:-n0<=n1 and n0<=n2
REPRESENTATION OF HEAP:-
unleass otherwise stated heap is maintained in memory by a linear array(list)
How to find parent or child node:-
index to find index of child nodes
index of left child = 2 * index + 1
index of right child = 2 * index + 2
index of parent node
index of node N = index
index of parent node of N = (index - 1)/2
HEAP SORT:-
in heap delete operation performed only on the top most element or top or root node only
Delete values from  the heap(max_heap) and store them in an array from right to left.As a result,at the end of 
deleting all the elements of heap array becomes sorted.



# BUBBLE SORT:-
def bubble_sort(data_list):
    for r in range(1,len(data_list)):
        for i in range(len(data_list)-r):
            if data_list[i]>data_list[i+1]:
                data_list[i],data_list[i+1]=data_list[i+1],data_list[i]

def modified_bubble_sort(data_list):
    flag=False
    for r in range(1,len(data_list)):
        flag=False
        for i in range(len(data_list)-r):
            if data_list[i]>data_list[i+1]:
                data_list[i],data_list[i+1]=data_list[i+1],data_list[i]
                flag=True
        if not flag:
            break
l=[24,58,11,67,92,43]
modified_bubble_sort(l)
print(l)

# SELECTION SORT:-
def selection_sort(list1):
    n=len(list1)
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if list1[j]< list1[min_index]:
                min_index=j
        list1[i],list1[min_index]=list1[min_index],list1[i]
l1=[64,35,89,71,72,13]
selection_sort(l1)
print(l1)

def insetion_sort(list1):
    for i in range(1,len(list1)):
        temp = list1[i]
        j=i-1
        while j>=0 and temp<list1[j]:
            list1[j+1] = list1[j]
            j-=1
        list1[j+1]=temp

mylist=[25,37,11,14,60,82,18,41]
insetion_sort(mylist)
print(mylist)      

#Quick sort
def Quick_sort(list1):
    if len(list1)<=1:
        return list1
    else:
        pivot=list1[0]
        lesser=[x for x in list1[1:] if x<=pivot]
        greather=[x for x in list1[1:] if x>pivot]
        return Quick_sort(lesser)+[pivot]+Quick_sort(greather)
mylist=[53,11,72,68,41,25,18,37,44,80]
Quick_sort(mylist)
print(mylist)

#merge sort
def merge_sort(list1):
    if len(list1)>1:
        mid = len(list1)//2
        leftlist = list1[:mid]
        rightlist = list1[mid:]
        merge_sort(leftlist)
        merge_sort(rightlist)
        i=j=k=0
        while i<len(leftlist) and j<len(rightlist):
            if leftlist[i]<rightlist[j]:
                list1[k]=leftlist[i]
                i+=1
            else:
                list1[k]=rightlist[j]
                j+=1
            k+=1
            while i<len(leftlist):
                list1[k]=leftlist[i]
                i+=1
                k+=1
            while j<len(rightlist):
                list1[k]=rightlist[j]
                j+=1
                k+=1

mylist=[75,29,83,42,16,90,56,34,20,71,88,92,7]
merge_sort(mylist)
print(mylist)


class Heap:
    def __init__(self):
        self.heap=[]
    def create_heap(self,list1):
        for e in list1:
            self.insert(e)
    def insert(self,e):
        index = len(self.heap)
        parentIndex = (index-1)//2
        while index>0 and self.heap[parentIndex]<e:
            if index == len(self.heap):
                self.heap.append(self.heap[parentIndex])
            else:
                self.heap[index]=self.heap[parentIndex]
            index = parentIndex
            parentIndex=(index-1)//2
        if index == len(self.heap):
            self.heap.append(e)
        else:
            self.heap[index]=e

    def top(self):
        if len(self.heap)==0:
            raise EmptyHeapException()
        return self.heap[0]
    def delete(self):
        if len(self.heap)==0:
            raise EmptyHeapException()
        if len(self.heap) ==1:
            return self.heap.pop()
        max_value=self.heap[0]
        temp = self.heap.pop()
        index = 0
        leftchildIndex=2*index+1
        rightchildIndex=2*index+2

        while leftchildIndex<len(self.heap):
            if rightchildIndex<len(self.heap):
                if self.heap[leftchildIndex]>self.heap[rightchildIndex]:
                    if self.heap[leftchildIndex]>temp:
                        self.heap[index] = self.heap[leftchildIndex]
                        index = leftchildIndex
                    else:
                        break
                else:
                    if self.heap[rightchildIndex]>temp:
                        self.heap[index] = self.heap[rightchildIndex]
                        index = rightchildIndex
                    else:
                        break
            else:   #no right child
                if self.heap[leftchildIndex] > temp:
                    self.heap[index]=self.heap[leftchildIndex]
                    index = leftchildIndex
                else:
                    break
            leftchildIndex=2*index+1
            rightchildIndex=2*index+2
        self.heap[index] = temp
        return max_value
    
    def heapsort(self,list1):
        self.create_heap(list1)
        list2=[]
        try:
            while True:
                list2.insert(0,self.delete())
        except EmptyHeapException:
            pass
        return list2
    
class EmptyHeapException(Exception):
    def __init__(self,msg="Empty heap"):
        self.msg=msg
    def __str__(self):
        return self.msg
list1=[34,56,12,78,43,25,10,80,60]
h=Heap()
list1=h.heapsort(list1)
print(list1)

"""
"""
searching:-
1.Linear search:-
list=   0   1   2   3   4   5   6   7   8   9
        34  41  29  62  87  91  43  18  27  5
item->25
for e in list1:
    if e==item:
        return list1.index(e)
    return none
Time complexity:-
worst case-O(n)

def linear_search(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

2.Binary search
list=   0   1   2   3   4   5   6   7   8   9
        34  41  29  62  87  91  43  18  27  5

sort:-
5   18  27  29  34  41  43  62  87  91

m=lower+upper//2
if item==list1[m]:
    return m
if item<list1[m]
    binarysearch(list1,0,3)
else:
    binarysearch(list1,5,9)

Time complexity:-O(log2 n)

def binary_search(arr,low,high,x):
    if high>= low:
        mid = (high+low)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr,low,mid-1,x)
        else:
            return binary_search(arr,mid+1,high,x)
    else:
        return -1
arr=[2,3,53,35,98,35]
x=3
result = binary_search(arr,0,len(arr)-1,x)
if result!=-1:
    print("element present in index",str(result))
else:
    print("Element is not available")
    
"""
"""
Hashing:-
WHY HASHING:-
->Hashing is deigned to slove the problem of needing to efficiently find or store an item in a collection
->if we have a list of 1,00,000 words of english and we want to search a given word in the lsit it would be
inefficient to succesive compare the word with all 1,00,000 words until we find a match

It is a technique of mapping keys and values into the hash table by using a hash function
it implemented correctly then one can achieve O(1) time complexity in searching an item in the collection
of elements
Efficiency of mapping depends on the effieciency of the hash function used
Hah Talble:-it is the data structure used to store elements
Hah function:-it is a function to map(hash) key_values to the memory address
Hashing:-It is a method for storing and retriveing records from a database
suppose 100 student records need to be stored in an array of 100 memory slots.use hashing to perform efficient 
access of student data.
Roll no->1 to 100
key
i=HF(key)
int HF(int key)
{
return key-1
}
memory slots will store 
i=key-1

->hashing is a method of storing and retreving records from data structures
->It lets you insert delete and search records based on search key value
->when properly implemented these operations can be performed in constants time
->This is far better than O(log2n) average cost required to do a binary search on a sorted array
->hashing generally takes records where key values come from a large range and stores those records in a table with
a relatively small number of slots

roll no---->5dig
10000 to 99999
10025--->25
25287--->87
51128-->28
48225-->25

def hf(key):
    return key%100;

Collision:-Collision occur whwn two records hash to the same slot in the table
unfortunately even under the best of circumstances collision are nearly unavailable

Hash Functions:-
The hash function creates a mapping between key and value this is done through the use of mathematical format
various hash functions:-
1.simple mod function
2.division method
3.binning
4.mid square method
two types of resoluctions:-
1.open hashing(chaining)
2.closed hashing(open addressing)
"""
"""
TIME COMPLEXITY:-
Basic of Functions
T=f(n)[y=f(x)]
t=time

Measuring performance of Algorithm:-
Algorith analysis is an important part of computational complexity theory ,which provides theoritical estimation 
for the required resources of an algorithm to slove a specific computational problem
->it is the determination of the amount of time and space resoures required to execute it

Why Analysis is required:-
->predicting behaviour of an algorithm without implementing
->Analysis is only approximately there are many influencing factors
->It helps us in determming the best algorithm to slove a programming problem.

Types of Algorithms Analysis:-
1.Best case
2.Worst case
3.Average case
->certain input takes less time for an algorithm to acccomplish its task.This is best case
->certain input takrs max time for an algorithm to accomplish its task.This is wrost case
->All other cases/total no.of cases=Average case

Time Complexity:-
It is a measure of rate of change in time with respect to change in input size
->various asymptotic notations are there to represent time complexity of an algorithm

Asymptotic Analysis:-
->It is used to anlysze performance of algorithma in terms of input size
->We dont calculate the actual time taken by the algorithm to slove the problem rather we are intersted in how the 
time taken by an algorithm increases with input size

1.Big O notation:-provides an upper bound on the growth rate of time.It represents the "wrost case" scenarios
2.Omega notation:-provides a lower bound on the growth rate of time.It represents the "best case" scenarios
3.Theta notation:-provides both an upper bound and lower bound on the growth rate of time.It represents the 
"average case" scenarios

Theta notation:-theta(g(n))= f(n)
c1*g(n)<=f(n)<=c2*g(n) 
c1,c2 are positive constants for all n>=n0

Big O notation:-
O(g(n)) = f(n)
o<=f(n)<=cg(n)
for all n>=n0

Omega notation:-
omega(g(n)) = f(n)
c*g(n)<=f(n)
for all n>=n0

Calculation O(n):-
1.Factorial
2.Insertionn sort

F=1         ->c1
if n==0     ->c2
    return 1
for i=1 to n    ->c3=ntimes
    f=i*f      ->c3=ntimes
return f        ->c4

f(n)=c3.n+c
g(n)=n
O(n)

2.
for(i=1 to n)
    temp=A[i]       ->c1
    for (j=i-1 to 0)        ->c2-->ic2
        if(A[j]>temp)       ->c2
            A[j+1]=A[j]     ->c2
        else
            break
    A[j+1]=temp     ->c3

n(c1+ic2+c3)
n(nc2 + c)
f(n)=c#down2n#up2+cn
g(n)=n2
O(n2)
theta(n2)
omega(n)


O(1)<O(logn)<O(n)<o(nlogn)<O(n2)<O(n2 log n)<O(n3)<O(a4)
"""