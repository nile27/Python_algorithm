#swea_1989. 초심자의 회문 검사
T = int(input())
for test_case in range(1, T + 1):
    arr = list(map(str,input()))
    bin = len(arr)//2
    ans = 1

    for i in range(0,bin):
        if arr[i] != arr[len(arr)-i-1]:
            ans = 0


    print(f"#{test_case} {ans}")