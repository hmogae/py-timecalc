nowh = int(input("현재시각을 입력하세요 (h): "))
nowm = int(input("현재시각을 입력하세요 (m): "))
nows = int(input("현재시각을 입력해주세요 (s): "))
seconds = int(input("더할 초를 입력하세요: "))

nowh = (seconds // 60) // 60
hours = (seconds // 60) // 60
nowm = (seconds // 60) % 60
minutes = (seconds // 60) % 60
now = seconds % 60
seconds = seconds % 60

h = hours + now
m = minutes + now
s = seconds + now

print(f"{h}시 {m}분 {s}초")
