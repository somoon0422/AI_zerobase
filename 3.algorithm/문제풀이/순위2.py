datas = [32,'a','z',45,'G',39,50,'T','t',22,31,55,'s',63,59,'E']
print(f'datas: {datas}')

ascIIDatas = []
for data in datas:
    if str(data).isalpha(): # 문자열이면
        ascIIDatas.append(ord(data)) # 아스키코드로 변환
        continue # 다음 데이터로
        
    
    ascIIDatas.append(data)
    
print(f'ascIIDatas: {ascIIDatas}')

ranks = [0 for i in range(len(ascIIDatas))]
print(f'ranks: {ranks}')

for idx, data1 in enumerate(ascIIDatas):
    for data2 in ascIIDatas:
        if data1 < data2: # data1이 data2보다 작으면
            ranks[idx] += 1  # rank를 1 증가
            
print(f'ranks after : {ranks}')

for i , d in enumerate(datas):
    print(f'data: {d:>2} \t rank: {ranks[i]+1}') # rank는 0부터 시작하므로 1을 더해줌
        
    
        