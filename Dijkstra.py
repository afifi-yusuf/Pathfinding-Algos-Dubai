from time import perf_counter_ns
from queue import PriorityQueue
class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []


    def addEdge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight


def dijkstra(graph, start_vertex):
    D = {v: float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D


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
D = dijkstra(g, 0)
end = perf_counter_ns()
print("---%s nanoseconds ---" % (end-start))


print(D)
for vertex in range(len(D)):
    print("Distance from vertex 0 to vertex", vertex, "is", D[vertex])
