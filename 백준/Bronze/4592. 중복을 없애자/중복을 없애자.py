while True:
    data = input().split()
    N = int(data[0])
    if N == 0:
        break
    nums = list(map(int, data[1:]))
    
    result = []
    prev = None
    for num in nums:
        if num != prev:
            result.append(num)
        prev = num
    
    print(' '.join(map(str, result)), '$')
