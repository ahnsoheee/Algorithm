#No.1181

import sys

N = int(sys.stdin.readline())
strings = []

for _ in range(N):
  word = input()
  strings.append((word, len(word)))
  
strings = list(set(strings))
strings = sorted(strings, key = lambda x:(x[1], x[0]))

for string in strings:
  print(string[0])