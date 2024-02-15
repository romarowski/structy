"""
longest path

Write a function, longest_path, that takes in an adjacency list for a 
directed acyclic graph. The function should return the length of the 
longest path within the graph. A path may start and end at any two nodes. 
The length of a path is considered the number of edges in the path, 
not the number of nodes.
"""

def longest_path(graph):
    # sounds like a DFS problem
    # I need to go to any given node 
    # and go to the end
    # store how many edges I passed to get to that node
    visited = dict()
    for node in graph:
        if graph[node] == []:
            visited[node] = 0
    for node in graph:
        explore(node, graph, visited)

    return max(visited.values())

def explore(node, graph, visited):

    if node in visited:
        return visited[node]


    largest = 0
    for neighbor in graph[node]:
        path = explore(neighbor, graph, visited)
        if path > largest:
            largest = path
    visited[node] = 1 +largest
    return visited[node]




graph = {
  'a': ['c', 'b'],
  'b': ['c'],
  'c': []
}

print(longest_path(graph)) # -> 2