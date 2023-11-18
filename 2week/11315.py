# swea_11315. 오목 판정
T = int(input())

def check(a,b):
    xarr = [0,1,1,1]
    yarr = [1,0,1,-1]
    count = 0
    x,y = a,b

    for i in range(4):
        for j in range(4):
            x += xarr[i]
            y += yarr[i]
            if 0 < x >= N or 0 < y >= N:
                break
            if arr[x][y] == '.':
                count = 0
                break
            count+=1
        if count == 4:
            return True
        x,y =a,b

    return False
for test_case in range(1, T + 1):
    ans = "NO"
    N = int(input())
    arr = [list(map(str,input())) for _ in range(N)]
    checkbool = False

    for i in range(N):
        for j in range(N):
            if arr[i][j] == "o":
                checkbool = check(i,j)
            if checkbool == True:
                break
        if checkbool == True:
            ans = "YES"
            break

    print(f"#{test_case} {ans}")