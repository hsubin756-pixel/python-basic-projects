import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def scrape_horse(driver,url):# 기계를 만들고
    print(f"\n 수집 중:{url}")
    driver.get(url)
    try:
        WebDriverWait(driver,15).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR,"table.db_h_race_results"
            )))
    except Exception as e:
        print(f"경주 테이블 로딩 실패:{url}")
        return None
    soup=BeautifulSoup(driver.page_source,"html.parser")
    # --- 이름 ---
    horse_name="알 수 없음"
    title_tag=soup.find("title")
    if title_tag:
        horse_name=title_tag.text.split("|")[0].strip()
    # --- 성별 / 털색 ---
    gender,color="정보없음","정보없음"
    txt_info=soup.find("p",class_="txt_01")
    if txt_info:
        parts=txt_info.text.strip().replace("\n","").split()
        if len(parts)>=2:
            gender,color=parts[0],parts[1]
        if len(parts)>=3:
            gender,color=parts[1],parts[2]
    # --- 생년월일 ---
    birth_date="정보없음"
    prof_table=soup.find("table",class_="db_prof_table")
    if prof_table:
        for row in prof_table.find_all("tr"):
            th=row.find("th")
            td=row.find("td")
            if th and td and "生年月日" in th.text:
                birth_date=td.text.strip()
    # --- 조교사 ---
    trainer="정보없음"
    if prof_table:
        for row in prof_table.find_all("tr"):
            th=row.find("th")
            td=row.find("td")
            if th and td and "調教師" in th.text:
                trainer=td.text.strip()
                break
    # --- 통산 성적 ---
    total_record="정보없음"
    if prof_table:
        for row in prof_table.find_all("tr"):
            th=row.find("th")
            td=row.find("td")
            if th and td and "通算成績" in th.text:
                total_record=td.text.strip()
                break
    # --- 경주 기록 (전체) ---
    races=[]
    race_table=soup.select_one("table.db_h_race_results")
    if race_table:
        thead=race_table.find("thead")
        tbody=race_table.find("tbody")
        header_row=thead.find("tr")if thead else race_table.find("tr")
        data_rows=(tbody.find_all("tr")if tbody
                   else race_table.find_all("tr")[1:])
        # 헤더에서 컬럼 위치 자동 매핑
        col_map={}
        if header_row:
            for idx,cell in enumerate(header_row.find_all(["th","td"])):
                col_map[cell.get_text(strip=True)]=idx
            def find_col(keywords):
                for name,idx in col_map.items():
                    if any(kw in name for kw in keywords):
                        return idx
                return None
            idx_date    = find_col(["日付"])
            idx_venue   = find_col(["開催"])
            idx_race    = find_col(["レース"])
            idx_rank    = find_col(["着順"])
            idx_jockey  = find_col(["騎手"])
            idx_dist    = find_col(["距離"])
            idx_pop     = find_col(["人気"])
            idx_heads   = find_col(["頭数"])
            for row in data_rows:
                cols=row.find_all("td")
                if not cols:
                    continue
                def get(idx):
                    if idx is not None and idx<len(cols):
                        return cols[idx].get_text(strip=True)
                    return""
                races.append({
                    "일자":   get(idx_date),
                    "개최":   get(idx_venue),
                    "레이스": get(idx_race),
                    "착순":   get(idx_rank),
                    "기수":   get(idx_jockey),
                    "거리":   get(idx_dist),
                    "인기":   get(idx_pop),
                    "두수":   get(idx_heads),
                        })       
    result = {
        "url":      url,
        "이름":     horse_name,
        "성별":     gender,
        "털색":     color,
        "생년월일": birth_date,
        "조교사":   trainer,
        "통산성적": total_record,
        "총출주":   len(races),
        "경주기록": races,
    }

    print(f"{horse_name}-{len(races)}건 수집 완료")
    return result

# ============================================================
#  [파트 B] 실행 부분 - 실제로 수집할 말 목록을 넣고 돌리기
# ============================================================

# ★ 여기에 수집하고 싶은 말들의 URL을 넣으세요!
# 넣고 싶은 만큼 추가할 수 있습니다.

horse_urls=[
"https://db.netkeiba.com/horse/1994100530/",
"https://db.netkeiba.com/horse/1994103997/",   
"https://db.netkeiba.com/horse/1997103038/",
]
# --- 브라우저 준비 ---
options=Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
# ✅ 수정 (최신 Selenium은 이 한 줄이면 끝)
driver = webdriver.Chrome(options=options)
try:
    print("="*60)
    print(f"    경마 데이터 수집 시작({len(horse_urls)}마리)")
    print("="*60)

    all_results=[]
    for url in horse_urls:
        result=scrape_horse(driver,url)
        if result is not None:
            all_results.append(result)
        else:
            print(f" 건너뜀:{url}")
    time.sleep(2)
    with open("horse_datebase.csv","w",encoding="utf-8-sig",
              newline="")as f:
        writer=csv.writer(f)
        writer.writerow(["이름","성별","털색","생년월일",
                         "조교사","통산성적","총출주수","URL"])
        for r in all_results:
            writer.writerow([
                r["이름"],r["성별"],r["털색"],r["생년월일"],r["조교사"],r["통산성적"],r["총출주"],
                r["url"]])
    with open("race_history_all.csv","w",encoding="utf-8-sig",
              newline="")as f:
        writer=csv.writer(f)
        writer.writerow(["말이름","일자","개최","레이스","착순"
                         ,"기수","거리","인기","두수"])
        for r in all_results:
            for race in r["경주기록"]:
                writer.writerow([
                    r["이름"],
                    race["일자"], race["개최"], race["레이스"],
                    race["착순"], race["기수"], race["거리"],
                    race["인기"], race["두수"]
                ])
        print("\n"+"="*60)
        print(" 수집 완료 보고서")
        print("="*60)
        for r in all_results:
            print(f"\n  {r['이름']}")
            print(f"    성별/털색: {r['성별']}/{r['털색']}")
            print(f"    생일:   {r['생년월일']}")    
            print(f"    통산성적: {r['통산성적']}")
            print(f"    경주 기록: {r['총출주']}건")

            for i,race in enumerate(r["경주기록"][:3]):
                print(f"    [{i+1}]{race['일자']}{race['레이스']}"
                      f"→{race['착순']}착 (기수: {race['기수']})")
            print(f"\n → 'horse_datebase.csv' 저장")
            print(f"  → 'race_history_all.csv' 저장 "
                f"(전체 경주 {sum(r['총출주'] for r in all_results)}건)")
            print("=" * 60)
 
finally:
    driver.quit()

