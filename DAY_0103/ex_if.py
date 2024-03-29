# --------------------------------------------------------
# 단순 조건문 ==> (1) 조건이 True인 경우만 처리하는 조건문
# if 조건문:
# <-->실행코드
# <-->실행코드
# <-->실행코드
# --------------------------------------------------------


# --------------------------------------------------------
# 단순 조건문 ==> (2) 조건이 True인 경우/ False 경우 처리하는 조건문
# if 조건문:
# <-->실행코드      T
# <-->실행코드
# <-->실행코드
# else:
# <-->실행코드      F
# <-->실행코드
# <-->실행코드
# --------------------------------------------------------

# --------------------------------------------------------
# 복잡 조건문 ==> (3) 조건이 2개 이상인 경우의 조건문 : 다중조건문
# if 조건문1:
# <-->실행코드      jumsu >= 90: #A
# <-->실행코드
# <-->실행코드
# elif 조건문2:
# <-->실행코드      jumsu >= 80: #B
# <-->실행코드
# <-->실행코드
# elif 조건문3:
# <-->실행코드      jumsu >= 70: #C
# <-->실행코드
# <-->실행코드
# elif 조건문4:
# <-->실행코드      jumsu >= 60: #D
# <-->실행코드
# <-->실행코드
# else:
# <-->실행코드      #F
# <-->실행코드
# <-->실행코드
# --------------------------------------------------------


# --------------------------------------------------------
# 복잡 조건문 ==> (4) 조건문 안에 조건문이 존재하는 조건문 : 중첩조건문
# if 조건문1:      # 양수일 떄
# <-->실행코드
# <-->실행코드
# <-->실행코드
# <-->if 조건문2:
#     <-->실행코드      #홀수
#     <-->실행코드
#     <-->실행코드
# <-->else:
#     <-->실행코드      #짝수
#     <-->실행코드
#     <-->실행코드
# else:
# <-->실행코드      # 0 또는 음수일 때
# <-->실행코드
# <-->실행코드
# --------------------------------------------------------


# --------------------------------------------------------
# 조건부 표현식 === > (5) 1줄 조건문
# 조건 True 실행될 코드 if 조건식 else 조건 False 실행 코드
# ':' 콜론 없음
# --------------------------------------------------------
# 홀수 & 짝수 식별 후 결과 출력하는 코드
num = 0
if num%2:
    print(f"{num}은 홀수")
else:
    print(f"{num}은 짝수")
# 로 지금까지는 써왔지만

print(f"{num}은 홀수") if num%2 else print(f"{num}은 짝수")
# 로 조건부 표현식 (한 줄 표현식) 가능

result = "홀수" if num%2 else "짝수"
# 저장하고 싶을 땐 이렇게도 가능


# 양수, 0 음수 식별 후 결과 출력
if num>0:
    print(f"{num}은 양수")
elif num<0:
    print(f"{num}은 음수")
else:
    print(f"{num}은 0")

# 한 줄 조건문으로 표현하면
result = "양수" if num>0 else "음수" if num<0 else "0"
#          ㄴ 참          거짓  ⏌ㄴ   참       거짓  ⏌
print(f"{num} {result}")

result = int("123") if "123".isdecimal() else "123"