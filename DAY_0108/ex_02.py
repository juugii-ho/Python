# ----------------------------------------------------------
# 지역변수 & 전역변수
# ----------------------------------------------------------

def foo():
    x= 10
    print(x)  # 전역변수 아님, 이름 같더라도  지역변수 20 사용

# 전역변수 없음---------------------------------------------------------
# x = 10

# 함수 호출 --------------------------------------------------------
foo()
print(x) # 전역변수가 없음, 지역변수 x=10 사용불가
# #---------------------------------------------------------

print(locals())
# print(globals())
