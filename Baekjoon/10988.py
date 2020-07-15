#No.10988 '팰린드롬인지 확인하기'

word = list(input())
length = len(word)
reverse = []

for i in range(length-1, -1, -1):
    reverse.append(word[i])

if word == reverse:
    print(1)
else:
    print(0)
