import pdb
def connected_components_count(graph):
  count = 0
  if not graph:
    return count
  all_nodes = set(graph.keys())
  visited = set()
  while len(visited) != len(graph):    
    remaining_nodes = all_nodes-visited
    node1 = remaining_nodes.pop()
    stack = [node1]
    while len(stack)>0:
      current = stack.pop()
      #print(stack)
      print(current)
      visited.add(current)
      for node in graph[current]:
        if (node not in visited) and (node not in stack):
          stack.append(node)
    count+=1      
 
  return count

if __name__ == '__main__':
    connected_components_count({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
})
