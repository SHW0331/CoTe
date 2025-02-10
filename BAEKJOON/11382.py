# 문제
# 꼬마 정민이는 이제 A + B 정도는 쉽게 계산할 수 있다. 이제 A + B + C를 계산할 차례이다!

# 입력
# 첫 번째 줄에 A, B, C (1 ≤ A, B, C ≤ 1012)이 공백을 사이에 두고 주어진다.

# 출력
"""
A+B+C의 값을 출력한다.
77 77 7777

7931
"""

# 코드
user_input = input()
values = user_input.split()
result = sum(map(int, values))
print(result)

# 사용한 함수 list 
# input : 사용자의 입력을 받아 문자열로 반환하는 함수
# split : 특정 구분자를 기준으로 나누어 list로 반환하는 함수
    # - separator : 구분자
    # - maxsplit : 최대 분할 횟수
# sum : 함수는 숫자로 이루어진 list나 tuple의 모든 요소의 합을 반환하는 함수
    # - iterable : list, tuple 등 숫자를 포함한 반복 가능한 객체,
    # - start : 기본값은 0, 초기값을 설정할 수 있음
# map : 함수는 주어진 함수를 반복 가능한 객체의 모든 요소에 적용하고, 그 결과를 반환하는 함수
    # - function : 적용할 함수
    # - iterable : list, tuple 등 반복 가능한 객체.


