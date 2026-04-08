import time
timer=int(input("Enter the timer value"))

while timer>0:
    sec=timer%60
    min=int(timer/60)%60
    hours=int(timer/3600)
    print(f"{hours:02}:{min:02}:{sec:02}")
    timer-=1
    time.sleep(1)
print("time up")