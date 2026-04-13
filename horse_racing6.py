import random
import time

# ==========================================
# 1. 기본 데이터 세팅 (말 정보)
# ==========================================
horses = [
    {"이름": "미션 트라이엄프", "스킬이름": "mission triumph", "발동확률": 0.15, "추가속도": 5.8},
    {"이름": "천랑성의 시리우스", "스킬이름": "추상의 트로이메라이", "발동확률": 0.25, "추가속도": 3},
    {"이름": "노 리즌", "스킬이름": "지소기전,백전불태", "발동확률": 0.2, "추가속도": 4},
    {"이름": "마그마 케이브", "스킬이름": "화산 폭발", "발동확률": 0.10, "추가속도": 8},
    {"이름": "라이칸 쓰로프", "스킬이름": "만월", "발동확률": 0.18, "추가속도": 4.2}
]
# 6번마 추가
horses.append({"이름": "저스틴 팰리스", "스킬이름": "페인킬러", "발동확률": 0.2, "추가속도": 4})


# ==========================================
# 2. 게임에 필요한 함수들 정의
# ==========================================

# --- 함수 1: 출전마 소개 ---
def show_horses():
    print("="*50)
    print("       🏇 출전마 소개 🏇 ")
    print("="*50)
    for i, horse in enumerate(horses):
        chance_pct = int(horse["발동확률"]*100)
        print(f" {i+1}번마: {horse['이름']}")
        print(f"        스킬: [{horse['스킬이름']}] 발동 {chance_pct}% / 속도 +{horse['추가속도']}")
    print("="*50)
    print()

# --- 함수 2: 배당률 계산 ---
def get_odds():
    odds = [] 
    for horse in horses:
        power = horse["발동확률"] * horse["추가속도"]
        rate = round(3.0 / (power + 0.5), 1)
        rate = max(1.5, min(6.0, rate))
        odds.append(rate)
    return odds

# --- 함수 3: 배팅하기 ---
def get_bet(money, odds):
    print(f"💰 현재 보유금: {money}원")
    print()
    while True:
        choice = input("배팅할 말 번호를 입력하세요(1~6): ")
        if choice in ["1", "2", "3", "4", "5", "6"]:
            choice = int(choice) - 1 
            break
        else:
            print("  ❌ 1~6 사이 숫자를 입력해주세요!")
            
    print(f"  →  {horses[choice]['이름']}을(를) 선택! (배당률 {odds[choice]}배)")
    print()
    
    while True:
        amount = input(f"배팅 금액을 입력하세요 (보유금: {money}원): ")
        if amount.isdigit() and 0 < int(amount) <= money:
            amount = int(amount)
            break
        else:
            print(f"    ❌ 1~{money}사이 금액을 입력해주세요!")
            
    print(f"  → {horses[choice]['이름']}에 {amount}원 배팅 완료!")
    print()
    return choice, amount

