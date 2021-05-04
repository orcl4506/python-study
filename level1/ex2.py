# 문자열 함수
# find, rfind, join

str1="가나-다-라"

r1=str1.find("-")
print(r1)

r2=str1.find("-",3)
print(r2)

r3=str1.rfind("-")
print(r3)

# 실습

tel1="02-222-7874"

tel2="051-777-8373"

print(tel1[0:3])
r4=tel1.find("222")
print(r4)

# 가,나,다,라,마
str2="가나다라마"
r5=",".join(str2)
print(r5)

