"""1991.py
Title: 트리 순회
Url: https://www.acmicpc.net/problem/1991
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write


def preorder(tree, node="A"):
    print = sys.stdout.write
    print(node)
    l_child, r_child = tree[node]
    if l_child != ".":
        preorder(tree, l_child)
    if r_child != ".":
        preorder(tree, r_child)


def inorder(tree, node="A"):
    print = sys.stdout.write
    l_child, r_child = tree[node]
    if l_child != ".":
        inorder(tree, l_child)
    print(node)
    if r_child != ".":
        inorder(tree, r_child)


def postorder(tree, node="A"):
    print = sys.stdout.write
    l_child, r_child = tree[node]
    if l_child != ".":
        postorder(tree, l_child)
    if r_child != ".":
        postorder(tree, r_child)
    print(node)


N = int(input())

tree = {}
for _ in range(N):
    node, l_child, r_child = input().split()
    tree[node] = (l_child, r_child)

preorder(tree)
print("\n")
inorder(tree)
print("\n")
postorder(tree)
print("\n")
