#日付の取得
import datetime
 
 
today = datetime.date.today()
todaydetail = datetime.datetime.today()
 
# 今日の日付
print('----------------------------------')
print(today)
print(todaydetail)
 
# 今日に日付：それぞれの値
print('----------------------------------')
print(today.year)
print(today.month)
print(today.day)
print(todaydetail.year)
print(todaydetail.month)
print(todaydetail.day)
print(todaydetail.hour)
print(todaydetail.minute)
print(todaydetail.second)
print(todaydetail.microsecond)
 
# 日付のフォーマット
print('----------------------------------')
print(today.isoformat())
print(todaydetail.strftime("%Y/%m/%d %H:%M:%S"))

#日付の計算
import datetime
 
 
today = datetime.datetime.today()
 
# 今日の日付
print(today)
 
# 明日の日付
print(today + datetime.timedelta(days=1))
 
newyear = datetime.datetime(2010, 1, 1)
 
# 2010年1月1日の一週間後
print(newyear + datetime.timedelta(days=7))
 
# 2010年1月1日から今日までの日数
calc = today - newyear
 
# 計算結果の戻り値は「timedelta」
print(calc.days)

#うるう年の判定
import calendar
 
print(calendar.isleap(2015))
print(calendar.isleap(2016))
print(calendar.isleap(2017))
 
print(calendar.leapdays(2010, 2020))