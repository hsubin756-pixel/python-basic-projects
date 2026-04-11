class horse:
    def __init__(self,age,name,agility,stamina,indurance,competence):
        self.age=age
        self.name=name
        self.agility=agility
        self.stamina=stamina
        self.indurance=indurance
        self.competence=competence
    def show_info(self):
        print(f"나이:{self.age}")
        print(f"이름:{self.name}")
        print(f"속도:{self.agility}")
        print(f"스태미너:{self.stamina}")
        print(f"근성:{self.indurance}")
        print(f"거리적성:{self.competence}")
    def run(self):
        track="🐴"+"─" *self.agility+"💨"
        print(f"{self.name}:{track}")
horse1=horse(3,"벨페고르",9,6,8,"S")
horse2=horse(3,"템페스터",8,6,7,"S")
horse3=horse(3,"제피로스",6,9,8,"S")
horse4=horse(3,"아이올로스",7,7,9,"S")
print("="*40)
print("🏇 출전마 소개 🏇")
print("="*40)
horse1.show_info()
horse2.show_info()
horse3.show_info()
horse4.show_info()
print("="*40)
print("🏁 달리기 미리보기 🏁")
print("="*40)
horse1.run()
horse2.run()
horse3.run()
horse4.run()
