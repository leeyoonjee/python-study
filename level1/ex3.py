# 1. 리스트 list1=[] , 1차원, 데이터 변경이 가능함
list1 = [1,2,3,4]
list2 = [5,6,7,8]

print(list1[2])
print("="*50)

#더하기 중요
list3 = list1+list2  #1차원 배열
print(list3)

#더하기 중요
list4 = [
    list1,
    list2
]

# 3 스칼라
# [1,3,4] 벡터 (열)

print(list4)   #2차원 배열 matrix, 3차원 tensor

list1.append(10)  #리스트에 추가하기
print(list1)

del list1[0]   #인덱스 자리값으로 삭제하기
print(list1)


list1.remove(2) #데이터 값으로 삭제하기
print(list1)


list6 = list(range(10))
print(list6)


list7 = list(range(1,12)) #마지막 인덱스 직전까지
print(list7)



# 2. 튜플 - 리스트 같음!! 데이터 변경이 불가능
tuple1 = (1,2,3)
print(tuple1)

tuple2 = (4,5,6)

tuple3=tuple1+tuple2
print(tuple3)


# 2차원 튜플
tuple4 =(
    tuple1,
    tuple2
)
print(tuple4)


list10 = list(tuple1)
print(list10)


# 3. 딕셔너리