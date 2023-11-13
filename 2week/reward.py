import sys
sys.stdin = open("input.txt", "r")

# swea_1244. [S/W 문제해결 응용] 2일차 - 최대 상금

def solution(depth):
    global ans
    global answer
    if depth == num:
        ans = max(ans, int("".join(arr)))
        return

    for i in range(len(arr)):
        for j in range (i+1, len(arr)):
            arr[i],arr[j] = arr[j],arr[i]
            word = ["".join(arr) ,depth]
            if word not in v:
                solution(depth+1)
                v.append(word)
            arr[i],arr[j] = arr[j],arr[i]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    inarr = list(map(str, input().split()))
    num = int(inarr[1])
    arr = list(map(str,inarr[0]))
    ans = 0
    v = []
    solution(0)

    print(f"#{test_case} {ans}")