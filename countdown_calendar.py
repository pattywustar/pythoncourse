# 匯入模組
from tkinter import Tk, Canvas
from datetime import date, datetime

# 讀取文字檔
def get_events():
     list_events = []
     with open('events.txt') as file:
# 寫迴圈 #TODO:迴圈有錯待修正
         for line in file:
             line = line.rstrip('\n')
             current_event = line.split(',')
             event_date = datetime.strptime(current_event[1], '%d/%m/%y').date()
             current_event[1] = event_date
# 將活動放到自己新增的空陣列清單內
             list_events.append(current_event)
     return list_events 
# 計算天數
def days_between_dates(date1,date2):
    time_between= str(date1 - date2)
#拆字串
    number_of_days = time_between.split(' ')
    return number_of_days[0]
             
                  
# 建立畫布
root = Tk()
c = Canvas(root,width=800,height=800,bg='pink')
c.pack()

c.create_text(320,50,anchor='w',fill='yellow',\
    font='Arial 28 underline',text='我的倒數日曆')
# 取得所有活動資料 # TODO:等待修正
events = get_events()
today = date.today()

# 顯示結果
for event in events:
    event_name = event[0]
    days_until = days_between_dates(event[1],today)
    display = '這是 %s days 直到 %s' % (days_until, event_name)
    c.create_text(100,100 ,anchor ='w',fill='green',\
                  font='Arail 28', text= display)
    