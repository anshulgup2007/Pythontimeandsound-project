import time
import winsound
print('%s'% time.ctime())
time.sleep(5)
frequency = 1000
duration = 2000 
winsound.Beep(frequency, duration)
print('%s'% time.ctime())

#using this program we can create an alarm 
