print(abs(-5))
print(pow(4,2))
print(max(5,12))
print(min(5,12))
print(round(3.14))
print(round(4.99))

from math import*
print(floor(4.99))
print(ceil(3.14))
print(sqrt(16))
from random import*
print(random()*10)
print(int(random()*10))
print(int(random()*10)+1)
print(int(random()*45)+1)

print(randrange(1,46))

print(randint(1,45))

from random import*
date=randint(4,28)
print("오프라인 스터디 모임 날짜는 매월"+ str(date)+"일로 선정되었습니다.")


jumin="991227-1030730"

print("성별:"+jumin[7])
print("연:"+jumin[0:2])#세미콜론은 0부터 2직전까지 즉,(0,1)
print("월:"+jumin[2:4])
print("일:"+jumin[4:6])
print("생년월일:"+jumin[:6])#처음부터 6 직전까지
print("뒤 7자리:"+jumin[7:])#7부터 끝까지
print("뒤 7자리:"+jumin[-7:])

fruits=["사과","멜론","포도","멜론","참외","멜론"]
index=fruits.index("멜론")
print(index)
index=fruits.index("멜론",index+1)
print(index)

print(fruits.count("멜론"))
print("멜론" in fruits)
멜론_positions=[index for index,fruits in enumerate(fruits)if fruits=="멜론"]
print(멜론_positions)

print(fruits==["사과","멜론","포도","멜론","참외","멜론"])
print(["멜론","사과","포도"] in fruits)
want_to_find = {"멜론", "사과"}
print(want_to_find.issubset(set(fruits)))

#문자열 포맷
print("나는 %d살입니다" %26)
print("나는 %s와 %s를 좋아해요."%("맨하탄 카페","심볼리 크리스 에스"))
print("나는 {}입니다.".format("트레이너"))
print("나는 {0}의 {1}입니다.".format("맨하탄 카페","트레이너"))
print("나는 {horse}의 {me}입니다.".format(horse="맨하탄 카페",me="트레이너"))
horse="심볼리 크리스 에스"
me="트레이너"
print(f"나는 {horse}의 {me}입니다.")
#탈출문자
print("백문이 불여일견\n백견이 불여일타")
print("저는 '트레이너'입니다.")
print('저는 "트레이너"입니다.')
print("저는 \"트레이너\"입니다.")
#\" \' :문장 내에서 따옴표 역할로 사용 가능
print("Red Apple\rPine")
#\r : 커서를 맨 앞으로 이동
print("Redd\bApple")
#\b : 백스페이스 (한 글자를 삭제)
print('Red\tApple')
#\t : 키보드 탭 버튼 역할


url="http://naver.com"
my_str=url.replace("http://","")
print(my_str)
my_str=my_str[:my_str.index(".")]#my_str[0:5]>0.5직전까지(0,1,2,3,4)
print(my_str)
password=my_str[:3]+str(len(my_str))+str(my_str.count("e"))+"!"
print("{0}의 비밀번호는 {1}입니다.".format(url,password))
#리스트 [ ]
#지하철 칸별로 10명,20명,30명
subway=[10,20,30]
print(subway)
#20명이 타고 있는 칸은 몇번째 칸인가?
print(subway.index(20))
subway.append(40)#append는 항상 맨 뒤에 붙음
print(subway)
subway.insert(1,50)#insert는 원하는 자리에 집어넣을 수 있음
print(subway)
print(subway.pop())#pop은 문자나 숫자를 하나씩 맨뒤에서 꺼냄
#num_list는 괄호 안에 있는 숫자나 문자들을 숫자의 순서대로 정렬함
num_list=[5,2,4,3,1]
num_list.sort()
print(num_list)
#num_reverse()는 list와 반대로 순서를 뒤집음
num_list.reverse()
print(num_list)
#리스트를 모두 지우기=num_list.clear
#숫자와 문자가 복합된 리스트를 만드는 법=mix_list
mix_list=["골드쉽",564,True]
print(mix_list)
#리스트 콤바인=extend
num_list.extend(mix_list)
print(num_list)
cabinet={3:"트랜센드",100:"원더 어큐트"}
print(cabinet[3])
print(cabinet.get(100))
print(cabinet.get(5,"사용 가능"))
print(3 in cabinet)#키 in 변수 순서대로 ex)3이 캐비넷 안에 있느냐?=true or false
#정수뿐만 아니라 스트링형태로도 가능
cabinet={"A-3":"트랜센드","B-100":"원더 어큐트"}
print(cabinet["A-3"])
print(cabinet["B-100"])
#새 손님
print(cabinet)
cabinet["A-3"]="스마트 팔콘"
cabinet["C-20"]="코파노 리키"
print(cabinet)
#떠난 손님
del cabinet["A-3"]
print(cabinet)
#key들만 출력
print(cabinet.keys())
#value들만 출력
print(cabinet.values())
#key,value를 전부 출력
print(cabinet.items())
menu=("불닭볶음면","짜파구리")
print(menu[0])
print(menu[1])
#값을 추가하거나,변경하는 것은 불가능ex)add 사용 불가
name="타니노 김렛"
age=26
hobby="파괴"
print(name,age,hobby)
(name,age,hobby)=("타니노 김렛",26,"파괴")
print(name,age,hobby)
#set(집합)
#중복 안됨,순서 없음
my_set={1,2,3,3,3}
print(my_set)
#교집합 &
dirt={"오구리 캡","하루 우라라","홋코 타루마에"}
turf=set(["오구리 캡","스테이 골드","티엠 오페라 오"])
print(dirt&turf)
#교집합 (더트와 터프에서 모두 뛸수 있는 말들)
print(dirt.intersection(turf))
#합집합 (더트나 터프에서 뛰는 말들)
print(dirt.union(turf))
#차집합 (더트에서 뛸 수 있지만 터프에서 뛸 수 없는 말들)
print(dirt-turf)
print(dirt.difference(turf))
#추가하거나 제거할 경우 add와 remove를 사용 가능

