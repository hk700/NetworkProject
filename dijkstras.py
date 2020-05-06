from collections import deque, namedtuple
from nodes import Nodes

def makeNode(ip,id,port):
    n = Nodes(ip,id,port)
    return n

s1 =makeNode("192.168.1.1","s1",8881)
r1 =makeNode(("192.168.1.2","10.0.1.0","10.0.2.0"),"r1",8882)
r2 =makeNode(("10.0.1.1","10.0.3.1","10.0.4.1"),"r2",8883)
r3 =makeNode(("10.0.2.1","10.0.3.2","10.0.5.1","10.0.6.1"),"r3",8884)
r4 =makeNode(("10.0.4.2","10.0.7.1"),"r4",8885)
r5 =makeNode(("10.0.5.2","192.168.3.2"),"r5",8886)
r6 =makeNode(("10.0.6.2","192.168.4.2"),"r6",8887)
r7 =makeNode(("10.0.7.2","192.168.2.2"),"r7",8888)
d1 =makeNode("192.168.2.1","d1",8889)
d2 =makeNode("192.168.3.1","d2",8890)
d3 =makeNode("192.168.4.1","d3",8891)


# we'll use infinity as a default distance to nodes.
inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')


def make_edge(start, end, cost=1):
  return Edge(start, end, cost)


class Graph:
    def __init__(self, edges):
        # let's check that the data is right
        wrong_edges = [i for i in edges if len(i) not in [2, 3]]
        if wrong_edges:
            raise ValueError('Wrong edges data: {}'.format(wrong_edges))

        self.edges = [make_edge(*edge) for edge in edges]

    @property
    def vertices(self):
        return set(
            sum(
                ([edge.start, edge.end] for edge in self.edges), []
            )
            
        )

    def get_node_pairs(self, n1, n2, both_ends=True):
        if both_ends:
            node_pairs = [[n1, n2], [n2, n1]]
        else:
            node_pairs = [[n1, n2]]
        return node_pairs

    def remove_edge(self, n1, n2, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)

    def add_edge(self, n1, n2, cost=1, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                return ValueError('Edge {} {} already exists'.format(n1, n2))

        self.edges.append(Edge(start=n1, end=n2, cost=cost))
        if both_ends:
            self.edges.append(Edge(start=n2, end=n1, cost=cost))

    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))

        return neighbours

    def dijkstra(self, source, dest):
            assert source in self.vertices, 'Such source node doesn\'t exist'

            # 1. Mark all nodes unvisited and store them.
            # 2. Set the distance to zero for our initial node
            # and to infinity for other nodes.
            distances = {vertex: inf for vertex in self.vertices}
            
            previous_vertices = {
                vertex: None for vertex in self.vertices
            }
            distances[source] = 0
            vertices = self.vertices.copy()

            while vertices:
                # 3. Select the unvisited node with the smallest distance,
                # it's current node now.
                current_vertex = min(
                    vertices, key=lambda vertex: distances[vertex])

                # 6. Stop, if the smallest distance
                # among the unvisited nodes is infinity.
                if distances[current_vertex] == inf:
                    break

                # 4. Find unvisited neighbors for the current node
                # and calculate their distances through the current node.
                for neighbour, cost in self.neighbours[current_vertex]:
                    alternative_route = distances[current_vertex] + cost

                    # Compare the newly calculated distance to the assigned
                    # and save the smaller one.
                    if alternative_route < distances[neighbour]:
                        distances[neighbour] = alternative_route
                        previous_vertices[neighbour] = current_vertex
                        
                        
                
                        

                # 5. Mark the current node as visited
                # and remove it from the unvisited set.
                vertices.remove(current_vertex)
            
            

            final_cost=distances[dest]
            path, current_vertex = deque(), dest
            while previous_vertices[current_vertex] is not None:
                path.appendleft(current_vertex)
                current_vertex = previous_vertices[current_vertex]
                
            if path:
                path.appendleft(current_vertex)
            return path, final_cost

    def test(self,src,destination):
        import os
        import pathlib
    

        #absFilePath = os.path.abspath(__file__)
       # print(absFilePath)
        fileDir = os.path.dirname(os.path.abspath(__file__))
    
        writepath = fileDir+'/'+'graphs'+'/'+src+'_'+destination+'.txt'
       # print(writepath)
        path, cost = graph.dijkstra(src,destination)
        print(path)
        print(cost)
    
        mode = 'w'
        
        with open(writepath, mode) as f:
            f.write('->'.join(path))# create/overwrite a txt file and print the shortest path
            f.write("\nTotal cost to the destination " + str(cost))# print the total cost to the destination
            
        f.close()
    
    #Sample graph, must find way to create topology as graph

if __name__== "__main__":
    graph = Graph([("s1", "r1", 1),("r1", "r2", 1), ("r2", "r4", 1), ("r4", "r7", 1),("r7", "d1", 1), ("r2", "r3", 1), ("r1", "r3",1), ("r3", "r5", 1), ("r3", "r6", 1),  ("r5", "d2", 1), ("r6", "d3", 1)])
    
    graph.test("s1","d3")
    graph.test("s1","d1")
    graph.test("s1","d2")
    graph.test("r3","d3")
