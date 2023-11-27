import copy

def sortByBubbleAlgorithm(ns, asc=True):
    
    c_ns = copy.copy(ns)
    
    length = len(c_ns) - 1 # 0 ~ 9
    for i in range(length):
        for j in range(length -1):
            
            # 오름차순
            if asc:
                if c_ns[j] > c_ns[j+1]:
                    c_ns[j], c_ns[j+1] = c_ns[j+1], c_ns[j]
            
            # 내림차순
            if not asc:
                if c_ns[j] < c_ns[j+1]:
                    c_ns[j], c_ns[j+1] = c_ns[j+1], c_ns[j]
                
            #로그
            print(f'ns: {c_ns}')
        print()
        
    return c_ns
    