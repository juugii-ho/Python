# ----------------------------------------------------------
# 지역변수 & 전역변수
# ----------------------------------------------------------

def foo():
    x=20
    print(x)  # 전역변수 아님, 이름 같더라도  지역변수 20 사용

# 전역변수 ---------------------------------------------------------
x = 10

# 함수 호출 --------------------------------------------------------
foo()
print(x) # 전역변수 x=10 사용
#---------------------------------------------------------