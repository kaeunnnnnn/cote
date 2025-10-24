# 백준 1546번 #
import sys
input = sys.stdin.readline

n = int(input())
scores = list(map(int, input().split()))
m = max(scores)

ans = sum(scores) * 100 / (m*n)
print(f"{ans:.6f}")