def mSort(ns):
    
    if len(ns) < 2:
        return ns
    
    midIdx = len(ns) // 2
    leftNums = mSort(ns[0:midIdx])
    rightNums = mSort(ns[midIdx:len(ns)])
    
    mergeNums = []
    leftIdx = 0; rightIdx = 0
    
    while leftIdx < len(leftNums) and rightIdx < len(rightNums):
        
        if leftNums[leftIdx] < rightNums[rightIdx]:
            mergeNums.append(leftIdx)
            leftIdx += 1
            
        else:
            mergeNums.append(rightNums[rightIdx])
            rightIdx += 1
            
    mergeNums = mergeNums + leftNums[leftIdx:]
    mergeNums = mergeNums + rightNums[rightIdx:]
    
    return mergeNums
    
    
nums = [8,1,4,3,2,5,10,6]
print(f'mSort : {mSort(nums)}')


