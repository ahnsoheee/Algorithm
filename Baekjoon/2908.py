#No.2908

import sys

A, B = map(int, sys.stdin.readline().split())

a = list(str(A))
b = list(str(B))

new_A = a[len(a)-1]
new_B = b[len(b)-1]

for i in range(len(a)-2, -1, -1):
    new_A += a[i]


for i in range(len(b)-2, -1, -1):
    new_B += b[i]

print(max(int(new_A), int(new_B)))
