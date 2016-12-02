
class Node():
    def __init__(self,value):
        self.value = value
        self.edges = []

    def update_Edges(self,G,X):
        self.edges.append([X,G])

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
        

    def graph_Add_Edges(self,N,X):
        #Creates a Bi-Directional relationship between the two
        N = self.get_node_pointers(N)
        X = self.get_node_pointers(X)

        N.update_Edges(self,X)
        X.update_Edges(self,N)

        



g = Graph()

g.graph_Add_Node(Node(1))
g.graph_Add_Node(Node(2))
g.graph_Add_Node(Node(3))
g.graph_Add_Node(Node(4))


g.graph_Add_Edges(1,2)
g.graph_Add_Edges(2,3)
g.graph_Add_Edges(3,4)
g.graph_Add_Edges(2,4)
