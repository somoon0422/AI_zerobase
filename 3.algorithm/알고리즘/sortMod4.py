#병합정렬실습
def mSort(ns, asc=True):
    
    if len(ns) < 2:
        return ns
    
    #분할단계
    midIdx = len(ns) // 2
    leftNums = mSort(ns[0:midIdx], asc = asc) #내림차순 False도 적용되게 하기 위해서 왜냐면 기본값이 True라서 재귀할 때 True 값으로 변하기 떄문에
    rightNums = mSort(ns[midIdx:len(ns)], asc=asc)
    
    mergeNums = [] #병합단계
    leftIdx = 0; rightIdx = 0
    
    while leftIdx < len(leftNums) and rightIdx < len(rightNums):
        
        if asc:
            
            if leftNums[leftIdx] < rightNums[rightIdx]:
                mergeNums.append(leftNums[leftIdx])
                leftIdx += 1
                
            else:
                mergeNums.append(rightNums[rightIdx])
                rightIdx += 1
                
        else:
            
            if leftNums[leftIdx] > rightNums[rightIdx]:
                mergeNums.append(leftNums[leftIdx])
                leftIdx += 1
                
            else:
                mergeNums.append(rightNums[rightIdx])
                rightIdx += 1
            
    mergeNums += leftNums[leftIdx:]
    mergeNums += rightNums[rightIdx:]
    
    return mergeNums
    
    
    
    