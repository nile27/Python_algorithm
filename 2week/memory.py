# swea_1289. 원재의 메모리 복구하기

T = int(input())
for test_case in range(1, T+1):
    n = str(input())
    trigger = '0'
    answer = 0
    for i in range(len(n)):
        if trigger != n[i]:
            trigger = n[i]
            answer+=1


    print(f"#{test_case} {answer}")