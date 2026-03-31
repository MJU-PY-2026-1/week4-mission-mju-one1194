# 파일이름 : main.py
# 작 성 자 : 제갈원
# 하 는 일 : 도장깨기 : 나만의 버킷리스트

bucket_list = []

restaurant1= input("맛집 리스트 입력: ")
bucket_list.append(restaurant1)

restaurant2 = input("맛집 리스트 입력: ")
bucket_list.append(restaurant2)

restaurant3 = input("맛집 리스트 입력: ")
bucket_list.append(restaurant3)

print(f"리스트 : {bucket_list}")

restaurnat4 = input("맛집 리스트 추가: ")

bucket_list.insert(0,restaurnat4)

print(f"리스트 : {bucket_list}")

restaurant = input("도장깨기: ")

bucket_list.remove(restaurant)

print(f"리스트 : {bucket_list=}")