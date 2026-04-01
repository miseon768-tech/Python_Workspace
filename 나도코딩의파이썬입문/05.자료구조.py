# 05. 자료구조

# ===== [ 1. 리스트 [ ] ] =====

# 지하철 칸 별로 10명, 20명, 30명
subway1 = 10  
subway2 = 20  
subway3 = 30  

subway = [10, 20, 30]  
print(subway)

subway = ["유재석", "조세호", "박명수"]  
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")  
print(subway)

# 정형돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈")   
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())  
print(subway)

print(subway.pop())  
print(subway)

print(subway.pop())  
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")  
print(subway)  
print(subway.count("유재석"))

# 정렬도 가능
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)

# 순서 뒤집기도 가능
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함꼐 사용
number_list = [5, 2, 4, 3, 1]  
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)

# ===== [ 2. 사전 ] =====

cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3])  
print(cabinet[100])  

print(cabinet.get(3))  # 유재석 
print(cabinet.get[5]) # error 
print(cabinet.get(5)) # None 
print(cabinet.get(5, "사용 가능")) # 사용 가능 
print("hi") # hi

print(3 in cabinet) # True 
print(5 in cabinet) # False

cabinet = {"A-3": "유재석", "B-100": "김태호"}  
print(cabinet["A-3"])  # 유재석 
print(cabinet["B-100"])  # 김태호  

# 새 손님  
print(cabinet)  
# {'A-3': '유재석', 'B-100': '김태호'} 
cabinet["A-3"] = "김종국"  
cabinet["C-20"] = "조세호"  
print(cabinet)   
# {'A-3': '김종국', 'B-100': '김태호', 'C-20': '조세호'}

# 간 손님
del cabinet["A-3"]  
print(cabinet)   
# {'B-100': '김태호', 'C-20': '조세호'}

# key 들만 출력
print(cabinet.keys())  
# dict_keys(['B-100', 'C-20'])

# value 들만 출력
print(cabinet.values())  
# dict_values(['김종국', '김태호', '조세호'])

# key, value 쌍으로 출력
print(cabinet.items())  
# dict_items([('A-3', '김종국'), ('B-100', '김태호'), ('C-20', '조세호')])

# 목욕탕 폐점
cabinet.clear()  
print(cabinet) # {}

# ===== [ 3. 튜플 ] =====

menu = ("돈까스", "치즈까스")  
print(menu[0]) # 돈까스 
print(menu[1]) # 치즈까스

menu.add("생선까스") # error

name = "김종국"  
age = 20  
hobby = "코딩"  
print(name, age, hobby) # 김종국 20 코딩

(name, age, hobby) = ("김종국", 20, "코딩")  
print(name, age, hobby) # 김종국 20 코딩

# ===== [ 4. 세트(집합, set) - 중복 안됨, 순서 없음 ] =====
my_set = {1, 2, 3, 3, 3}  
print(my_set) # 1, 2, 3

java = {"유재석", "김태호", "양세형"}  
python = set(["유재석", "박명수"])

# 교집합 (java 와 python 을 모두 할 수 있는 개발자)
print(java & python) # {'유재석'} 
print(java.intersection(python)) # {'유재석'}

# 합집합 (java 할 수 있거나 python 할 수 있는 개발자)
print(java | python) # {'유재석', '김태호', '양세형', '박명수'} 
print(java.union(python)) # {'유재석', '김태호', '양세형', '박명수'}

# 차집합 (java 할 수 있지만 python 은 할 줄 모르는 개발자)
print(java - python) # {'김태호', '양세형'} 
print(java.difference(python)) # {'김태호', '양세형'}


# python 할 줄 아는 사람이 늘어남
python.add("김태호")  
print(python) # {'유재석', '박명수', '김태호'}

# java 를 잊어버림
java.remove("김태호")  
print(java) # {'유재석', '양세형'}

# ===== [ 5. 자료구조의 변경 ] =====

# 커피숍
menu = {"커피", "우유", "주스"}  
print(menu, type(menu)) # {'커피', '우유', '주스'} <class 'set'>

menu = list(menu)  
print(menu, type(menu)) # ['커피', '우유', '주스'] <class 'list'>

menu = tuple(menu)  
print(menu, type(menu)) # ('커피', '우유', '주스') <class 'tuple'>

menu = set(menu)
print(menu, type(menu)) # {'커피', '우유', '주스'} <class 'set'>

