#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 21:26:10 2020

@author: Alaisha Naidu
Practice

"""

#Question 1
#Fibonaci Sequence Iteration
def fibI(n):
    terms = [0,1]
    i = 2 
    while i <= n:
        terms.append(terms[i-1] + terms[i -2])
        i = i + 1
    return terms


#Question 2
#Fibonaci Sequence Recursion 
def fibR(n):
    if n == 0:
        return 0 
    elif n == 1:
        return 1
    else:
        return (fibR(n-1) + fibR(n-2)) #note problem of redundancy 


#Question 3
#Palindrome check
def PalCheck1(string): 
    # Comparing first and last, working inwards saves half the number of comparisons
    # than inverting each word and comparing every letter
    char_index1 = 0 
    char_index2 = len(string)-1
    while char_index1 <= char_index2:
        if string[char_index1] == string[char_index2]:
            print(string[char_index1],string[char_index2], "True")
            char_index1 +=1
            char_index2 -=1
        else:
            return False

#print(PalCheck1("alaisha"))

#Question 4
#Anagram check
from collections import Counter
def AnaCheck(string1, string2):
    str1 = string1.replace(" ", "")
    str2 = string2.replace(" ", "")
    if len(str1) == len(str2):
        count1 = Counter(str1)
        count2 = Counter(str2)
        print (count1-count2) #If it returns empty then it is an anagram
        if count1 == count2:
            print(string1,"-", string2, "\n", "This is an anagram")
        else:
            print(string1,"-", string2, "\n", "not an anagram")
    else:
        print(string1,"-", string2, "\n", "not an anagram")
        
#print(AnaCheck("school master", "the classroom")) 

#Question 5
#Determine if a Binary tree is a binary search tree or not 
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None #initial left child is none
        self.right = None #initial right child is none

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
        
    def print_tree(self, traversal_type): #prints nodes according to how tree is traversed
        if traversal_type == "inorder":
            return self.inorder_print(tree.root, " ") #pass tree root and empty string
        else:
            print("traversal type" + str(traversal_type) + "is not supported")
            return False
   
 #IN-ORDER (starting from left most node to root to right most node)
    #4,2,5,1,6,3,7,
    def inorder_print(self, start, traversal):
        if start: 
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + " ")
            traversal = self.inorder_print(start.right, traversal)
        return traversal
                    
            
tree = BinaryTree(6)                #         6
tree.root.left = Node(4)            #       /   \
tree.root.right = Node(8)           #     4       8
tree.root.left.left = Node(3)       #    / \     / \
tree.root.left.right = Node(5)      #   3   5   7   9  an in-order traversal will return an ordered list from smallest to largest value
tree.root.right.left = Node(7) 
tree.root.right.right = Node(9) 

print("In-order " + tree.print_tree("inorder"))

def Convert(string): 
    a_list = string.split()
    map_object = map(int, a_list)
    
    list_of_integers = list(map_object)
    return list_of_integers

def Check(list):
    x = 0
    y = len(list)-1
    while x < y:
        if list[x] < list[x+1]:
            print("true") 
            x += 1
            if x == y:
                print('This is a Binary Search Tree')
        else:
            print("Not a Binary Search Tree")
            return False
        
print(Convert(tree.print_tree("inorder")))
print(Check(Convert(tree.print_tree("inorder"))))

#Question 6
#Mirror of a binary tree
#Define a node class for the nodes in the tree
class Node(object): 
    def __init__(self, value):
        self.value = value
        self.left = None #initial left child is none
        self.right = None #initial right child is none
        
    
def inorder_print(node): 
    if node == None:  
        return
          
    inorder_print(node.left)  
    print(node.value, end = ",")  
    inorder_print(node.right)  
        
def binary_tree_mirror(node):
    if node == None:
        return 
    else:
        temp = node 
        binary_tree_mirror(node.left)
        binary_tree_mirror(node.right)
        
        temp = node.left  # place holder for left node
        node.left = node.right  # new value for left node is previous value of right node
        node.right = temp # new value of right node is previous value of the left node



tree = Node(1)                 #         1
tree.left = Node(2)            #       /   \
tree.right = Node(3)           #     2       3
tree.left.left = Node(4)       #    / \     / \
tree.left.right = Node(5)      #   4   5   6   7
tree.right.left = Node(6) 
tree.right.right = Node(7) 

print("\nInorder traversal of the existing tree is ")  

inorder_print(tree) 

binary_tree_mirror(tree)

print("\nInorder traversal of the mirror tree is ")  
               
inorder_print(tree) 



































