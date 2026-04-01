# 함수

# ===== [ 1. 함수 ] =====
# 함수 : 반복적으로 사용되는 코드를 줄이기 위해서 사용한다.
def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account()


# ===== [ 2. 전달값과 반환값 ] =====
# 전달값 : 함수에 입력값을 전달하는 것
# 반환값 : 함수의 결과값을 반환하는 것

def deposit(balance, money):  # 입금
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money):  # 출금
    if balance >= money:  # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance

def withdraw_night(balance, money):  # 저녁에 출금
    commission = 100  # 수수료 100원
    return commission, balance - money - commission

balance = 0  # 잔액
balance = deposit(balance, 1000)
print(balance)

balance = withdraw(balance, 2000)
balance = withdraw(balance, 500)

commission, balance = withdraw_night(balance, 500)
print("수수료는 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))

# ===== [ 3. 기본값 ] =====
# 기본값 : 함수의 매개변수에 기본값을 설정해 줄 수 있다.
# 기본값이 설정된 매개변수는 함수 호출 시 값을 입력하지 않아도 된다.

def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
          .format(name, age, main_lang))

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업을 듣는 경우
def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
          .format(name, age, main_lang))

profile("유재석")
profile("김태호")

# ===== [ 4. 키워드값 ] =====
# 키워드값을 이용하여 함수 호출 시 매개변수의 순서를 바꿔도 된다.

def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="김태호")

# ===== [ 5. 가변인자 ] =====
# 가변인자 : 함수의 매개변수 앞에 *를 붙이면 가변인자가 된다.
# 가변인자는 입력받는 값의 개수를 알 수 없다.

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift")


# ===== [ 6. 지역변수와 전역변수 ] =====
# 지역변수 : 함수 내에서만 사용할 수 있는 변수
# 전역변수 : 프로그램 내에서 모두 사용할 수 있는 변수

gun = 10

def checkpoint(soldiers):  # 경계근무
    global gun  # 전역 공간에 있는 gun 변수를 사용하겠다는 의미
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
checkpoint(2)  # 2명이 경계 근무 나감
gun = checkpoint_ret(gun, 2)  # 2명이 경계 근무 나감
print("남은 총 : {0}".format(gun))
