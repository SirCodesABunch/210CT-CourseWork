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
               x.next=n.next
               n.next=x
               x.prev=n
               if x.next!=None:
                    x.next.prev=x
               if self.head==None:
                    self.head=self.tail=x
                    x.prev=x.next=None
               elif self.tail==n:
                    self.tail=x
     def display(self):
          values=[]
          n=self.head
          while n!=None:
               values.append(int(n.value))
               n=n.next
               print (values)

     def deleteNode(self, delNode):
          if delNode.next != None:
               delNode.next.prev = delNode.prev
          else:
               print ("Tail has been reassigned!")
               self.tail = delNode.prev
          if delNode.prev != None:
               delNode.prev = delNode.next
          else:
               print ("Head has been reassigned!")
               self.head = delNode.next

          print ("Node: " + int(delNode.value) + " Deleted.")
          delNode = None

                      

            
          
if __name__ == '__main__':
     l=List()
     l.insert(None, Node(4))
     l.insert(l.head,Node(6))
     l.insert(l.head,Node(8))
     l.display()