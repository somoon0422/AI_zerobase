import os # os 모듈을 가져옴

exts=(".jpg", ".jpeg", ".png", ".JPG", ".JPEG", ".PNG",".bmp")  # 확장자명을 튜플로 저장 

def read_files(path, exts): # path: 폴더경로, exts: 확장자명 
    files = []  # 파일 경로를 저장할 리스트
    
    for r, d, f in os.walk(path):   # root 폴더 경로, dirs폴더명, file파일명
        for file in f: # path의 파일명을 하나씩 가져옴
            if file.lower().endswith(exts): # 파일명이 확장자명으로 끝나면 
                file = os.path.join(r, file) # join() 함수로 root와 file을 합침
                file = os.path.abspath(file) # abspath() 함수로 절대경로를 읽어옴
                file = file.replace(os.sep, "/") #os.sep으로 경로구분자를 "/"로 변경함.
                files.append(file) # files 리스트에 for문을 돌면서 파일 경로를 저장함. 
            
    return files # 파일 경로를 반환

read_files("C:/Users/kimsh-dt01/Downloads/PlateCut/Special_Plate", exts) # 파일 경로를 출력함.


# 도전과제 1
# 지금은 read_files() 함수 안에 넣는 인자가 하드코딩되어 있습니다.
# argparse를 사용해서 인자를 받아서 처리하도록 수정해 보세요.

# 도전과제 2
# 도전과제 1의 결과에 더해서, 파일 대신 하위 폴더 목록을 출력하도록 수정해 보세요.