# swea_6190. 정곤이의 단조 증가하는 수
def danjo (num):
    strnum = str(num)
    for i in range(len(strnum)-1):
        if strnum[i] > strnum[i+1]:
            return False

    return True



T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr =  list(map(int,input().split()))
    answer = -1
    for i in range(1,len(arr)):
       for j in range(i+1,len(arr)):
           if danjo(arr[i]*arr[j]):
               answer= max(answer,arr[i]*arr[j])



    print(f'#{test_case} {answer}')