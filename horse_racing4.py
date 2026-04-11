# ============================================
# 🐴 경마 프로젝트 - 3단계: Race 클래스 분리
# ============================================
# 배울 것: 클래스 간 협력, 역할 분리
# Horse = 말 하나의 데이터와 행동
# Race  = 레이스 전체를 관리하는 진행자
import random

GRADE_VALUE = {"S": 10, "A": 8, "B": 6, "C": 4, "D": 2}
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
    def run_one_turn(self,goal):
        base=GRADE_VALUE[self.agility]
        luck=random.randint(-2,3)
        burst=0
        if random.random()<0.2:
            burst=GRADE_VALUE[self.endurance]
            print(f"  🔥 {self.name}이(가) 뒷심을 발휘했다!")
        fatigue=0
        if self.position>goal*0.6:
            stamina_val=GRADE_VALUE[self.stamina]
            fatigue=(10-stamina_val)//2
        if fatigue>0:
            print(f"  😰 {self.name}이(가) 지쳐가고 있다! (-{fatigue})")
        grade_bonus=0
        if goal<=1400 and self.distance_grade=="S":
            grade_bonus=2
        elif 1401<=goal<=2000 and self.distance_grade=="M":
            grade_bonus=2
        elif 2000<=goal<=3200 and self.distance_grade=="L":
            grade_bonus=2
        distance=base+burst+luck-fatigue+grade_bonus
        if distance<1:
            distance=1
        self.position+=distance
        return distance
    def reset(self):
        self.position=0
class race:
    def __init__(self,name,goal,horses):
        self.name=name# 레이스 이름
        self.goal=goal# 결승선 거리
        self.horses=horses# 출전마 리스트
        self.result=[]# 최종 순위 저장용
    def show_entry(self):
        print("="*45)
        print(f"  🏇 {self.name} - 출전마 소개 🏇")
        print(f"  📏 거리:{self.goal}m")
        print(f"="*45)
        for horse in self.horses:
            horse.show_info()
    def run(self):
        for horse in self.horses:
            horse.reset()
        print("="*45)
        print(f"  🏁 {self.name} 레이스 시작! 🏁") 
        print("="*45)
        print()

        turn=0
        winner=None
        while winner is None:
            turn+=1
            print(f"── 턴 {turn} ──")
            for horse in self.horses:
                distance=horse.run_one_turn(self.goal)
                track_len=horse.position//50
                track= "🐴" + "ㅡ" * track_len
                print(f"{horse.name:6s}{track}({horse.position}m)")
                if horse.position>=self.goal and winner is None:
                    winner=horse
            print()
        self.result=sorted(self.horses,key=lambda h:h.position,reverse=True)
        return winner
    def show_result(self,winner):
        print("="*45)
        print(f"  🏆 우승마: {winner.name}! 🏆")
        print("="*45)
        print()
        print("📊 최종 순위:")
        medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣"]
        for i,horse in enumerate(self.result):
            print(f"{medals[i]}{i+1}위:{horse.name}({horse.position}m)")
            print()
horses = [
    horse("템페스터", 3, "S", "C", "A", "S"),
    horse("제피로스", 3, "B", "S", "A", "S"),
    horse("아이올로스", 3, "A", "A", "S", "S"),
    horse("벨페고르", 3, "A", "S", "S", "S"),
    horse("칼란다간", 4, "S", "B", "S", "S"),]
race1=race("제1회 클로드배",2000,horses)
race1.show_entry()
winner=race1.run()
race1.show_result(winner)