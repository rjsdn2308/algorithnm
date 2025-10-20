def find_ins_idx(a,x):
    result=[]
    n=len(a)
    for i in range(0,n): 
        if x==a[i]: 
            return i 
    return []
        
v=[17,92,18,33,58,7,33,42]
print(find_ins_idx(v,18))  
print(find_ins_idx(v,33)) 
print(find_ins_idx(v,900))

def ins_sort(a):
    while a:  
        result=[]   
        value=a.pop(0)
        ins_idx = find_ins_idx(result,value) 
        result.insert(ins_idx,value)  
    return result

 