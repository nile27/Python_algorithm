# swea_1860. 진기의 최고급 붕어빵
T = int(input())


for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = sorted(list(map(int, input().split())) )
    i = 0
    bread = 0
    ans = "Possible"

    while(i < N):
        if (arr[i] // M) * K - i <= 0:
            ans = "Impossible"
            break
        i+=1


    print(f"#{test_case} {ans}")