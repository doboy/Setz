# Copyright (c) 2013 Huan Do, http://huan.do

def is_empty(a):
  return len(a) == 0

def is_disjoint(*sets):
  t = set()
  t_count = 0
  for s in sets:
    t |= s
    if len(t) < t_count + len(s):
      return False
    t_count += len(s)
  return True

def product(*sets):
  cartesian_product = _product(((),), *sets)
  return '\n'.join(', '.join(row) for row in cartesian_product)

def _product(product_so_far, *sets):
  if len(sets) == 0:
    return product_so_far
  else:
    next_product_so_far = ()
    for x in product_so_far:
      for y in sets[0]:
        next_product_so_far += (x + (y,),)
    return _product(next_product_so_far, *sets[1:])

def power_set(a):
  subsets = _power_set(a)
  return '\n'.join(', '.join(subset) for subset in subsets)

def _power_set(a):
  a_list = list(a)
  subsets = []
  for bits in xrange(1, 2 ** len(a)):
    subset = []
    bit = 0
    while (1 << bit) <= bits:
      if bits & (1 << bit):
        subset.append(a_list[bit])
      bit += 1
    subsets.append(subset)
  return subsets

exports = {
  'is_empty': is_empty,
  'is_disjoint': is_disjoint,
  'power_set': power_set,
  'product': product
}
