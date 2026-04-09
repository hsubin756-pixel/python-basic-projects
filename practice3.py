#빈 자리는 빈공간으로 두고,오른쪽 정렬을 하되,총 10자리 공간을 확보
print("{0: >10}".format(500))
#양수일 땐 +로 표시,음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
#왼쪽 정렬하고,빈 칸을 밑줄_로 채움
print("{0:_<+10}".format(500))
#3자리마다 콤마를 찍어주기
print("{0:,}".format(1000000000))
#3자리마다 콤마를 찍어주기
print("{0:+,}".format(1000000000))
#3자리마다 콤마를 찍어주기+부호도 붙이고 자릿수 확보
print("{0:^<+30,}".format(10000000000))
#소수점 출력
print("{0:f}".format(5/3))
#소수점 특정 자리수까지만 표시
print("{0:.2f}".format(5/3))

#score_file=open("score.txt","w",encoding="utf8")
#print("수학:0",file=score_file)
#print("영어:50",file=score_file)
#score_file.close

#score_file=open("score.txt","a",encoding="utf8")
#score_file.write("과학:80")
#score_file.write("\n코딩:100")
#score_file.close

#import pickle
#profile_file=open("profile.pickle","rb")
#profile={"이름:김영삼","나이:89","취미:[선동,학살]"}
#print(profile)
#pickle.dump(profile,profile_file)#profile에 있는 정보를 file에 저장
#profile_file.close() 
#import pickle
#profile_file=open("profile.pickle","rb")
#profile=pickle.load(profile_file)
#print(profile)
#profile_file.close()

#import pickle
#with open("profile.pickle","rb")as profile_file:
 #   print(pickle.load(profile_file))

horse="...메지로 맥퀸..."
print(horse.strip("."))
print(horse.find("맥"))
print(horse.replace("맥퀸","파머"))

#my_tuple=('메지로 맥퀸','토카이 테이오')
#my_list=list(my_tuple)
#my_list.append('골드 쉽')
#my_tuple=tuple(my_list)
#print(my_tuple)

my_list=['야마닌 제퍼','카츠라기 에이스','카츠라기 에이스','오구리 캡']
my_dic=dict.fromkeys(my_list)
print(my_dic)

today='맑음'
if today=='진창길':
    print('파워')
elif today=='맑음':
    print('컨디션')

weather='살짝 흐림'
is_raining=True
if is_raining:
    umbrella=True
    if weather=='폭우':
        print('우산을 반드시 챙기세요')
    else:
        print('우산 챙기면 좋아요')
    if umbrella == True:
        print('오늘 우산 챙겼나요? 확인하세요!')

player_hp=30
is_alive=True
has_weapon=True
weapon='대검'
if is_alive:
    if has_weapon:
        if weapon=='검':
            print('검으로 적을 공격! 10의 데미지를 입혔다!')
        elif weapon=='활':
            print('활로 적을 공격하여 10의 데미지를 입혔다!')
        else:
            print('당신은 이 무기를 다룰 수 없습니다.')
    else:
        print('당신은 무기가 없어 맨손으로 공격했다.')
else:
    print('플레이어가 적에게 대항할 수 없어 쓰러졌습니다.')

for x in range(3):
    print(f'피지컬 트레이닝 {x+1}회 완료!')
for x in range(0,10,2):
    print(f'피지컬 트레이닝 {x+1}회 완료!')

max=25
weight=0
item=3
while weight+item<=max:
    weight+=item
    print("짐을 추가하겠습니다")
print(f"총 무게는 {weight}kg입니다.")

#name='라이트닝 볼트'
#heart_rate=140
#heart_limit=210
#while heart_rate>=140:
   # heart_rate+=20
    #if heart_rate>=180:
      #  print('페이스를 낮춰야합니다.')
    #if heart_rate>=heart_limit:
       # print('라이트닝 볼트의 경주를 즉시 중단하겠습니다')
       # break

#1.재료준비 말과 심박수,심박수 증가량,바퀴수를 리스트로 만들기.       
horses = ['라이트닝 볼트', '템페스트', '스톰브링어']
rts=[140,140,140]
rt_limit=210
incs=[10,15,20]
lap=[0,0,0]
#for문 말을 한마리씩 꺼내기 i=0>1>2 순서로 한마리씩 경주를 실시함
for i in range(3):
    while rts[i]>=140:#while문 경주를 반복.심박수 140이상인 동안 바퀴를 돌며 심박수가 상승함.
        lap[i]+=1
        rts[i]+=incs[i]
        if rts[i]>=180:#if문 중첩.상태 판단.심박수가 180을 넘기면 경고,210을 넘으면 즉시 중단
            print(f"{horses[i]}의 속도를 줄여야합니다.")
            if rts[i]>=rt_limit:
                print(f"{horses[i]}의 경주를 즉시 중단합니다.")
                print(f"{horses[i]} {lap[i]}바퀴에서 중지.")
                break
