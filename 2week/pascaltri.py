# swea_2005. 파스칼의 삼각형
T = int(input())

for test_case in range(1, T + 1):
    num = int(input())
    answer = ['1']
    for i in range(1,num):
        Jarr = answer[i-1].split()
        arr = ['1']
        for j in range(len(Jarr)-1):
            arr.append(str(int(Jarr[j]) + int(Jarr[j + 1])))
        arr.append('1')
        answer.append(" ".join(arr))

    ans = '\n'.join(answer)

    print(f"#{test_case}\n{ans}")