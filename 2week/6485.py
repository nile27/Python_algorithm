# swea_6485. 삼성시의 버스 노선
T = int(input())


for test_case in range(1, T + 1):
    N= int(input())
    busArr = [list(map(int,input().split())) for _ in range(N)]
    C = int(input())
    cArr = {}
    for i in range(C):
        a = int(input())
        if a not in cArr:
            cArr[a]= [i]
        elif a in cArr:
            cArr[a].append(i)
    ans = [0 for i in range(C)]


    for i in range(N):
        for j in range(busArr[i][0], busArr[i][1]+1):
            if j in cArr:
                for k in (cArr[j]):
                    ans[k] += 1


    ans = " ".join(map(str,ans))



    print(f"#{test_case} {ans}")