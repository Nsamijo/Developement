def mapFilter(predicate, generator, current, threshold):
  print()
  currentTransformed = generator(current)
  if current > threshold:
    return ''
  else:
    if predicate(currentTransformed):
      return str(currentTransformed) + ' ' + mapFilter(predicate, generator, current + 1, threshold)
    return mapFilter(predicate, generator, current + 1, threshold)
threshold = 20
predicate1 = lambda x: x % 2 == 0
predicate2 = lambda x: x % 3 == 0
print()
res = mapFilter(predicate1, lambda n: n * 3, 1, threshold)
print()