#No.2941

s = input()

a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in a:
    s = s.replace(i, '*')
    
print(len(s))

