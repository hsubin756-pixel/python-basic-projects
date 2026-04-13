from bs4 import BeautifulSoup

import pprint

my_web_page = """
<ul class="race_results">
    <li class="horse">
        <span class="name">마스커레이드 볼</span>
        <span class="odds">2.5</span>
        <span class="jockey">르메르</span>
        <span class="rank">1</span>
    </li>
    <li class="horse">
        <span class="name">뮤지엄 마일</span>
        <span class="odds">5.4</span>
        <span class="jockey">데무로</span>
        <span class="rank">2</span>
    </li>
    <li class="horse">
        <span class="name">크루아 뒤 노르</span>
        <span class="odds">1.8</span>
        <span class="jockey">키타무라</span>
        <span class="rank">3</span>
    </li>
</ul>
"""

soup = BeautifulSoup(my_web_page, 'html.parser')
horses = soup.find_all('li', class_='horse')

# [미션] 빈 리스트를 하나 만듭니다. 여기에 오늘의 경주 정보를 다 담을 거예요.
today_race_db = []

for h in horses:
    name = h.find('span', class_='name').text
    odds = float(h.find('span', class_='odds').text) # 계산을 위해 숫자로 바꿉니다!
    jockey = h.find('span', class_='jockey').text
    rank = h.find('span',class_='rank').text
    
    # [중요] 각 말의 정보를 딕셔너리 형태로 묶어서 리스트에 추가(append)합니다.
    horse_list={
        "이름":name,
        "배당률":odds,
        "기수":jockey}
        
    # 리스트에 추가하는 코드를 여기에 작성해보세요! (힌트: append)
    today_race_db.append(horse_list)

# --- 확인 작업 ---
print(f"총 {len(today_race_db)}마리의 정보가 저장되었습니다.")
print("-" * 40)
print(f"{'순위':<5} | {'이름':<15} | {'배당률':<10} | {'기수':<10}")
print("-" * 40)
for i, horse in enumerate(today_race_db, 1):
    name = horse['이름']
    odds = horse['배당률']
    jockey = horse['기수']
    print(f"{i:<5} | {name:<15} | {odds:<10} | {jockey:<10}")

print("-" * 40)

import csv

# 1. 'race_result.csv'라는 이름의 파일을 쓰기(w) 모드로 만듭니다.
# newline=''은 줄바꿈이 두 번 되지 않게 막아주는 설정입니다.
with open('race_result.csv', 'w', encoding='utf-8-sig', newline='') as f:
    # 2. 엑셀 형식을 만들어주는 도구(writer) 준비
    writer = csv.writer(f)
    
    # 3. 맨 윗줄 제목(Header) 쓰기
    writer.writerow(['순위', '이름', '배당률', '기수'])
    
    # 4. 리스트에 저장된 말 정보를 한 줄씩 파일에 기록하기
    for i, horse in enumerate(today_race_db, 1):
        writer.writerow([i, horse['이름'], horse['배당률'], horse['기수']])

print("\n📂 'race_result.csv' 파일이 저장되었습니다! 폴더를 확인해 보세요.")