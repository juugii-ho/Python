# -------------------------------------------------------------------
# 문자/문자열 데이터 살펴보기 => str 데이터 타입
# - 규칙/문법 ==> '데이터', "데이터", '''데이터''', """데이터"""
# -------------------------------------------------------------------
msg = "Happy New Year 2024!" # str의 데이터는 원소/요소로 부름
#      01234/5/678/9/0123/4/5678/9 0부터 19번째까지 공백과 특수문자 모두 인덱싱
#      09876/5/432/1/0987/6/5432/1 -19부터 -1까지 오른쪽부터도 인덱싱 가능

#출력
print(msg)

# -------------------------------------------------------------------
# 문자/글자 안에서 일부분만 추출해서 다루기 => 인덱싱
# - 왼쪽에서 오른쪽 : 0, 1, ...
# - 오른쪽에서 왼쪽 : ..., -2, -1
# - 원소/요소 추출 규칙/문법 => 변수명[인덱스]
print(F'0번 원소 => {msg [0]}')
print(F'1번 원소 => {msg [1]}')
print(F'19번 원소 => {msg [19]}')

# index out of range : 인덱스 범위 벗어나면 오류 발생
# print(F'20번 원소 => {msg [20]}') #IndexError: string index out of range
#                                 종료 코드 1(으)로 완료된 프로세스 - 에러난 것

#Happy만 화면에 출력하기
print(msg[0], msg[1], msg[2], msg[3], msg[4], sep='')
print(msg[0:5])
print(msg[:5])

# 2024!만 화면에 출력하기
print(msg[15], msg[16], msg[17], msg[18], msg[19], sep='')
print(msg[15:20])
print(msg[-5], msg[-4], msg[-3], msg[-2], msg[-1], sep='')
print(msg[-5:0])

# New만 화면에 출력하기
print(msg[6], msg[7], msg[8], sep='')


# -------------------------------------------------------------------
# 문자/글자 안에서 일부분만 추출해서 다루기 ==> 슬라이싱(Slicing)
#
# - 원소/요소 추출 규칙/문법 => 변수명[시작인덱스:끝인덱스+1:간격]
# - 조건 : 연속된 인덱스 또는

msg = "Happy New Year 2024!"

# Happy만 화면에 출력하기 => 슬라이싱으로 출력하기
print(f'msg[0:4] => {msg[0:4]}')
print(f'msg[0:4] => {msg[0:5]}')

# 2024!만 화면에 출력하기 => 슬라이싱으로 출력하기
print(f'msg[15:20] => {msg[15:20]}')
print(f'msg[-5:0] => {msg[-5:0]}') # 아무것도 안 나옴
print(f'msg[-5:0] => {msg[-5:-1]}') # 2024만 나오고 !가 안 나옴
print(f'msg[-5:0] => {msg[-5:20]}') # 모두가 음수일 이유는 없음

# 첫번째부터 시작하는 경우 시작 인덱스 생략 가능
print(f'msg[0:5] => {msg[0:5]}, msg[:5] => {msg[:5]}')

# 마지막번째까지 인 경우 마지막인덱스 생략 가능
print(f'msg[-5:0] => {msg[-5:20]}, msg[-5:] => {msg[-5:]}, msg[15:] => {msg[15:]}') # 모두가 음수일 이유는 없음
print(f'msg[-5:0] => {msg[-5:20]}') # 모두가 음수일 이유는 없음

#처음부터 끝까지 출력하기
print(f'msg[0:20] => {msg[0:20]}, msg[:] => {msg[:]}') # 모두가 음수일 이유는 없음

# -------------------------------------------------------------
# 연속적이지 않지만 규칙이 있는 경우의 슬라이싱
# - 변수명[시작인덱스:끝인덱스+1:간격/규칙]
#-------------------------------------------------------------
msg="123456789"
#    012345678
# msg 안에서 2, 4, 6, 8 요소만 출력
#     1 3 5 7
print(msg[1], msg[3], msg[5], msg[7], sep='')

# 규칙 => 인덱스 연속 X, 인덱스 간격 3씩 증가
print(msg[1:8:2])   # 1 ==> 1+2=3 ==> 3+2=5 ==> 5+2=7 /
                    # ==> 7+2=9는 범위 벗어남

# 3의 배수만 인덱스에서 2,5,8
print(msg[2:9:3])   # 2 ==> 2+3=5 ==> 5+3=8 / ==> 이후 범위 벗어남