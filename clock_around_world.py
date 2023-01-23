import os
import time
from pytz import timezone
import keyboard 

def modern_clock():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') # clear the console
        # get current time in different time zones
        paris_time = time.strftime("%H:%M:%S", time.gmtime())
        london_time = time.strftime("%H:%M:%S", time.gmtime(time.time()+3600))
        new_york_time = time.strftime("%H:%M:%S", time.gmtime(time.time()-14400))
        los_angeles_time = time.strftime("%H:%M:%S", time.gmtime(time.time()-25200))
        shangai_time = time.strftime("%H:%M:%S", time.gmtime(time.time()+28800))
        # print the current time in different time zones
        print("Paris       : " + paris_time)
        print()
        print("London      : " + london_time)
        print()
        print("New York    : " + new_york_time)
        print()
        print("Los Angeles : " + los_angeles_time)
        print()
        print("Shangai     : " + shangai_time)
        time.sleep(1)
        if keyboard.is_pressed('s'):  #touche "s" pour arreter le programme 
            print("_____E__N__D_____")
            break  

modern_clock()
