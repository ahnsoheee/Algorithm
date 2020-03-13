#No.6378

import sys


while(1):
    num = int(sys.stdin.readline())

    if num == 0: 
        break
    
    while(1):
        num = sum(list(map(int, str(num))))

        if(num // 10 == 0):
            print(num)
            break

    

    
