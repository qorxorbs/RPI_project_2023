# 분수의 덧셈
# 문제 설명
# 첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1, 두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다. 두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

# 제한사항
# 0 <numer1, denom1, numer2, denom2 < 1,000
# 입출력 예
# numer1	denom1	numer2	denom2	result
# 1	2	3	4	[5, 4]
# 9	2	1	3	[29, 6]
# 입출력 예 설명
# 입출력 예 #1

# 1 / 2 + 3 / 4 = 5 / 4입니다. 따라서 [5, 4]를 return 합니다.
# 입출력 예 #2

# 9 / 2 + 1 / 3 = 29 / 6입니다. 따라서 [29, 6]을 return 합니다.

# 숫자 4개 입력
# 솔루션에 집어 넣고
# 분모 맞춰주고 분자를 분모에 맞게끔 곱해서 맞춰준 다음 최대공약수로 나눠서 배열로 저장
# 저장한값 리턴 후 출력
import math

def solution(numer1, denom1, numer2, denom2):
    denom = denom1*denom2
    num1 = numer1*denom2
    num2 = numer2*denom1
    num = num1 + num2
    gcd = math.gcd(num,denom) 
    num = int(num / gcd)
    denom = int(denom / gcd)
    answer = [num,denom]
    return answer

numer1, denom1, numer2, denom2 = 1,2,3,4
ans = solution(numer1, denom1, numer2, denom2)
print(ans)