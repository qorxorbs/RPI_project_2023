# 배열 두배 만들기
# 문제 설명
# 정수 배열 numbers가 매개변수로 주어집니다. numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# -10,000 ≤ numbers의 원소 ≤ 10,000
# 1 ≤ numbers의 길이 ≤ 1,000
# 입출력 예
# numbers	result
# [1, 2, 3, 4, 5]	[2, 4, 6, 8, 10]
# [1, 2, 100, -99, 1, 2, 3]	[2, 4, 200, -198, 2, 4, 6]
# 입출력 예 설명
# 입출력 예 #1

# [1, 2, 3, 4, 5]의 각 원소에 두배를 한 배열 [2, 4, 6, 8, 10]을 return합니다.
# 입출력 예 #2

# [1, 2, 100, -99, 1, 2, 3]의 각 원소에 두배를 한 배열 [2, 4, 200, -198, 2, 4, 6]을 return합니다.

# 숫자 4개 입력
# 솔루션에 집어 넣고
# for문으로 배열에 곱히기 2
# 저장한값 리턴 후 출력

def solution(numbers):
    answer = [0]*len(numbers)
    for i in range(0,len(numbers),1):
        answer[i] = 2 * numbers[i]
    return answer

numbers = [1, 2, 3, 4, 5]
ans = solution(numbers)
print(ans)