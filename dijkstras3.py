from collections import deque, namedtuple

from variables import * # imports all the variables for the network



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
            
            

            total_cost=distances[dest] #total cost to destination
            # print(distances) cost to each node
            path, current_vertex = deque(), dest
            while previous_vertices[current_vertex] is not None:
                path.appendleft(current_vertex)
                current_vertex = previous_vertices[current_vertex]
                
            if path:
                path.appendleft(current_vertex)
            return path, total_cost

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
    # graph = Graph([("s1", "r1"),("r1", "r2"), ("r2", "r4"), ("r4", "r7"),("r7", "d1"), ("r2", "r3"), ("r1", "r3"), ("r3", "r5"), ("r3", "r6"),  ("r5", "d2"), ("r6", "d3" )])
    # graph.test("s1","d3")
    # graph = Graph([(str(s1.id),str(r1.id),1)],(str(r1.id),str(r2.id),1))
    
    graph= Graph([(s1.id,r1.id),(r1.id,r2.id),(r1.id,r3.id),(r3.id,r5.id),(r2.id,r4.id),(r4.id, d1.id), (r3.id, r4.id), (r5.id, r6.id), (r6.id, d2.id),  (r6.id, d3.id), (r6.id ,d3.id)])
    graph.test(s1.id,d1.id)
    graph.test(s1.id,d2.id)
    graph.test(s1.id,d3.id)
'''
    graph.test(r1.id,r2.id)
    graph.test(r1.id,r3.id)
    graph.test(r1.id,r4.id)
    graph.test(r1.id,r5.id)
    graph.test(r1.id,r6.id)
    graph.test(r1.id,r7.id)
    graph.test(r1.id,d1.id)
    graph.test(r1.id,d2.id)
    graph.test(r1.id,d3.id)
    graph.test(r2.id,r3.id)
    graph.test(r2.id,r4.id)
    graph.test(r2.id,r5.id)
    graph.test(r2.id,r6.id)
    graph.test(r2.id,r7.id)
    graph.test(r2.id,d1.id)
    graph.test(r2.id,d2.id)
    graph.test(r2.id,d3.id)
'''
