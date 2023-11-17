# swea_1984. 중간 평균값 구하기

T = int(input())

for test_case in range(1, T + 1):
    arr = list(map(int,input().split()))
    ans = 0
    arr.sort()
    ans = round(sum(arr[1 : 9]) / 8)


    print(f"#{test_case} {ans}")
