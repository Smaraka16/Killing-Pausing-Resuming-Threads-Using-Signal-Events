import keyboard 
import threading
import time
event_pause = threading.Event() #PAUSE SIGNAL EVENT
event_kill = threading.Event()  #THREAD KILLING SIGNAL EVENT
def calculationProduct(n):
    for i in range(n):
        if event_pause.is_set(): #IF PAUSE FLAG IS SET TO TRUE
            while True:
                if not event_pause.is_set(): #IF PAUSE FLAG IS NOT SET TO TRUE
                    break
                continue
        elif event_kill.is_set(): #IF KILLING FLAG IS SET TO TRUE
            break     
        a = i*i
        time.sleep(.1)
        print(a)
    print(" ****** Execution is carried out successfully ******")
start = time.perf_counter()
t1 = threading.Thread(target = calculationProduct , args = (500,))
t1.start()
end = time.perf_counter()
print(f"Threading Time Taken is {end - start}")

#SETTING THREAD EVENT TO PAUSE
def pause():
    event_pause.set()
    time.sleep(0.2)
    print(" *** Pause signal is received ***")

#SETTING THREAD EVENT TO RESUME       
def resume():
    event_pause.set()
    time.sleep(0.2)
    print(" *** Resume signal is received ***")
    event_pause.clear()

#SETTING THREAD KILL EVENT    
def killThread():
    print(" *** Thread killing signal is received ***")
    time.sleep(0.2)
    print(' *** Thread was killed ***')
    event_kill.set()
     
     
     
     

#KEYBOARD SIGNALS
while True:
    if keyboard.is_pressed('p'):
        pause()
    elif keyboard.is_pressed('r'):
        resume()
    elif keyboard.is_pressed('k'):
        killThread()      
