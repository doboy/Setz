Setz
====

Setz is a command line utility used to run set operations on files using python syntax

Installation
------------
```
pip install setz
```

Usage
-----
```
setz "query" [a.txt b.txt ..]
```

Possible Queries
----------------
Set Membership. Test if an element belongs to a set.

`"'test' in a"`

Set Equality. Test if two sets contain the same elements.

`"a == b"`

Set Cardinality. Return the number of elements in the set.

`"len(a)"`

Subset Test. Test if a given set is a subset of another set.

`"a < b"`

Set Union. Find union of two sets.

`"a | b"`

Set Intersection. Find intersection of two sets.

`"a & b"`

Set Complement. Given two sets A and B, find all elements in A that are not in B.

`"a - b"`

Set Symmetric Difference. Find symmetric difference of two sets.

`"a ^ b"`

Power Set. Generate all subsets of a set.

`"power_set(a)"`

Set Cartesian Product. Find A x B.

`"product(a, b, ..)"`

Disjoint Set Test. Test if two sets are disjoint.

`"is_disjoint(a, b, ..)"`

Empty Set Test. Test if a given set is empty.

`"is_empty(a)"`

Minimum. Find the smallest element of a set.

`"max(a)"`

Maximum. Find the largest element of a set.

`"min(a)"`

Examples
--------
```
> setz '"foo" in a' <(echo foo)
1
> setz 'len(a)' <(echo for bar garply)
3
> setz 'a < b' <(echo foo bar baz) <(echo foo bar)
0
> setz 'max(a)' <(echo 9001 10)
9001
> setz 'is_disjoint(a, b, c)' <(echo foo) <(echo bar)   <(echo baz garply)
1
> setz 'a | b' <(echo foo) <(echo baz garply)
garply
foo
baz
> setz 'product(a, b)' <(echo foo bar) <(echo baz garply)
foo, garply
foo, baz
bar, garply
bar, baz
> setz 'power_set(a)' <(echo foo bar garply)
garply
foo
garply, foo
bar
garply, bar
foo, bar
garply, foo, bar
```