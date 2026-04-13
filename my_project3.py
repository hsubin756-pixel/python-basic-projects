import requests
from bs4 import BeautifulSoup

url = "https://db.netkeiba.com/horse/1994100530/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url, headers=headers)
# 한글이나 일본어가 깨지지 않게 인코딩 설정을 추가
response.encoding = response.apparent_encoding 

soup = BeautifulSoup(response.content, "html.parser")

# 1. 상단 요약 정보 가져오기
txt_info=soup.find("p",class_="txt_01")
if txt_info:
    # .split() 안에 아무것도 안 적으면 어떤 종류의 빈칸이든 다 잘라줌
    info_list=txt_info.text.split()
    status=info_list[0]
    gender=info_list[1]
    color=info_list[2]
    print("---[정리된 요약정보]---")
    print(f"상태:{status}")
    print(f"성별:{gender}")
    print(f"털색:{color}")

# 1. 문서의 가장 꼭대기 <title> 태그를 찾기
title_tag = soup.find("title")

if title_tag:
    
    horse_name=title_tag.text.split("|")[0].strip()
    print(f"\n이름: {horse_name}")
else:
    print("이 사이트는 제목도 없네요... 주소를 다시 확인해볼까요?")
