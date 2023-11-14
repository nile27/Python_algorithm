# swea_1215. [S/W 문제해결 기본] 3일차 - 회문1
T = 10
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(str,input())) for _ in range(8)]
    zipArr = list(zip(*arr))
    stack = []
    zipStack = []
    answer = 0
    boolArr = [True,True]
    a = []

    for i in range(8):
        for j in range(8 - n+1):
            stack.append(arr[i][j:j + n ])
            zipStack.append(zipArr[i][j:j + n])

            for k in range((n // 2)):
                if stack[0][0 + k] != stack[0][n - 1 - k]:
                    boolArr[0] = False
                if zipStack[0][0 + k] != zipStack[0][n - 1 - k]:
                    boolArr[1] = False

            stack.clear()
            zipStack.clear()
            if boolArr[1] == True:
                answer += 1
            if boolArr[0] == True:
                answer += 1
            boolArr = [True,True]


    print(f'#{test_case} {answer}')
