def rankAlgorithm(ns):
    
    ranks = [0 for i in range(len(ns))]
    
    for idx , n1 in enumerate(ns):
        for n2 in ns:
            if n1 < n2:
                ranks[idx] += 1
    
    print(f'nums: {ns}')
    print(f'ranks: {ranks}')
    
    
    for i, n in enumerate(ns):
        print(f'num :{n} \t rank : {ranks[i]+1}')
        
        sortedNums = [0 for i in range(len(ns))]
        
        for idx , rank in enumerate(ranks):
            sortedNums[rank] = ns[idx]
            
    
    return sortedNums