import random as rd
import sortMod4 as sm

rNums = rd.sample(range(1,101), 10)
print(f'not sorted rNums :{rNums}')


print(f'sorted rNums ASC: {sm.mSort(rNums)}')
print(f'sorted rNums DESC: {sm.mSort(rNums, asc=False)}')