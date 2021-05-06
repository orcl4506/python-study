# 오버로딩 없음

def add(a,b):
    return a+b

print(add(1,2))
print("="*50)

def minus(a,b=5):
    return a-b

print(minus(10))
print("="*50)

def many(*data): # 데이터를 튜플로 받음
    print(data)

many(1,2,3,4,5)

def keyword(**data): # 딕셔너리 데이터 받기
    print(data)

keyword(id=1, username="ssar")

n1=1

def var_test():
    global n1 # global 선언 시 전역변수 변경 가능, 중요
    n1=2

var_test()
print(n1)


