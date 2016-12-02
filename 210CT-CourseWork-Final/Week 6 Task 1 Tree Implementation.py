#include <iostream>

class BinTreeNode(object):

    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None

def tree_sort(newTreeArray):

    t=tree_insert(None,newTreeArray[0])

    for i in newTreeArray[0:]:
        tree_insert(t,i)
    in_order(t)


        
def tree_insert( tree,item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree

def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print (tree.value)
#S = []
#S.append(i)
#S.pop() -> 10
#S = [3,6,8,9]
def in_order(tree):


    treeStack = [tree]

    c = 1
    

    while( treeStack != None):
        

        l = treeStack[c-1]

        if l.left != None:
            treeStack.append(tree.left)
            tree = tree.left
            c = c + 1
            continue

        x = treeStack.pop()

        print (x.value)

        r = treeStack[c-1]


        if r.right != None:
            tree = tree.right
            treeStack.append(tree)
            c = c + 1
            continue

        print(x.value)


        



if __name__ == '__main__':
    
  
  #tree_insert(t,10)
  #tree_insert(t,5)
  #tree_insert(t,2)
  #tree_insert(t,3)
  #tree_insert(t,4)
  #tree_insert(t,11)
  #in_order(t)
  treeArray = [0,1,8,5,9,2,13]
  tree_sort(treeArray)


