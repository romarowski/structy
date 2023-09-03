import pdb
def connected_components_count(graph):
  count = 0
  if not graph:
    return count
  all_nodes = set(graph.keys())
  node1 = all_nodes.pop()
  visited = {node1}
  stack = [node1]
  #while len(visited) != len(graph):    
  while len(stack)>0:
    current = stack.pop()
    visited.add(current)
    for node in graph[current]:
      if (node not in visited) and (node not in stack):
        stack.append(node)
        pdb.set_trace()
    print(current)
    print(stack)
    print(visited)
  count+=1      
  remaining_nodes = all_nodes-visited
  node1 = remaining_nodes.pop()
  stack = [node1]
 
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
