# swea 1979. 어디에 단어가 들어갈 수 있을까

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(N)]
    answer = 0
    count = 0

    for i in range(0,N):
        for y in range(0,N):
            if arr[y][i] == 1:
                count += 1

            else:
                if count == K:
                    answer +=1
                count = 0
        if count == K:
            answer += 1

        count = 0
        for y in range(0,N):
            if arr[i][y] == 1:
                count += 1

            else:
                if count == K:
                    answer +=1
                count = 0

        if count == K:
            answer += 1
        count = 0

    print(f"#{test_case} {answer}")
