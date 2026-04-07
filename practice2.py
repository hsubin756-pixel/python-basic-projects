## 가변 인자:여러 개의 인자를 보따리(*)로 받아 쉼표(join)로 연결하는 프로필 함수
def profile(name,age,*language):
    # end: 출력 끝에 줄바꿈 대신 문구 추가
    print(f"이름:{name},나이:{age}",end=",작전:")
    # join: 보따리 속 내용물 사이에 ", "를 넣어 합치기
    print(", ".join(language))
profile("메지로 맥퀸",20,"선행","강선행","도주")

carrot=10 # 함수 밖 변수
def checkpoint(horses):
    # '함수 밖의 carrot을 가져다 쓰겠다'는 선언
    global carrot # global: 함수 밖의 보따리(변수)를 안으로 들여오기
    # 함수 안에서 밖의 변수를 수정하려면 'global' 통행증이 필요함
    # 전역 변수(Global) = 공용 물품 / 지역 변수(Local) = 개인 소지품
    carrot=carrot-horses
    print(f"남은 당근:{carrot}")
checkpoint(2)

def dog_to_human_age(age,size):
    if size=="소형":
        human_age=age*5
    elif size=="대형":
        human_age=age*7
    return human_age
dog_age=3
dog_size="소형"
result=(dog_to_human_age(dog_age,dog_size))
print(f"우리 강아지의 나이는{result}살 입니다.")

def std_weight(height,gender):
    my_height=height/100
    if gender=="남성":
        weight=my_height*my_height*22
    elif gender=="여성":
        weight=my_height*my_height*21
    return weight
height=175
gender="남성"
result=(std_weight(height,gender))
print(f"키{height}cm의 평균 체중은{result:.2f}kg입니다.")

    

