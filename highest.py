def min_max(lst):
  min = lst[0]
  max = lst[0]
  if len(lst) == 1:
     return [lst[0],lst[0]]
  for x in lst:
     if x < min:
        min = x
  for x in lst:
     if x > max:
        max = x 
  return [min,max]
