import sys
sys.stdin = open('input.txt','r')


# swea_1926. 간단한 369게임
T = int(input())
a= 12
answer =""
st = ""
count = 0

for n in range(1, T + 1):
    num = list(map(str, str(n)))
    for i in range(len(num)):
        if int(num[i]) % 3 == 0 and num[i] != '0':
            count += 1

    if count != 0 :
        st = ""
        for i in range(count):
            st += '-'
    else:
        st = ''.join(num)
    count = 0
    answer += st + " "

print(answer)
