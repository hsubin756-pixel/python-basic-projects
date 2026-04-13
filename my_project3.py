import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
 
# ★ 여기에 원하는 말의 URL을 넣으세요
url = "https://db.netkeiba.com/horse/1994100530/"
 
# --- 브라우저 설정 ---
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
 
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)
 
try:
    driver.get(url)
 
    # 경주 테이블이 로딩될 때까지 대기
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "table.db_h_race_results")
        )
    )
 
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
 
    # --- [1. 이름] ---
    horse_name = "알 수 없음"
    title_tag = soup.find("title")
    if title_tag:
        horse_name = title_tag.text.split("|")[0].strip()
 
    # --- [2. 성별 / 털색] ---
    status, gender, color = "정보없음", "정보없음", "정보없음"
    txt_info = soup.find("p", class_="txt_01")
    if txt_info:
        parts = txt_info.text.strip().replace("\n", " ").split()
        if len(parts) == 2:
            gender, color = parts[0], parts[1]
        elif len(parts) >= 3:
            status, gender, color = parts[0], parts[1], parts[2]
 
    # --- [3. 생년월일] ---
    birth_date = "정보없음"
    prof_table = soup.find("table", class_="db_prof_table")
    if prof_table:
        for row in prof_table.find_all("tr"):
            th = row.find("th")
            td = row.find("td")
            if th and td and "生年月日" in th.text:
                birth_date = td.text.strip()
                break
 
    # --- [4. 경주 기록] ---
    all_races = []
    race_table = soup.select_one("table.db_h_race_results")
 
    if race_table:
        # thead / tbody 분리
        thead = race_table.find("thead")
        tbody = race_table.find("tbody")
 
        header_row = thead.find("tr") if thead else race_table.find("tr")
        data_rows = (tbody.find_all("tr") if tbody
                     else race_table.find_all("tr")[1:])
 
        # 헤더 매핑
        col_map = {}
        if header_row:
            for idx, cell in enumerate(header_row.find_all(["th", "td"])):
                col_map[cell.get_text(strip=True)] = idx
 
        # 컬럼 인덱스 찾기
        def find_col(keywords):
            for name, idx in col_map.items():
                if any(kw in name for kw in keywords):
                    return idx
            return None
 
        idx_date    = find_col(["日付"])
        idx_venue   = find_col(["開催"])
        idx_weather = find_col(["天気"])
        idx_race    = find_col(["レース"])
        idx_heads   = find_col(["頭数"])
        idx_frame   = find_col(["枠番"])
        idx_number  = find_col(["馬番"])
        idx_odds    = find_col(["オッズ"])
        idx_pop     = find_col(["人気"])
        idx_rank    = find_col(["着順"])
        idx_jockey  = find_col(["騎手"])
        idx_weight  = find_col(["斤量"])
        idx_dist    = find_col(["距離"])
 
        # 데이터 추출
        for row in data_rows:
            cols = row.find_all("td")
            if not cols:
                continue
 
            def get(idx):
                if idx is not None and idx < len(cols):
                    return cols[idx].get_text(strip=True)
                return ""
 
            race = {
                "일자":   get(idx_date),
                "개최":   get(idx_venue),
                "날씨":   get(idx_weather),
                "레이스": get(idx_race),
                "두수":   get(idx_heads),
                "枠番":   get(idx_frame),
                "馬番":   get(idx_number),
                "오즈":   get(idx_odds),
                "인기":   get(idx_pop),
                "착순":   get(idx_rank),
                "기수":   get(idx_jockey),
                "근량":   get(idx_weight),
                "거리":   get(idx_dist),
            }
            all_races.append(race)
 
    # 최근 경주
    if all_races:
        r = all_races[0]
        recent_race = f"{r['레이스']} {r['착순']}착"
    else:
        recent_race = "기록없음"
 
    # --- [5. CSV 저장] ---
    # 기본 정보
    with open("uma_database.csv", "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["이름", "성별", "털색", "상태", "생년월일", "최근성적"])
        writer.writerow([horse_name, gender, color, status, birth_date, recent_race])
 
    # 전체 경주 기록
    if all_races:
        with open("uma_race_history.csv", "w", encoding="utf-8-sig", newline="") as f:
            writer = csv.writer(f)
            headers_csv = list(all_races[0].keys())
            writer.writerow(headers_csv)
            for race in all_races:
                writer.writerow([race.get(h, "") for h in headers_csv])
 
    # --- 결과 출력 ---
    print("\n" + "=" * 60)
    print(f"  이름:       {horse_name}")
    print(f"  성별/털색:  {gender} / {color}")
    print(f"  상태:       {status}")
    print(f"  생일:       {birth_date}")
    print(f"  최근성적:   {recent_race}")
    print(f"\n  전체 경주 기록: {len(all_races)}건")
    for i, r in enumerate(all_races):
        print(f"    [{i+1:2d}] {r['일자']} {r['개최']} "
              f"{r['레이스']:20s} → {r['착순']}착 "
              f"(기수: {r['기수']}, 거리: {r['거리']})")
    print(f"\n  → 'uma_database.csv' 저장 완료")
    print(f"  → 'uma_race_history.csv' 저장 완료 ({len(all_races)}건)")
    print("=" * 60)
 
finally:
    driver.quit()