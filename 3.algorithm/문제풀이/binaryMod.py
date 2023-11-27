def searchNumberByBinaryAlgorithm(ns, sn):
    
    searchResultIdx = -1
    
    startIdx = 0
    endIdx = len(ns) -1
    midIdx = (startIdx + endIdx) // 2
    midVal = ns[midIdx]
    
    print(f'startIdx : {startIdx} , endIdx : {endIdx} , midIdx : {midIdx} , midVal : {midVal}') 
    
    while sn >= ns[0] and sn <= ns[len(ns)-1]:
        
        if sn == ns[len(ns)-1]:
            searchResultIdx = len(ns) -1
            break
        
        if startIdx + 1 == endIdx:
            if ns[startIdx] != sn and ns[endIdx] != sn:
                break
        
        if sn > midVal:
            
            startIdx = midIdx
            midIdx = (startIdx + endIdx) // 2
            midVal = ns[midIdx]
            print(f'+ startIdx : {startIdx} , endIdx : {endIdx}')
            print(f'+ midIdx : {midIdx} , midVal : {midVal}')
        
        elif sn < midVal:
            
            endIdx = midIdx
            midIdx = (startIdx + endIdx) // 2
            midVal = ns[midIdx]
            print(f'- startIdx : {startIdx} , endIdx : {endIdx}')
            print(f'- midIdx : {midIdx} , midVal : {midVal}')
        
        
        elif sn == midVal:
            searchResultIdx = midIdx
            break
        
    return searchResultIdx