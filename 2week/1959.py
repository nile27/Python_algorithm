# swea_1959. 두 개의 숫자열
T = int(input())

for test_case in range(1, T + 1):
    ans = 0
    leng1,leng2 = map(int,input().split())
    N = list(map(int,input().split()))
    M = list(map(int,input().split()))
    total = 0

    if len(N) < len(M) :
        for i in range(0, abs(len(M) - len(N)) + 1):
            arr = M[i:i + len(N)]
            for j in range(len(arr)):
                total += arr[j] * N[j]
            ans = max(ans, total)
            total = 0
    else :
        for i in range(0, abs(len(M) - len(N)) + 1):
            arr = N[i:i + len(M)]
            for j in range(len(arr)):
                total += arr[j] * M[j]

            ans = max(ans, total)
            total = 0

    print(f"#{test_case} {ans}")