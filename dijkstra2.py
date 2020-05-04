
from collections import deque, namedtuple

import os

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

            final_cost=distances[neighbour]
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
        
        mode = 'w'
        path, cost =graph.dijkstra(src,destination)
       
        with open(writepath, mode) as f:
            f.write('->'.join(path))# create/overwrite a txt file and print the shortest path
            f.write("\nTotal cost to the destination " + str(cost))# print the total cost to the destination
            
        f.close()
    
    #Sample graph, must find way to create topology as graph
    def read(self,src,dest):
        fileDir = os.path.dirname(os.path.abspath(__file__))
        f = open(fileDir+'/'+'graphs'+'/'+src+"_"+dest+".txt", "r")
        re= f.readline()
        print(re)
    # new_str = re.replace('->', '') 
        array = re.split("->")
        print(array)
        str1 = ''.join(array)
        print(str1)
        dict={"ab":7,"ba":7, "ac":9,"ca":9, "af":14,"fa":14, "bc":10,"cb":10,"bd":15,"db":15, "cd":11,"dc":11, "cf":2,"fc":2,  "de": 6,"ed": 6}
        sum =0
        str1 = str1.rstrip(' \t\r\n\0')
        for i in range(0, len(str1)-1):
            d=dict.get(str1[i]+str1[i+1])
            print(d)
            sum=sum+d
          
    
 

        return sum

if __name__== "__main__":
    graph = Graph([("a", "b", 7),("b", "a", 7), ("a", "c", 9),("c", "a", 9),  ("a", "f", 14),("f", "a", 14), ("b", "c", 10),("c", "b", 10),("b", "d", 15), ("d", "b", 15),("c", "d", 11),("d", "c", 11), ("c", "f", 2), ("f", "c", 2), ("d", "e", 6), ("e", "d", 6)])




    graph.test("a","b")
    graph.test("a","c")
    graph.test("a","d")
    graph.test("a","e")
    graph.test("a","f")

    graph.test("b","a")
    graph.test("b","c")
    graph.test("b","d")
    graph.test("b","e")
    graph.test("b","f")

    graph.test("c","a")
    graph.test("c","b")
    graph.test("c","d")
    graph.test("c","e")
    graph.test("c","f")

    graph.test("d","a")
    graph.test("d","b")
    graph.test("d","c")
    graph.test("d","e")
    graph.test("d","f")

    graph.test("e","a")
    graph.test("e","b")
    graph.test("e","c")
    graph.test("e","d")
    graph.test("e","f")

    print(graph.read("a","e"))


