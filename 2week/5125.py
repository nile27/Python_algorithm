# 5215. 햄버거 다이어트


T = int(input())


def dfs(i, taste, kcal):
    global max_taste
    if kcal > K:
        return
    if taste > max_taste:
        max_taste = taste
    if i == N:
        return
    dfs(i + 1, taste + arr[i][0], kcal + arr[i][1])
    dfs(i + 1, taste, kcal)


for test_case in range(1, T + 1):
    N, K = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_taste = 0
    dfs(0, 0, 0)

    print(f"#{test_case} {max_taste}")