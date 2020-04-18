#No.5585 '거스름 돈'

#1
import sys

c = int(sys.stdin.readline())

res = 0

r = 1000 - c

while(r != 0):
    if (r // 500) > 0:
        res += (r // 500)
        r = r % 500

    else:
        if (r // 100) > 0:
            res += (r // 100)
            r = r % 100

        else:
            if (r // 50) > 0:
                res += (r // 50)
                r = r % 50

            else:
                if (r // 10) > 0:
                    res += (r // 10)
                    r = r % 10
                
                else:
                    if (r // 5) > 0:
                        res += (r // 5)
                        r = r % 5

                    else:
                        res += (r // 1)
                        r = r % 1
    
print(res)

#2
import sys

c = int(sys.stdin.readline())

res = 0

r = 1000 - c

coin = [500, 100, 50, 10, 5, 1]

for i in range(6):
    res += (r // coin[i])
    r = r % coin[i]

print(res)
