import random
import rankMod

if __name__ == '__main__': # 이 파일이 메인이면 실행
    
    nums = random.sample(range(50,101), 20) #list
    sNums = rankMod.rankAlgorithm(nums)
    print(f'sNums: {sNums}')
        