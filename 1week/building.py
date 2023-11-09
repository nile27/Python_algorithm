# swea_1206. [S/W 문제해결 기본] 1일차 - View

for test_case in range(0, 10):
    num = input();
    buliding = list(map(int, input().split()))
    sum = 0

    for i in range(2, len(buliding)-2):
        max_h = max(buliding[i-2], buliding[i-1], buliding[i+1], buliding[i+2])
        if(buliding[i] - max_h > 0):
            sum += buliding[i]-max_h

    print(sum)