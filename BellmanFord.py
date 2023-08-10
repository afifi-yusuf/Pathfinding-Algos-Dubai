
# shortest path algorithm.
from time import perf_counter_ns

# Class to represent a graph
class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # utility function used to print the solution
    def printArr(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

    # The main function that finds shortest distances from src to
    # all other vertices using Bellman-Ford algorithm. The function
    # also detects negative weight cycle
    def BellmanFord(self, src):

        # Step 1: Initialize distances from src to all other vertices
        # as INFINITE
        dist = [float("Inf")] * self.V
        dist[src] = 0

        # Step 2: Relax all edges |V| - 1 times. A simple shortest
        # path from src to any other vertex can have at-most |V| - 1
        # edges
        #write a function that returns true if there is a negative weight cycle
        def negative_weight_cycle():
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    return True
            return False

        for _ in range(self.V - 1):
            # Update dist value and parent index of the adjacent vertices of
            # the picked vertex. Consider only those vertices which are still in
            # queue
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Step 3: check for negative-weight cycles. The above step
        # guarantees shortest distances if graph doesn't contain
        # negative weight cycle. If we get a shorter path, then there
        # is a cycle.

        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return

        # print all distance
        self.printArr(dist)

g = Graph(8)
g.addEdge(0, 1, 5.2)
g.addEdge(0, 2, 13.5)
g.addEdge(1, 2, 9.7)
g.addEdge(1, 3, 20.5)
g.addEdge(2,4,14.8)
g.addEdge(4,1,5.4)
g.addEdge(4,3,24.8)
g.addEdge(4,5,11.5)
g.addEdge(5,2,18.3)
g.addEdge(0,6,9.8)
g.addEdge(3,7,16.9)
g.addEdge(7,1,9.2)
g.addEdge(1,8,17.4)
g.addEdge(8,6,13.9)
g.addEdge(9,5,18.6)
g.addEdge(2,9,8.7)
g.addEdge(10,4,21.1)
g.addEdge(7,10,9.9)
g.addEdge(11,0,22.9)
g.addEdge(6,11,12.9)
g.addEdge(12,8,27.7)
g.addEdge(3,12,12.7)
g.addEdge(13,11,5.5)
g.addEdge(10,13,14.8)
g.addEdge(14,2,16.9)
g.addEdge(1,14,17.9)
g.addEdge(15,3,12.8)
g.addEdge(9,15,16.8)
g.addEdge(16,10,5.9)
g.addEdge(14,16,9)
g.addEdge(17,5,18)
g.addEdge(6,17,4.7)
g.addEdge(7,18,13.6)
g.addEdge(18,8,29.9)
g.addEdge(19,16,10.9)
g.addEdge(9,19,10.9)

start = perf_counter_ns()
g.BellmanFord(0)
end = perf_counter_ns()
print("---%s nanoseconds ---" % (end-start))


# Initially, Contributed by Neelam Yadav
# Later On, Edited by Himanshu Garg