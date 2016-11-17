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
  

def in_order(tree):


    previousLeft = []
    previousRight = []
    x = True

    while( x == True):

        if tree.left != None:
            previousLeft.append(tree.value)
            tree = tree.left
            continue
        print (tree.value)

        if tree.right != None:
            previousRight.append(tree.value)
            tree=tree.right
            continue

        if len(previousLeft) > len (previousRight):
            largestLength = len(previousLeft)

        else:
            largestLength = len (previousRight)

        leftExcced = False
        rightExcced = False
            

        for i in range(0,largestLength):
            

            if i > len(previousRight)-1:
                rightExcced = True

            if i > len(previousLeft)-1:
                leftExcced = True

            if leftExcced == False:
                print (previousLeft[i])

            if rightExcced == False:
                print (previousRight[i])

        print(previousLeft)
        print(previousRight)

        x = False


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


