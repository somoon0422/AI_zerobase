def recusion(num):
    
    if num > 0:
        print('*' * num)
        return recusion(num-1)
    
    else:
        return 1
    
recusion(10)

