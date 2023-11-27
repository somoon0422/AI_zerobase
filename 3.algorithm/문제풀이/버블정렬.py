import random
import bubbleMod

if __name__ == '__main__':
    
    nums = random.sample(range(1, 21), 10)
    print(f'not sorted nums: {nums}')
    
    result = bubbleMod.sortByBubbleAlgorithm(nums)
    print(f'sorted nums by ASC :{result}')
    
    result = bubbleMod.sortByBubbleAlgorithm(nums, False)
    print(f'sorted nums by DESC :{result}')