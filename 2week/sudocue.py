# swea_1974. 스도쿠 검증
T = int(input())

for test_case in range(1, T + 1):
    sdocu = [list(map(int,input().split())) for _ in range(9)]
    visit = [0 for _ in range(9)]
    squvisit = [0 for _ in range(9)]
    count = 0
    squcount = 0
    answer = 1

    for i in range(9):
        count +=2
        for j in range(9):
            visit[sdocu[i][j]-1] += 1
            visit[sdocu[j][i]-1] += 1
        if count != max(visit):
            answer = 0
            break

    for x in range(0,9,3):
        for y in range(0,9,3):
            squcount += 1
            for k in range(3):
                for j in range(3):
                    squvisit[sdocu[x+k][y+j]-1] +=1

            if squcount != max(squvisit):
                answer = 0
                break



    print(f'#{test_case} {answer}')