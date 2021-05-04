#문자열 함수
#find, rfind, join

str1 = "가나-다-라"

r1=str1.find("-")
print(r1)

r2=str1.find("-",3)
print(r2)

r3=str1.rfind("-")
print(r3)

#find와 슬라이싱 이용하기
tel1= "02-2222-7874"

tel1_start=tel1.find("-")+1
tel1_end=tel1.rfind("-")

print(tel1[tel1_start:tel1_end])

tel2 = "051-777-8373"


#가,나,다,라,마
str2="가나다라마"
r4 = ",".join(str2)
print(r4)

#str2.replace 함수로 대체할수 있다.