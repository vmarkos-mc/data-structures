# create the a star algorithm
import heapq
import math

# pass in the heuristic function as a parameter
def a_star(graph, start, goal, heuristic):
    # initialize
    dist = {}
    prev = {}
    for node in graph:
        dist[node] = math.inf
        prev[node] = None
    dist[start] = 0
    # create priority queue
    pq = []
    heapq.heappush(pq, (dist[start], start))
    # main loop
    while len(pq) > 0:
        # get the node with the smallest distance
        d, node = heapq.heappop(pq)

        if node == goal:
            return dist, prev

        # update the distance of all the neighbours based on the heuristic
        for neighbour in graph[node]:
            if dist[neighbour] > dist[node] + graph[node][neighbour]:
                dist[neighbour] = dist[node] + graph[node][neighbour]
                prev[neighbour] = node
                heapq.heappush(pq, (dist[neighbour] + heuristic(neighbour, goal), neighbour))
                
    return None  # goal not found

# create a function to reconstruct the path
def reconstruct_path(prev, start, goal):
    # initialize
    path = []
    # start at the goal
    node = goal
    # loop until we reach the start
    while node != start:
        # add the current node to the path
        path.append(node)
        # update the current node
        node = prev[node]
    # add the start node to the path
    path.append(start)
    # reverse the path
    path.reverse()
    return path

def heuristic_manhattan(node, goal):
    # calculate the manhattan distance
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def heuristic_euclidean(node, goal):
    # calculate the euclidean distance
    return math.sqrt((node[0] - goal[0]) ** 2 + (node[1] - goal[1]) ** 2)

def main():
    # create graph
    graph = {}
    graph[(0,0)] = {}
    graph[(0,0)][(0,1)] = 1
    graph[(0,0)][(1,0)] = 1
    graph[(0,1)] = {}
    graph[(0,1)][(0,0)] = 1
    graph[(0,1)][(0,2)] = 1
    graph[(0,2)] = {}
    graph[(0,2)][(0,1)] = 1
    graph[(0,2)][(0,3)] = 1
    graph[(0,3)] = {}
    graph[(0,3)][(0,2)] = 1
    graph[(0,3)][(1,3)] = 1
    graph[(1,0)] = {}
    graph[(1,0)][(0,0)] = 1
    graph[(1,0)][(2,0)] = 1
    graph[(1,1)] = {}
    graph[(1,1)][(1,2)] = 1
    graph[(1,1)][(2,1)] = 1
    graph[(1,2)] = {}
    graph[(1,2)][(1,1)] = 1
    graph[(1,2)][(1,3)] = 1
    graph[(1,2)][(2,2)] = 1
    graph[(1,3)] = {}
    graph[(1,3)][(0,3)] = 1
    graph[(1,3)][(1,2)] = 1
    graph[(1,3)][(2,3)] = 1
    graph[(2,0)] = {}
    graph[(2,0)][(1,0)] = 1
    graph[(2,0)][(3,0)] = 1
    graph[(2,1)] = {}
    graph[(2,1)][(1,1)] = 1
    graph[(2,1)][(2,2)] = 1
    graph[(2,1)][(3,1)] = 1
    graph[(2,2)] = {}
    graph[(2,2)][(1,2)] = 1
    graph[(2,2)][(2,1)] = 1
    graph[(2,2)][(2,3)] = 1
    graph[(2,2)][(3,2)] = 1
    graph[(2,3)] = {}
    graph[(2,3)][(1,3)] = 1
    graph[(2,3)][(2,2)] = 1
    graph[(2,3)][(3,3)] = 1
    graph[(3,0)] = {}
    graph[(3,0)][(2,0)] = 1
    graph[(3,0)][(3,1)] = 1
    graph[(3,1)] = {}
    graph[(3,1)][(2,1)] = 1
    graph[(3,1)][(3,0)] = 1
    graph[(3,1)][(3,2)] = 1
    graph[(3,2)] = {}
    graph[(3,2)][(2,2)] = 1
    graph[(3,2)][(3,1)] = 1
    graph[(3,2)][(3,3)] = 1
    graph[(3,3)] = {}
    graph[(3,3)][(2,3)] = 1
    graph[(3,3)][(3,2)] = 1


    # run the algorithm
    dist, prev = a_star(graph, (0, 0), (3, 3), heuristic_euclidean)
    print(f"dist: \n\n{dist}\n")
    print(f"prev: \n\n{prev}\n")
    print(f"path: \n\n{reconstruct_path(prev, (0, 0), (3, 3))}\n")


    # run the algorithm
    dist, prev = a_star(graph, (0, 0), (3, 3), heuristic_manhattan)
    print(f"dist: \n\n{dist}\n")
    print(f"prev: \n\n{prev}\n")
    print(f"path: \n\n{reconstruct_path(prev, (0, 0), (3, 3))}\n")


    
if __name__ == "__main__":
    main() 

