# # Sorting Network = just rotate trees!
# def sort(d, s, tree):
#   switch d:
#     case 0:
#       return tree
#     case _:
#       (x,y) = tree
#       lft   = sort(d-1, 0, x)
#       rgt   = sort(d-1, 1, y)
#       return rots(d, s, (lft, rgt))

# # Rotates sub-trees (Blue/Green Box)
# def rots(d, s, tree):
#   switch d:
#     case 0:
#       return tree
#     case _:
#       (x,y) = tree
#       return down(d, s, warp(d-1, s, x, y))

# # Swaps distant values (Red Box)
# def warp(d, s, a, b):
#   switch d:
#     case 0:
#       return swap(s ^ (a > b), a, b)
#     case _:
#       (a.a, a.b) = a
#       (b.a, b.b) = b
#       (A.a, A.b) = warp(d-1, s, a.a, b.a)
#       (B.a, B.b) = warp(d-1, s, a.b, b.b)
#       return ((A.a,B.a),(A.b,B.b))

# # Propagates downwards
# def down(d,s,t):
#   switch d:
#     case 0:
#       return t
#     case _:
#       (t.a, t.b) = t
#       return (rots(d-1, s, t.a), rots(d-1, s, t.b))

# # Swaps a single pair
# def swap(s, a, b):
#   switch s:
#     case 0:
#       return (a,b)
#     case _:
#       return (b,a)

# # Testing
# # -------

# # Generates a big tree
# def gen(d, x):
#   switch d:
#     case 0:
#       return x
#     case _:
#       return (gen(d-1, x * 2 + 1), gen(d-1, x * 2))

# # Sums a big tree
# def sum(d, t):
#   switch d:
#     case 0:
#       return t
#     case _:
#       (t.a, t.b) = t
#       return sum(d-1, t.a) + sum(d-1, t.b)

# # Sorts a big tree
# def main:
#   return sum(20, sort(20, 0, gen(20, 0)))


# def numbers():
#   total = 0
#   for i in range(10)
#     total += i
#   return total
#   # bend idx = 0:
#   #   when idx < 10:
#   #     sum = idx + fork(idx + 1)
#   #   else:
#   #     sum = 0
#   return Nil


# def strings():
#   strings1 = "foo"
#   strings2 = "bar"
#   return strings1

# def main:
#   return numbers()
#   # return strings()


# type Tree:
#   Node { ~lft, ~rgt }
#   Leaf { val }

# def sum(tree):
#   fold tree:
#     case Tree/Node:
#       return tree.lft + tree.rgt
#     case Tree/Leaf:
#       return tree.val

# def main:
#   tree = Tree/Node {
#     lft: Tree/Node { lft: Tree/Leaf { val: 1 }, rgt: Tree/Leaf { val: 2 } },
#     rgt: Tree/Node { lft: Tree/Leaf { val: 3 }, rgt: Tree/Leaf { val: 4 } }
#   }
#   return sum(tree)



# type Tree:
#   Node { ~lft, ~rgt }
#   Leaf { val }

# def enum(tree):
#   idx = 0
#   fold tree with idx:
#     case Tree/Node:
#       return Tree/Node {
#         lft: tree.lft(idx * 2 + 0),
#         rgt: tree.rgt(idx * 2 + 1),
#       }
#     case Tree/Leaf:
#       return Tree/Leaf { val: (idx, tree.val) }

# def main:
#   tree = Tree/Node {
#     lft: Tree/Node { lft: Tree/Leaf { val: 1 }, rgt: Tree/Leaf { val: 2 }, },
#     rgt: Tree/Node { lft: Tree/Leaf { val: 3 }, rgt: Tree/Leaf { val: 4 }, }
#   }
#   return enum(tree)


def reverse(list):
  fold list:
    case List/Nil:
      return List/Nil
    case List/Cons:
      return List/Cons{ head: reverse(list.tail), tail: list.head}
  # bend d = 0, i = 0:
  #   when d < 28:
  #     sum = fork(d+1, i*2+0) + fork(d+1, i*2+1)
  #   else:
  #     sum = i
  # return sum

def main:
  return reverse([1,2,3])