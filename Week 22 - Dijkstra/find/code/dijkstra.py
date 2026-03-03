# create dijkstra's algorithm
import heapq
import math

def dijkstra(graph, start):
    # initialize distance and previous node dictionaries
    dist = {}
    prev = {}
    for node in graph:
        # set the distance to infinity and the previous node to none for all nodes
        dist[node] = math.inf
        prev[node] = None
    # set the distance to the starting node to zero
    dist[start] = 0
    # create a priority queue and add the starting node with its distance as priority
    pq = []
    heapq.heappush(pq, (dist[start], start))
    # main loop
    while len(pq) > 0:
        # get the node with the smallest distance from the priority queue
        d, node = heapq.heappop(pq)
        # update the distances of all the neighbors of the current node
        for neighbour in graph[node]:
            # calculate the tentative distance to the neighbor through the current node
            new_distance = dist[node] + graph[node][neighbour]
            # if the tentative distance is shorter than the current distance, update it
            if dist[neighbour] > new_distance:
                dist[neighbour] = new_distance
                prev[neighbour] = node
                # add the neighbor to the priority queue with its updated distance
                heapq.heappush(pq, (dist[neighbour], neighbour))
    
    # return the distance and previous node dictionaries
    return dist, prev

def main():
    # create graph
    graph = {}
    graph['s'] = {}
    graph['s']['a'] = 1
    graph['s']['b'] = 4
    graph['a'] = {}
    graph['a']['b'] = 2
    graph['a']['c'] = 6
    graph['b'] = {}
    graph['b']['c'] = 3
    graph['b']['d'] = 2
    graph['d'] = {}
    graph['d']['c'] = 1
    graph['d']['e'] = 4
    graph['c'] = {}
    graph['c']['e'] = 2
    graph['e'] = {}
    # run dijkstra's algorithm
    dist, prev = dijkstra(graph, 's')
    print(dist)
    print(prev)

    # add a second example
    graph = {}
    graph['a'] = {}
    graph['a']['b'] = 2
    graph['a']['c'] = 1
    graph['b'] = {}
    graph['b']['c'] = 2
    graph['b']['d'] = 1
    graph['c'] = {}
    graph['c']['d'] = 2
    graph['c']['e'] = 1
    graph['d'] = {}
    graph['d']['e'] = 2
    graph['d']['f'] = 1
    graph['e'] = {}
    graph['e']['f'] = 2
    graph['e']['g'] = 1
    graph['f'] = {}
    graph['f']['g'] = 2
    # add node g
    graph['g'] = {}
    

    # run dijkstra's algorithm
    dist, prev = dijkstra(graph, 'a')
    print(dist)
    print(prev)

if __name__ == '__main__':
    main()