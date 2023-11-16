# swea_1983. 조교의 성적 매기기

T = int(input())

for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = 0
    score = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
    sortArr = {}
    obj = {}
    tu = N // 10

    for i in range(len(arr)):

        obj[i+1] = (arr[i][0] * 0.35) + (arr[i][1] * 0.45) + (arr[i][2] * 0.2)

    sortArr = sorted(obj.values(), key=lambda x: -x)
    ans = score[sortArr.index(obj[M]) // tu]


    print(f"#{test_case} {ans}")
