from collections import deque

n, k = map(int, input().split())
li = list(map(int, input().split()))

q = deque()

while q:
    """bfs"""
