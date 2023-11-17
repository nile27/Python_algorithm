# swea_1209. [S/W 문제해결 기본] 2일차 - Sum


T = 10
for test_case in range(1, T + 1):
    int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    ans = 0
    sumArr = [0,0,0,0]
    a,b = 0,0
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            a += arr[i][j]
            b += arr[j][i]
        sumArr[0] = max(a,sumArr[0])
        sumArr[1] = max(b, sumArr[1])
        sumArr[2] += arr[i][i]
        sumArr[3] += arr[i][len(arr)-(i+1)]
        a = 0
        b = 0

    print("#{} {}".format(test_case, max(sumArr)))