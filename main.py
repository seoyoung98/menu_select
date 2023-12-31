import random

# 식당
menu_sort = ["한식", "아시안", "양식", "디저트", "편의점", "럭셔리"]

korean_restaurant = [
    "또보겠지 떡볶이집", "소풍", "한(제육)", "홍반장(순대국)", "미소국수(국수, 떡국)", "밥장인 돼지찌개",
    "제주은희네 해장국", "일미식당", "아우네돼지불백", "먹보식당", "정성이 가득찬 집밥", "혼고집", "이대조뼈다귀",
    "무무닭갈비", "배꼽시계", "월강부산돼지국밥", "감나무 기사식당", "낭풍 김치찌개", "홍대순대국", "찰스숯불김밥"
]
# korean_food = []
asian_restaurant = [
    "우동가조쿠", "고쿠텐(텐동)", "명동왕돈까스", "짬뽕위에 더 짬뽕", "온미동(덮밥)", "토모토카레",
    "어사출또(칼국수,회덮밥)", "올바른 스시", "오레타치카레", "샤브로21", "리리마카오", "오군수제돈까스",
    "포포야어묵(나베)", "사루카메", "베트남이랑", "저스트 텐동", "연남쌀국수", "마라탕집 찾아서 넣기"
]
# asian_food = [""]
yangsik_restaurant = ["다운타우너", "치버킹", "프랭크버거"]
# yangsik_food = []
cafe = ["카페게이트", "스타벅스", "투썸", "할리스", "에그셀런트"]
cafe_food = ["샌드위치", "베이글", "치아바타", "스프"]
convient_food = ["라면", "도시락", "삼각김밥", "컵밥"]
luxury_restaurant = ["낙곱새미장원", "스시엔준", "유부(스시)"]


# 어떤 식으로 고를지, 아예 랜덤, 종류는 정할지 함수
def random_menu():
  print("메뉴를 정하기 어려우신가요? 당신의 점심 메뉴를 정해드립니다.")
  # print("번호를 골라주세요.")
  print("----------------------------------------------------------------")
  print("1. 아예 못 고르겠어요. | 2. 종류 선택할래요.")
  print("----------------------------------------------------------------")
  print("선택 >> ", end='')


# 종류를 알려주는 메뉴
# 종류 선택이 가능할 때 보여준다.
# 그냥도 보여줄지 고민해보기
# 인터페이스 어떻게 생긴지 고민해보기
def menu():
  print("----------------------------------------------------------------")
  print("1. 한식 | 2. 아시안 | 3. 양식 | 4. 디저트 | 5. 편의점 | 6. 럭셔리")
  print("----------------------------------------------------------------")
  print("선택 >> ", end='')


# 식당 결과
def result():
  print("당신이 갈 식당은 => ", end='')


# 편의점 음식 결과, 나중에 종류가 더 생기면 추가하기
def con_result():
  print("당신이 먹을 음식은 => ", end='')


#
def res_sort_choice(arr):
  res_choice = random.choice(arr)
  result()
  print(res_choice)


# 시작
random_menu()
random_select = int(input())
if random_select == 1:  # 1번
  choice1 = random.choice(menu_sort)
  print(choice1)
  if choice1 == "한식":
    res_sort_choice(korean_restaurant)
  elif choice1 == "아시안":
    res_sort_choice(asian_restaurant)
  elif choice1 == "양식":
    res_sort_choice(yangsik_restaurant)
  elif choice1 == "카페":
    res_sort_choice(cafe)
  elif choice1 == "편의점":
    res_choice = random.choice(convient_food)
    con_result()
    print(res_choice)
  else:
    res_sort_choice(luxury_restaurant)
else:  # 2번
  menu()
  # 종류 선택받기
  restaurant_select = int(input())
  if restaurant_select == 1:  # 한식 식당
    res_sort_choice(korean_restaurant)
  elif restaurant_select == 2:  # 아시안 식당
    res_sort_choice(asian_restaurant)
  elif restaurant_select == 3:  # 양식 식당
    res_sort_choice(yangsik_restaurant)
  elif restaurant_select == 4:  # 카페, 디저트류
    res_sort_choice(cafe)
  elif restaurant_select == 5:  # 편의점 메뉴
    choice2 = random.choice(convient_food)
    con_result()
    print(choice2)
  else:  # 고오급 메뉴
    res_sort_choice(luxury_restaurant)
