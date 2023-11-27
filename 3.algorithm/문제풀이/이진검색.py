

import binaryMod

if __name__ == '__main__':
    nums = [1,2,4,6,7,8,10,11,13,15,16,17,20,21,23,24,27,28]
    
    searchNum = int(input('input search number: '))
    
    
    resultIdx = binaryMod.searchNumberByBinaryAlgorithm(nums, searchNum)
    print(f'nums: {nums}')
    
    if resultIdx == -1:
        print(f'No results found.')
        print(f'search result index : {resultIdx}')
        
    else:
        print('>>> serach Results <<<')
        print(f'serach result index : {resultIdx}')
        print(f'search result number : {nums[resultIdx]}')