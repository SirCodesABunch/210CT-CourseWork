from queue import *

class Node():
    def __init__(self,value):
        self.value = value
        #self.edges now stores the weight/cost of the edges. [[LINKEDNODE,COST,GRAPH],[LINKEDNODE,COST,GRAPH]]
        self.edges = []
        self.tw = None

    def get_edges(self):
        return self.edges

    def update_Edges(self,G,X,C):
        self.edges.append([X,C,G])

    def get_value(self):
        return self.value


class Graph():
    def __init__(self):
        self.nodes = []

    def graph_Add_Node(self,N):
        self.nodes.append(N)

    def get_node_pointers(self,V):
        for i in range(0,len(self.nodes)):
            if self.nodes[i].get_value() == V:
                return self.nodes[i]
        

    def graph_Add_Edges(self,N,X,C):
        #Creates a Bi-Directional relationship between the two
        N = self.get_node_pointers(N)
        X = self.get_node_pointers(X)

        N.update_Edges(self,X,C)
        X.update_Edges(self,N,C)

    def dijkstra(self,src,d):
        c = src

        for i in range(0,len(self.nodes)):
            #in this case str - 8 means infinity
            self.nodes[i].tw = '8'

        src.tw = 0
        visited = []

        while c != d:
            for e in range(0,len(c.get_edges())):
                #if the tw of the current node  + the COST of one of its 'neighbour' nodes.
                if c.tw + c.get_edges()[e][1] < c.get_edges()[e][1]

        
        

    def depth_First_Search(self,N):
        s = []
        visted = []
        s.append(N)

        while len(s) != 0:
            '''as long as there is something in the stack check if it has been visited
            If it hasn't add it to the visited list
            if it HAS continue to the next elemnt
            When the stack is empty return the list of all the visited nodes
            '''
            if s[0] not in visted:
                visted.append(s[0])
                for e in range(0,len(s[0].get_edges())):
                    s.append(s[0].get_edges()[e][0])
            s.remove(s[0])

        #Handles writing the results to a file
        f = open('DFS.txt','w')
        for i in range(0,len(visted)):
            f.write("Node:\t" + str(visted[i].get_value())+ "\n")
        f.close()
        return visted

    def breath_First_Search(self,N):
        q = Queue(maxsize=0)
        visited = []
        q.put(N)
        while q.empty() != True:
            '''
            node N is parsed in set as the first (and last) elemnt of a queue
            while the queue isn't empty it checks if the last element of the queue
            is in visited if it isn't it adds it to visited and then runs a loop to get
            all of that node's edges and puts them into the queue.
            if the node has already been visited the loop continues to the next node.
            '''
            c = q.get()
            if c not in visited:
                visited.append(c)
                for e in range(0,len(c.get_edges())):
                    q.put(c.get_edges()[e][0])

        #Handles writing the results to a file
        f = open('BFS.txt','w')
        for i in range(0,len(visited)):
            f.write("Node:\t" + str(visited[i].get_value())+ "\n")
        f.close()

        return visited




g = Graph()

g.graph_Add_Node(Node(1))
g.graph_Add_Node(Node(2))
g.graph_Add_Node(Node(3))
g.graph_Add_Node(Node(4))


g.graph_Add_Edges(1,2,2)
g.graph_Add_Edges(2,3,6)
g.graph_Add_Edges(3,4,9)
g.graph_Add_Edges(2,4,8)

g.depth_First_Search(g.get_node_pointers(1))
g.breath_First_Search(g.get_node_pointers(1))

