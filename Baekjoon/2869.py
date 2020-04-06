#No.2869

import sys, math

A, B, V = map(int, sys.stdin.readline().split())

print(math.ceil((V-B) / (A-B)))
