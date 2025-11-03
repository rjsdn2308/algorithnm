# 리스트에서 특정 숫자 위치 찾기
def search_list(a, x):
    n = len(a)
    for i in range(0, n):
        if x == a[i]:
            return i
        
    return -1

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search_list(v, 18))
print(search_list(v, 33))
print(search_list(v, 900))

# 쉽게 설명한 선택 정렬 
def find_min_idx(a):
    n = len(a)
    min_idx = 0
    for i in range(1, n):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx

def sel_sort(a):
    result = []
    while a:
        min_idx = find_min_idx(a)
        value = a.pop(min_idx)
        result.append(value)
    return result

d = [2, 4, 5, 1, 3]
print(sel_sort(d))

# 실제 선택 정렬
def sel_sort(a):
    n = len(a)
    for i in range(0, n-1):
        min_idx = i
        for j in range(i+1, n):
            if a[j] < a[min_idx]:
                min_idx = j

        a[i], a[min_idx] = a[min_idx], a[i]

d = [2, 4, 5, 1, 3]
sel_sort(d)
print(d) 

# 쉽게 설명한 삽입 정렬
def find_ins_idx(r, v):
    for i in range(0, len(r)):
        if v < r[i]:
            return i
    return len(r)

def ins_sort(a):
    result = []
    while a:
        value = a.pop(0)
        ins_idx = find_ins_idx(result, value)
        result.insert(ins_idx, value)
    return result

d = [2, 4, 5, 1, 3]
print(ins_sort(d))

# 실제 삽입 정렬 알고리즘
def ins_sort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
            a[j+1] = key

d = [2, 4, 5, 1, 3]
ins_sort(d)
print(d)

# 알고리즘 연습 문제 1번
def search_list(a, x):
    result = []
    n = len(a)
    for i in range(0, n):
        if x == a[i]:
            result.append(i)
        
    return result

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search_list(v, 18))
print(search_list(v, 33))
print(search_list(v, 900))

# 선택 정렬 내림차순 
def sel_sort(a):
    n = len(a)
    for i in range(0, n-1):
        max_idx = i
        for j in range(i+1, n):
            if a[j] > a[max_idx]:
                max_idx = j
        a[i], a[max_idx] = a[max_idx], a[i]

d = [2, 4, 5, 1, 3]
sel_sort(d)
print(d)

# 삽입 정렬 내림차순
def ins_sort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] < key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key

d = [2, 4, 5, 1, 3]
ins_sort(d)
print(d)