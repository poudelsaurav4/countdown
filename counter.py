import time

def CountDown(t):
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
      
    print('times up !!') 

t = input("Enter the time in seconds: ") 

CountDown(int(t)) 