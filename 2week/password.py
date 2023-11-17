# swea_1225. [S/W 문제해결 기본] 7일차 - 암호생성기


T = 10
for test_case in range(1, T + 1):
    a = int(input())
    arr = list(map(int,input().split()))
    ans = ''
    count = 1
    while arr[7] > 0:
        if count >= 6:
            count = 1
        arr.append(arr[0] - count)
        arr = arr[1:len(arr)]
        count += 1

    arr[7] = 0
    for i in arr:
        ans += str(i) + ' '



    print(f"#{test_case} {ans[0:len(ans)-1]}")