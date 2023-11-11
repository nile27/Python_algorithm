# swea 2001. 파리 퇴치
T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(N)]
    answer = 0
    count = 0
    for i in range(0,N-K+1):
        for j in range(0,N-K+1):
            for k in range(K):
                count += sum(arr[i + k][j: j + K])
            if answer < count :
                answer = count
            count = 0



    print(f"#{test_case} {answer}")