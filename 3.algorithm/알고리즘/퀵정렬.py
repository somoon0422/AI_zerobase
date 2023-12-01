def qSort(ns):
    
    if len(ns) < 2:
        return ns
    
    midIdx = len(ns) // 2
    midVal = ns[midIdx] #기준값을 정하는 부분
    
    samllNums = []; sameNums = []; bigNums = []
    
    for n in ns:
        if n < midVal:
            samllNums.append(n)
            
        elif n == midVal:
            sameNums.append(n)
        
        else:
            bigNums.append(n)
            
    return qSort(samllNums) + sameNums + qSort(bigNums)

nums = [8,1,4,3,2,5,4,10,6,8]
result = qSort(nums)
print(f'result : {result}')
