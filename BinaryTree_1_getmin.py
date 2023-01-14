#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
애플에서 출제된 문제입니다.

주어진 이진 트리에서, 루트 (최상위 노드) 에서 리프 (자식이 없는 최하위 노드) 까지의 경로를 모두 더하였을 떄 가장 작은 값을 갖는 경로를 찾고, 그 합을 반환하세요.

예를 들어, 이 트리에서 최소 값을 갖는 경로는 [10, 5, 1, -1] 이며, 그 합인 15를 반환해야 합니다.

  10
 /  \
5    5
 \     \
   2    1
       /
     -1
"""

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left=left
        self.right=right
    def __str__(self):
        return f'<node: value={self.value}, left={self.left}, right={self.right}>'

"""
  10
 /  \
5    5
 \     \
   2    1
       /
     -1
"""

def path1():
    n43 = Node(-1, None, None)
    n32 = Node(2, None, None)
    n34 = Node(1, n43, None)
    n21 = Node(5, None, n32)
    n22 = Node(5, None, n34)
    n11 = Node(10, n21, n22)

    return n11

"""
             2
       /          \
       8           -4
    /    \        /    \
  -2      4       3      1
    \    /  \    /         \
     2   10  4  -9          4
       /
     -13
"""
def path2():

    n55 = Node(-13, None, None)
    n48 = Node( 4,  None, None)
    n45 = Node(-9,  None, None)
    n44 = Node( 4,  None, None)
    n43 = Node( 10, n55,  None)
    n42 = Node( 2,  None, None)
    n34 = Node( 1,  None,  n48)
    n33 = Node( 3,  n45,  None)
    n32 = Node( 4,  n43,  n44)
    n31 = Node(-2,  None, n42)
    n22 = Node(-4,  n33,  n34)
    n21 = Node( 8,  n31,  n32)
    n11 = Node( 2,  n21,  n22)

    return n11

def RNL(node):

    if node.right != None:
        right = RNL(node.right)
    else:
        right = 0

    if node.left != None:
        left = RNL(node.left)
    else:
        left = 0

    return (node.value + left) if left < right else (node.value + right)

if __name__=="__main__":
    paths = [path1(), path2()]

    for path in paths:
        print(f'result = {RNL(path)}')
