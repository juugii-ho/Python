# --------------------------------------------------------
# [실습] 'Hello World!' 100번 입력
# --------------------------------------------------------
print('Helo World!') #를 100번 복사 붙여넣기 할 수도 있지만
# 반복문 => for in 반복문 -----------------------------------
# - 여러 개의 데이터를 가지고 있는 데이터에서 한 개씩 원소/요소를 읽어와줌
# for 요소저장변수명 in 여러 개의 데이터 가진 타입:
# <-->요소/원소 반복할 코드
# <-->요소/원소 반복할 코드
# --------------------------------------------------------

msg = "Happy New Year 2024! Gook Luck^^"

# msg를 구성하는 문자 한개씩 화면에 출력해주세요!
# H
# a
# p
# p
# y     이런 식으로 하나씩 출력해야..

for ele in msg:
    print(ele)

# [실습1] 'Hello World' 100번 출력
for cnt in range(100):
    print("Hello World!")

# [실슴2] 좋아하는 음식명을 리스트에 저장하기 (단, 10개)
foods = ['치킨', '갈비', '불고기', '피자', '족발', '보쌈', '떡볶이', '마라탕', '돈가스', '제육볶음']
print(foods[0]) #을 10번 쓸 수도 있지만..

for cnt in foods:
    print(cnt)

for cnt in foods: print(cnt) # 실행구문이 한 줄이면 이렇게도 가능