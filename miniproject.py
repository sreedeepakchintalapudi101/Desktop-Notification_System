import time
from win10toast import ToastNotifier
import datetime
 
def getTimeInput(): 
    hour = int(input("hours of interval :")) 
    minutes = int(input("Mins of interval :")) 
    seconds = int(input("Secs of interval :")) 
    time_interval = seconds+(minutes*60)+(hour*3600) 
    return time_interval
 
def log():
    now=datetime.datetime.now()
    start_time=now.strftime("%H:%M:%S")
 
def notify():
    notification=ToastNotifier()
    notification.show_toast("Time to take a break")
    log()
    
def starttime(time_interval):
    while True:
        time.sleep(time_interval)
        notify()
if __name__=="__main__":
    time_interval=getTimeInput()
    starttime(time_interval)
