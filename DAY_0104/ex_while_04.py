# -----------------------------------------------------------------
# continue => 계속해서~
# - 키워드 아래 코드 실행 안됨
# - 반복 상단으로 이동
# -----------------------------------------------------------------
# 1 ~ 30으로 구성된 리스트를 생성하세요
numList = list(range(1,31))

# 리스트의 요소 중에서 짝수인 경우만 화면에 출력해 주세요~
# print(numList[0])
# print(numList[1])
#     ...
# print(numList[28])
# print(numList[29])

for data in numList:
    if not data % 2:
        print(data)

for data in numList:
    if data%2:              # 1은 True, 0은 False 잊지 말자
        continue            # for문, while문 모두 사용
    print(data)
print("for문 방법")

idx = -1
while idx<30:
    idx +=1
    if numList[idx]%2:
        continue
    print(f'{idx}번째 요소 값 : {numList[idx]}')


print("while문 방법\n")



