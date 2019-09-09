from datetime import datetime

print("현재 날짜 시각 객체 얻기")
today = datetime.now()
print("today = datetime.noew",today)
print("년 월 일 : today.year, today.month, today.day : ", today.year, today.month, today.day )
print("시 분 초 : today.hour, today.minute, today.second : ",today.hour, today.minute, today.second)
print("요일 : ",today.weekday())
#요일 = 0 = 오늘에 해당하는 요일 ! 
print()
day = datetime(2019,1,1,0,0,0)
print("day = datetime(2019,1,1,0,0,0) : ",day)
print("2019년부터 지나온 시간 구하기")
print("today - day : ",today-day)
print()

#내가 태어난 날의 요일
birth = datetime(2002,7,1)
print("내가 태어난 날의 요일 (2002.7.1) : ","월화수목금토일"[birth.weekday()],"요일")
#"가나다[0] = 가"

#나는 몇일 살았을까 ?
print("나는 몇일 살았을까 ?(today - birth) : ",today-birth)

# 올해 크리스마스 며칠 남았을까 ?
ch = datetime(2019,12,25)
print("올해 크리스마스 며칠 남았을까 ? (ch - today) : ",ch - today)