# --- 함수 4: 경주 실행 ---
def run_race():
    positions = [0, 0, 0, 0, 0, 0]
    skill_counts = [0, 0, 0, 0, 0, 0]
    records = []
    goal = 50
    turn = 0
 
    print("=" * 50)
    print("          🏁 경주 시작! 🏁")
    print("=" * 50)
    print()
 
    while len(records) < len(horses):
        turn = turn + 1
        print(f"--- {turn}턴 ---")
 
        for i in range(len(horses)):
            if positions[i] >= goal:
                if not any(r["이름"] == horses[i]["이름"] for r in records):
                    print(f"    {horses[i]['이름']}: 🏆 도착 완료")
                continue
 
            speed = random.randint(1, 5)
            skill_fired = False
 
            if random.random() < horses[i]["발동확률"]:
                speed = speed + horses[i]["추가속도"]
                skill_counts[i] = skill_counts[i] + 1
                skill_fired = True
 
            positions[i] = positions[i] + speed
 
            if positions[i] >= goal:
                positions[i] = goal
                rank = len(records) + 1
                records.append({
                    "순위": rank,
                    "이름": horses[i]["이름"],
                    "도착턴": turn,
                    "스킬발동": skill_counts[i]
                })
                if skill_fired:
                    print(f"  🏁 {horses[i]['이름']}: ✨[{horses[i]['스킬이름']}] 발동하며 골인! ({rank}등, {turn}턴)")
                else:
                    print(f"  🏁 {horses[i]['이름']}: 결승선 도착! ({rank}등, {turn}턴)")
            else:
                bar = "■" * int(positions[i] // 3)
                pos_display = round(positions[i], 1)
                if skill_fired:
                    print(f"  ✨ {horses[i]['이름']}: {bar} ({pos_display}) [{horses[i]['스킬이름']}] 발동! 속도+{horses[i]['추가속도']}")
                else:
                    print(f"    {horses[i]['이름']}: {bar} ({pos_display})")
 
        print()
        time.sleep(0.4)
 
    return records

# --- 함수 5: 결과 및 정산 (들여쓰기 수정 완료) ---
def show_result(records, bet_choice, bet_amount, odds, money):
    print("="*50)
    print("         🏆 최종 레이스 결과 🏆")
    print("=" * 50)
    
    medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣", "6️⃣"]
    my_horse_name = horses[bet_choice]["이름"]
    
    for record in records:
        rank = record["순위"]
        name = record["이름"]
        arrived = record["도착턴"]
        skills = record["스킬발동"]
        
        medal = medals[rank-1] if rank <= 6 else "🏁"
        marker = " ◀ MY BET" if name == my_horse_name else ""
        print(f"    {medal} {rank}등 | {name} | {arrived}턴 | 스킬 {skills}회 발동{marker}")
        
    print()
    winner_name = records[0]["이름"]
    
    # 여기서부터 들여쓰기가 함수 안으로 쏙 들어와야 합니다!
    if winner_name == my_horse_name:
        winnings = int(bet_amount * odds[bet_choice])
        money += winnings
        print(f"  🎉 적중! {my_horse_name} 1등!")
        print(f"  💰 {bet_amount}원 × {odds[bet_choice]}배 = {winnings}원 획득!")
    else:
        money -= bet_amount
        my_rank = 0
        for r in records:
            if r["이름"] == my_horse_name:
                my_rank = r["순위"]
        print(f"  😢 아쉽게 빗나감... {my_horse_name}은(는) {my_rank}등")
        print(f"  💸 {bet_amount}원 잃음...")
        
    print(f"  💰 현재 보유금: {money}원")
    print("=" * 50)
    return money
print("       🏁 경마 시뮬레이터 🏁")
print("="*50)
print()

# 초기 보유금 설정
my_money = 10000

# 1. 말 목록 보여주기
show_horses()

# 2. 배당률 미리 계산해두기
current_odds = get_odds()

# 3. 사용자에게 배팅 받기
bet_choice, bet_amount = get_bet(my_money, current_odds)

# 4. 경주 시작 대기
input("enter를 누르면 경주가 시작됩니다!")
print()

# 5. 경주 실행하고 결과 기록받기
race_records = run_race()

# 6. 최종 결과 보여주고 돈 정산하기
my_money = show_result(race_records, bet_choice, bet_amount, current_odds, my_money)
#while:아직 아무도 결승선(goal=30)에 도착하지 않았으면,
#계속해서 반복!
#while max(positions)<goal:
    #max()는 리스트에서 가장 큰 값을 찾는 함수.
    #가장 앞선 말이 아직 30이라는 값 미만이면 계속해서 반복시킴.
    #turn=turn+1
    #print(f"---{turn}턴---")
    #for i in range(len(horses)):
        #range(5)는 [0,1,2,3,4]까지 만들어줌.
        #i가 0부터 4까지 바뀌면서 차례대로 반복.
        #speed=random.randint(1,4)#1~10사이의 무작위 속도
        #positions[i]=positions[i]+speed#현재 위치에 속도만큼 더하기
        #트랙 그리기
        #track="■"*positions[i]
        #print(f"  {horses[i]}:{track}({positions[i]})")
        #          ↑↑↑↑↑↑↑↑↑         ↑↑↑↑↑↑↑↑↑↑↑↑
        #          horses에서           positions에서
        #          i번째 꺼내기          i번째 꺼내기
        # i=0일 때:
        #   horses[0] → "미션 트라이엄프"
        #   positions[0] → 1
        #   → "  미션 트라이엄프: ■ (1)"
    #print()
    #time.sleep(0.5)#0.5초 기다리게하는 명령

#while 반복이 끝남=누군가가 결승선에 도착!



