# swea_2007. 패턴 마디의 길이
T = int(input())

for test_case in range(1, T + 1):
    word = input()
    wordSum =''
    count = 1

    for i in range(len(word)):
        count+=1
        wordSum += word[i]
        if wordSum == word[i+1:i+count]:
            break

    print(f"#{test_case} {len(wordSum)}")