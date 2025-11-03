# 최댓값 구하기
def find_max(a):
    n=len(a)
    max_v = a[0]
    for i in range(1,n):
        if a[i] > max_v:
            max_v =a[i]
    return max_v

v = [17, 92, 33, 58, 7, 33, 42]
print(find_max(v))

# 최댓값의 위치 구하기
def find_max_idx(a):
    n = len(a)
    max_idx = 0
    for i in range(1, n):
        if a[i] > a[max_idx]:
            max_idx = 1
    return max_idx

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_max_idx(v))

# 두 번 이상 나온 이름 찾기 
def find_same_name(a):
    n = len(a)
    result = set()
    for i in range(0, n-1):
        for j in range(i+1, n):
            if a[i]== a[j]:
                result.add(a[i])
    return result

name = ["Tom", "Jerry", "Mike", "Tom"]
print(find_same_name(name))

name2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
print(find_same_name(name2))

# 알고리즘 연습 문제 
v = [17, 92, 18, 33, 58, 7, 33, 42]  # 예시 입력

min_value = v[0]  # 첫 번째 값을 초기 최솟값으로 설정

for i in range(1, len(v)):
    if v[i] < min_value:
        min_value = v[i]  # 더 작은 값이 있으면 갱신

print("최솟값:", min_value)