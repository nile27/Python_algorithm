# swea_2805. 농작물 수확하기

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input()))for _ in range(N)]
    leng = N//2
    answer = 0
    count = 0

    for i in range(N):
        answer += sum(arr[i][leng-count : leng+count+1])

        if leng <= i:
            count-=1
        else:
            count+=1

    print(f"#{test_case} {answer}")