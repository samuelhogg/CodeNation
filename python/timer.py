import time

def timer(): 
    t = 1*60
    print("Time starts now!")
    while t > 0: 
      mins = t // 60 
      secs = t % 60
      timer = '{:02d}:{:02d}'.format(mins, secs) 
      print(timer, end="\r") # overwrite previous line 
      time.sleep(1)
      t -= 1 
    else:
        print("Times up!! Say Goodbye to your teacher")

timer()


