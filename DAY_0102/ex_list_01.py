# ---------------------------------------------------------
# List 자료형
# - 기본 data 타입 - 숫자 / 글자 / 논리 / 바이트
# - 참조 Data 타입(컨테이너 Data 타입)
#       - 여러 개 Data 저장 - list / tuple / dict / set
# ---------------------------------------------------------


# ---------------------------------------------------------
# List => 여러 개의 데이터를 저장하는 데이터 타입
# - 문법 => [데이터1, 데이터2, ..., 데이터n]
# - 원소 / 요소 => 식별하기 위해서 인덱스(Index) : 파이썬에서 명명
# - 인덱싱 기능 / 슬라이싱 기능 모두 사용 가능
# ---------------------------------------------------------

# 1~50 범위의 7의 배수에 해당하는 정수로 구성된 리스트
# => 7, 14, 21, 28, 35, 42, 49
# => 시작 7
# => 끝 51
# => 간격 7
sevens = list(range(7,51,7))
print(sevens)

# str 데이터 타입 => 인덱싱 -----> 요소 변경 안 됨
# list는 각가의 원소/요소마다 데이터의 주소를 가지고 있기 때문에 요소 변경 가능

# 제일 첫 번째 인덱스에 있는 원소 삭제
# ==> del 삭제하고 싶은 데이터 또는 del(삭제할 데이터)
del sevens[0]
del(sevens[0])
print(sevens)

#del sevens # 리스트 객체 주소를 저장한느 변수 삭제

# ---------------------------------------------------------
# str 데이터 타입 => 인덱싱 ------> 요소 변경 x
# 리스트에 인덱싱 방식으로 원소/요소 데이터 변경/삭제는 가능, 추가는 안 됨
# ---------------------------------------------------------
# 요소 갯수 5개 => 0 ~ 4

# sevens[5] = 56 IndexError: list assignment index out of range
sevens[4] = 56
print(f'sevens => {sevens}') # 요소 추가가 아니라 값이 변경됨