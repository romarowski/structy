def subsets(elements):
  if len(elements) == 0:
    return [[]]
    
  first = elements[0]
  remaining_elements = elements[1:]
  subsets_without_first = subsets(remaining_elements)
  
  subsets_with_first = []
  for sub in subsets_without_first:
    subsets_with_first.append([first, *sub])
  
  return subsets_without_first + subsets_with_first


print(subsets(["a", "b", "c"]))