# ============================================
# 🐴 경마 프로젝트 - 2단계: 레이스 돌리기
# ============================================
# 배울 것: list, for문, while문, random

import random

class horse:
    def __init__(self,name,age,agility,stamina,endurance,distance_grade):
        self.name=name
        self.age=age
        self.agility=agility
        self.stamina=stamina
        self.endurance=endurance
        self.distance_grade=distance_grade
        self.position=0
    def show_info(self):
        print(f"이름:{self.name}")
        print(f"나이:{self.age}") 
        print(f"속도:{self.agility}")
        print(f"스태미너:{self.stamina}")
        print(f"근성:{self.endurance}")
        print(f"거리적성:{self.distance_grade}")
        print()
    def run_one_turn(self):
        base=self.agility# 기본 이동거리 = 속도 기반 + 랜덤 요소
        luck=random.randint(-2,3)# 운 요소 (-2 ~ +3)
        burst=0# 근성: 가끔 폭발적으로 달림 (20% 확률)
        if random.random()<0.2:
            burst=self.endurance
            print(f"🔥{self.name}이(가)뒷심을 발휘했다!")
        fatigue=0
        if self.position>goal*0.6:
            fatigue=(10-self.stamina)//2
            if fatigue>0:
                print(f"  😰 {self.name}이(가) 지쳐가고 있다! (-{fatigue})")
        grade_bonus=0
        if goal<=40 and self.distance_grade=="S":
            grade_bonus=2
        elif 41<=goal<=70 and self.distance_grade=="A":
            grade_bonus=2
        elif goal>=71 and self.distance_grade=="L":
            grade_bonus=2
        

        distance=base+luck+burst-fatigue+grade_bonus
        if distance<1:
            distance=1# 최소 1은 이동
        self.position+=distance
        return distance
# ============================================
# 말 만들기 & 리스트에 담기
# ============================================     
horses=[
horse("템페스터", 3, 8, 6, 7, "S"),
horse("제피로스", 3, 6, 9, 8, "S"),
horse("아이올로스", 3, 7, 7, 9, "S"),
horse("벨페고르",3,7,9,9,"S"),
horse("칼란다간",4,9,7,9,"S")]
# 출전마 소개
print("="*45)
print("  🏇 출전마 소개 🏇")
print("="*45)

for horse in horses:# 리스트를 for문으로 순회
    horse.show_info()
goal=50 # 결승선 거리
print("="*45)
print("  🏁 레이스 시작! (결승선: %dm) 🏁" % goal)
print("="*45)
print()
turn=0
winner=None
while winner is None:# 우승마가 나올 때까지 반복
    turn+=1
    print(f"── 턴 {turn} ──")

    for horse in horses:
        distance=horse.run_one_turn()
        # 트랙 시각화
        track_len=horse.position//2 # 화면에 맞게 축소
        track="🐴"+"ㅡ"*track_len
        print(f"{horse.name:6s}{track}({horse.position}m)")
        # 결승선 도달 체크
        if horse.position>=goal and winner is None:
            winner=horse
    print()
# ============================================
# 결과 발표
# ============================================
print("="*45)
print(f"  🏆 우승마: {winner.name}! 🏆 ")
print("="*45)
# 전체 순위 출력
print()
print("📊 최종 순위:")
ranking=sorted(horses,key=lambda h:h.position,reverse=True)
# sorted()로 position이 큰 순서대로 정렬
for i,horse in enumerate(ranking):
    medal=["🥇", "🥈", "🥉","4️⃣", "5️⃣"]
    print(f"{medal[i]}{i+1}위:{horse.name}({horse.position}m)")
