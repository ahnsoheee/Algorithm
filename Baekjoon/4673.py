#No. 4673

import sys

self_num = []

for i in range(10000):
    self_num.append(i+1)

for i in range(1, 10001):
    num = list(str(i))

    for j in range(len(num)):
        num[j] = int(num[j])

    if i + sum(num) in self_num:   
        self_num.remove(i + sum(num)) 

for i in range(len(self_num)):
    print(self_num[i])
