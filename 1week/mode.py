# swea 1일차 - 최빈수 구하기, 1204
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    table = {}
    for i in range(0, len(arr)):

        if arr[i] not in table:
            table[arr[i]] = 1
        else:
            table[arr[i]] += 1

    answer = sorted(table, key=lambda x : -table[x]);
    print(answer[0])
