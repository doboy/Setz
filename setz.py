#!/usr/bin/python
# Copyright (c) 2013 Huan Do, http://huan.do
"""
Queries set operators from files using python syntax

Usage:
  setz "query" [a.txt b.txt ..]

  --help for more info
"""

import sys

import setz_funcs

def usage():
  print __doc__

def help():
  print """
Possible Queries:
  Set Membership. Test if an element belongs to a set.
    "'test' in a"
  Set Equality. Test if two sets contain the same elements.
    "a == b"
  Set Cardinality. Return the number of elements in the set.
    "len(a)"
  Subset Test. Test if a given set is a subset of another set.
    "a < b"
  Set Union. Find union of two sets.
    "a | b"
  Set Intersection. Find intersection of two sets.
    "a & b"
  Set Complement. Given two sets A and B, find all elements in A that are not in B.
    "a - b"
  Set Symmetric Difference. Find symmetric difference of two sets.
    "a ^ b"
  Power Set. Generate all subsets of a set.
    "power_set(a)"
  Set Cartesian Product. Find A x B.
    "a * b * .."
  Disjoint Set Test. Test if two sets are disjoint.
    "is_disjoint(a, b, ..)"
  Empty Set Test. Test if a given set is empty.
    "is_empty(a)"
  Minimum. Find the smallest element of a set.
    "max(a)"
  Maximum. Find the largest element of a set.
    "min(a)"

Examples:
  > setz 'a | b' <(echo foo) <(echo baz garply)
  garply
  foo
  baz
  > setz 'max(a)' <(echo 9001 10)
  9001
  """

def parse_arguments(args):
  query = args[1]
  input_filepaths = args[2:]
  sets_map = {}
  for i, input_filepath in enumerate(input_filepaths):
    letter = chr(ord('a') + i)
    sets_map[letter] = set(open(input_filepath).read().split())
  return query, sets_map

def evaluate_query(query, sets_map):
  globals = {}
  globals.update(sets_map)
  globals.update(setz_funcs.exports)
  result = eval(query, globals)
  display_result(result)

def display_result(result):
  if isinstance(result, set):
    print '\n'.join(result)
  elif isinstance(result, bool):
    print int(result)
  else:
    print result

def main():
  if '--help' in sys.argv:
    help()

  elif len(sys.argv) < 2:
    usage()
    exit(1)

  else:
    query, sets_map = parse_arguments(sys.argv)
    evaluate_query(query, sets_map)

if __name__ == '__main__':
  main()