#자료구조의 변경
#커피샵
menu={"커피","하치미","우유","당근 주스"}
print(menu,type(menu))

menu=list(menu)
print(menu,type(menu))
menu=tuple(menu)
print(menu,type(menu))

from random import *
users=range(1,21)
users=list(users)
shuffle(users)
print(users)
winners=sample(users,4)
print("당첨자 발표")
print("치킨 당첨자:{0}".format(winners[0]))
print("커피 당첨자:{0}".format(winners[1:]))
print("축하합니다")

for waiting_no in range(1,6):
    print("대기번호:{0}".format(waiting_no))
starbucks=["시리우스 심볼리","심볼리 루돌프","스피드 심볼리"]
for customer in starbucks:
    print("{0}님 커피가 준비되었습니다.".format(customer))

absent=[2,5]
no_book=[7]
for student in range(1,11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지.{0}는 교무실로 따라와".format(student))
        break
    print("{0},책을 읽어봐".format(student))

students=[1,2,3,4,5]
print(students)
students=[i+100 for i in students]
print(students)
students=["symboli rudolf","symboli kris s","sirius symboli"]
students=[len(i) for i in students]
print(students)

students=["symboli rudolf","symboli kris s","sirius symboli"]
students=[i.upper()for i in students]
print(students)

from random import*#도구 상자 가져오기(랜덤 숫자를 쓰기위한 준비)
cnt=0
for i in range(1,8):#(시작과 끝,특정 횟수만큼 똑같은 일을 시킬 때)
    customer=randint(1,7)#주사위 던지기(a부터b까지 숫자 중 하나를 무작위로 뽑기)
    if customer <= 4:#갈림길(조건이 맞으면 이 길로,아니면 저 길로)
        print(f"{i}번 대기팀(인원:{customer}명)입장하세요.")#빈칸 채우기 문장(문자열 안에 변수 값을 넣을 때)
        cnt+=1
    else:
        print(f"{i}번 대기팀(인원:{customer}명)입장 불가.")
#SyntaxError: expected ':'에러 원인=for나 if문장 끝에 :을 안 찍었음.
#2026-04-06 파이썬 기초:제어문과 랜덤
#1.핵심 로직
#반복이 필요할 땐 for i in range(1, 11):
#랜덤 숫자가 필요할 땐 randint(시작, 끝)
#조건에 따라 나눌 땐 if 조건: -> else:
#2.출력 팁
#print(f"밸류{변수}밸류")
def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance,money):
    print("입금이 완료되었습니다.잔액은 {}원입니다.".format(balance+money))
    return balance+money
balance=0
balance=deposit(balance,1500)
print(balance)

def withdraw(balance,money):
    if balance >=money:
        print("출금이 완료되었습니다.잔액은{}입니다.".format(balance-money))
        return balance-money
    else:
        print("출금이 완료되지않았습니다.잔액은{}입니다.".format(balance))
        return balance
def withdraw_night(balance,money):
    commission=100
    return commission,balance-money-commission
balance=0
balance=deposit(balance,1000)
balance=withdraw(balance,2000)
commission,balance=withdraw_night(balance,500)
print("수수료{0}원이며,잔액은{1}원입니다.".format(commission,balance))

def profile(name,age,language):
    print("이름:{},나이:{},주 사용 언어:{}".format(name,age,language))

profile("트윈 터보",20,"대도주")
profile("메지로 파머",23,"대도주")