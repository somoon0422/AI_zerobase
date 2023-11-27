# #유클리드 호제법

# def greatestCommonDevide(n1,n2):
    
#     maxNum = 0
#     for i in range(1, (n1+1)):
#         if n1 % i == 0 and n2 % i ==0:
#             maxNum = i
    
#     return maxNum

# print(f'greatestCommonDevide :{ greatestCommonDevide(82,32)}')
# print(f'greatestCommonDevide :{ greatestCommonDevide(96,40)}')


def gcd(n1, n2):
    if n1% n2 == 0:
        return n2
    
    else:
        return gcd(n2, n1%n2)
    

print(f'gcd :{ gcd(82,32)}')
print(f'gcd :{ gcd(96,40)}')
    