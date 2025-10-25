from machine import Pin
from time import sleep
led1=Pin(1,Pin.OUT)
led2=Pin(5,Pin.OUT)
led3=Pin(13,Pin.OUT)
while True:
  led1.on()
  led2.off()
  led3.off()
  sleep(1)
  led2.on()
  led1.off()
  led3.off()
  sleep(1)
  led1.off()
  led3.on()
  led2.off()
  led1.off()
  sleep(1)
  

   
  


