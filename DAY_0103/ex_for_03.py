# [문제] --------------------------------------------------
# 문자열 여러 개와 실수 숫자 여러 개를 두 줄로 입력 받기 => input() 1개만 사용
# - 첫 번째 입력 받은 값은 Key
# - 두 번째 입력 받은 값은 Value
# - 딕셔너리로 저장해 주세요.
# --------------------------------------------------------
data = input("문자열과 실수 여러 개 입력\n단, 문자열과 실수 갯수 동일 (예: aa bb cc, 1.1 2.2 3.3)")

# 입력 형식이 맞을 경우만 딕셔너리에 저장
# - (1) 입력 " , " 문자열 안에 ','가 존재해야 함
# - (2) 문자열과 실수 갯수가 동일해야 함
if ',' in data:
    dataList = data.split(',')
    key = dataList[0].split()
    value = dataList[1].split() #여기서 float 형변환은 list 값이기 때문에 안 됨
#   key, value = dataList[0].split(), dataList[1].split() 도 언패킹으로 가능
    dataDict = {}
    if len(key) == len(value):
        for num in range(len(key)):
            dataDict[key[num]] = float(value[num])
        print(dataDict)
    else:
        print("정확한 형식이 아닙니다.")
else:
    print("정확한 형식이 아닙니다.")


# --------------------------------------------------------
# 내장함수 zip()
# --------------------------------------------------------
x = [1,2,3,4,5]
y = [11,22,33,44,55]
z = [111,222,333,444,555]

result = zip(x, y, z)
print(f'result => {type(result)}, {list(result)}')



# zip으로 고친다면?
# [문제] --------------------------------------------------
# 문자열 여러 개와 실수 숫자 여러 개를 두 줄로 입력 받기 => input() 1개만 사용
# - 첫 번째 입력 받은 값은 Key
# - 두 번째 입력 받은 값은 Value
# - 딕셔너리로 저장해 주세요.
# --------------------------------------------------------
data = input("문자열과 실수 여러 개 입력\n단, 문자열과 실수 갯수 동일 (예: aa bb cc, 1.1 2.2 3.3)")

# 입력 형식이 맞을 경우만 딕셔너리에 저장
# - (1) 입력 " , " 문자열 안에 ','가 존재해야 함
# - (2) 문자열과 실수 갯수가 동일해야 함
if ',' in data:
    dataList = data.split(',')
    key = dataList[0].split()
    value = dataList[1].split() #여기서 float 형변환은 list 값이기 때문에 안 됨
#   key, value = dataList[0].split(), dataList[1].split() 도 언패킹으로 가능
    dataDict = {}
    if len(key) == len(value):
        # for num in range(len(key)):
        #     dataDict[key[num]] = float(value[num])
        dataDict2 = dict(zip(key,float(value)))
        print(dataDict2)
    else:
        print("정확한 형식이 아닙니다.")
else:
    print("정확한 형식이 아닙니다.")