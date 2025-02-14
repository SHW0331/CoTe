# 문제
# 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.

# 입력
"""
첫째 줄에 정수의 개수 N(1 ≤ N ≤ 100)이 주어진다. 
둘째 줄에는 정수가 공백으로 구분되어져있다. 
셋째 줄에는 찾으려고 하는 정수 v가 주어진다. 입력으로 주어지는 정수와 v는 -100보다 크거나 같으며, 100보다 작거나 같다.
"""

# 출력
"""
첫째 줄에 입력으로 주어진 N개의 정수 중에 v가 몇 개인지 출력한다.
11
1 4 1 2 4 2 4 2 3 4 4
2
"""

# 코드
user_input = int(input())
arr = [0] * user_input

user_value = input().split()

for index, item in enumerate(user_value):
    arr[index] = (int(item))

user_find = int(input())
print(arr.count(user_find))

# 최적화 코드
user_input = int(input())

# 입력값을 정수 리스트로 변환하고 크기를 user_input으로 제한
arr = list(map(int, input().split()))[:user_input]
user_find = int(input())
print(arr.count(user_find))


# 사용한 함수 list 
# split() : 주어진 문자열의 앞뒤 공백을 제거
# strip() : 구분자를 기준으로 문자열을 나누고 리스트로 반환
# enumerate() : list, tuple, 문자열 등 순회 가능한 객체를 반복하면서, 인덱스와 값을 동시에 가져오는 함수
# list 슬라이싱 : [:n]은 리스트에서 처음부터 n개의 요소만 가져오는 기능




