class Node(object):
     def __init__(self, value):
          self.value=value
          self.next=None
          self.prev=None

class List(object):
     def __init__(self):
          self.head=None
          self.tail=None
     def insert(self,n,x):
          if n!=None:
               print ("")
               x.next=n.next
               n.next=x
               x.prev=n
               if x.next!=None:
                    x.next.prev=x
              
          if self.head == None:
               print ("Head Assignment")
               self.head=self.tail=x
               x.prev=x.next=None
          elif self.tail==n:
               print ("Tail Assignment")
               self.tail=x
                    
     def display(self):
          values=[]
          n=self.head
          c = 0
          while n !=None:
               print ("Loop: " + str(c))
               values.append(str(n.value))
               n=n.next
               print (values[c])
               c = c+1
               
          print ("Stopping!")

     def getNode(self, value):
          n = self.head
          while True:
               if n.value == value:
                    return n
               n = n.next 
               
     def deleteNode(self, delNode):

          if delNode.prev != None:
               delNode.prev.next = delNode.next
          else:
               print ("Head has been reassigned!")
               self.head = delNode.next

          if delNode.next != None:
               delNode.next.prev = delNode.prev
          else:
               print ("Tail has been reassigned!")
               self.tail = delNode.prev
               
          print ("Node: " + str(delNode.value) + " Deleted.")
          delNode = None
     
if __name__ == '__main__':
     l=List()
     l.insert(None, Node(4))
     l.insert(l.head,Node(6))
     l.insert(l.head,Node(8))
     l.insert(l.head,Node(2))
     l.display()
     l.deleteNode(l.getNode(6))
     l.display()
