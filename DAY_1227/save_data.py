'''
데이터를 메모리에 저장하는 방법
=> 파이썬 문법 : 변수명 = 저장할 데이터 - 오른쪽에 있는 것을 왼쪽에 저장
=> 파이썬의 변수는 힙영역에 저장된 데이터 주소를 저장하는 변수
=> 참조 변수
'''

# 나이를 메모리에 저장하기
# => 나이 : 정수 int ==> 힙 영역
# => 변수 = age
age = 100 #100은 힙에 저장되고, 100의 주소값이 age라는 변수에 저장됨
# 'age'=100의 경우는 변수가 아니라 문자로 인식하므로 값이 할당되지 않음

#이름을 메모리에 저장하기
# => 이름 : 문자 str ==> 힙 영역
# => 변수 ==> name

_name="홍길동"
name="홍길동"
my_name="홍길동"
# 99name="홍길동" <== X, 숫자는 변수이름으로 첫번째 불가

# if="Good" # 툴에서는 예약어가 있다고 알려주지만, 메모장 등에서 작성 시 구분이 안됨
# False="Good" #예시2

#메모리에 저장은 됨 ==> 저장된 데이터 위치 알 수 없음 => 다시 사용 불가
2024
"Good Luck"

year = 2024     #2024 데이터가 저장된 주소를 year 이름이 붙은 메모리에 저장한 것
                #year는 스택, 2024는 힙
print(year)

# --------------------------------------------------------
# 데이터의 주소를 확인하는 내장함수 => id( 실제 데이터 ) / id( 변수명 )
# --------------------------------------------------------

print(id(2024)) #4376126064 print 꼭 넣기
print(id(year)) #4376126064

year=2023
print( id(year)) #4349633360

# --------------------------------------------------------
# 변수가 저장하고 있는 데이터의 종류 즉, 데이터의 데이터 타입을 알려주는 함수
# => type( 데이터 ) 또는 type( 변수명 )
# --------------------------------------------------------

print(type(2024)) #<class 'int'>
print(type(4.)) #<class 'float'>
print(type('4.')) #<class 'str'>