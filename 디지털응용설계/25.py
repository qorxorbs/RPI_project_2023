# 가위 바위 보
# 문제 설명
# 가위는 2 바위는 0 보는 5로 표현합니다. 가위 바위 보를 내는 순서대로 나타낸 문자열 rsp가 매개변수로 주어질 때, rsp에 저장된 가위 바위 보를 모두 이기는 경우를 순서대로 나타낸 문자열을 return하도록 solution 함수를 완성해보세요.

# 제한사항
# 0 < rsp의 길이 ≤ 100
# rsp와 길이가 같은 문자열을 return 합니다.
# rsp는 숫자 0, 2, 5로 이루어져 있습니다.
# 입출력 예
# rsp	result
# "2"	"0"
# "205"	"052"
# 입출력 예 설명
# 입출력 예 #1

# "2"는 가위이므로 바위를 나타내는 "0"을 return 합니다.
# 입출력 예 #2

# "205"는 순서대로 가위, 바위, 보이고 이를 모두 이기려면 바위, 보, 가위를 순서대로 내야하므로 “052”를 return합니다.

# rsp를 입력
# for문 이랑 if문으로 문자열 첫번째부터 비교해서 가위바위보 이기는 답 저장 
# 저장한 이기는 값을 문자열에 차례대로 합치기

def solution(rsp):
    answer=""
    for i in rsp:
        if i=='2':
            ans = '0'
        elif i=='0':
            ans = '5'
        elif i=='5':
            ans = '2'
        answer=answer+ans
    return answer

rsp='205205'
ans=solution(rsp)
print(ans)