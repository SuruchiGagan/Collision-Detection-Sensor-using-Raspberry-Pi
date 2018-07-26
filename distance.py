import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

TRIG = 11
ECHO = 12
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.output(3,1)
GPIO.output(5,1)
GPIO.output(7,1)
GPIO.output(8,1)
GPIO.output(13,1)
GPIO.output(16,1)
GPIO.cleanup(15)

GPIO.setup(38,GPIO.IN)
GPIO.setup(40,GPIO.IN)
while True:
 if GPIO.input(40) == 0:
   try:
     while True:


         GPIO.setup(TRIG,GPIO.OUT)
         GPIO.output(TRIG,0)

         GPIO.setup(ECHO,GPIO.IN)

         time.sleep(0.1)


         GPIO.output(TRIG,1)
         time.sleep(0.00001)
         GPIO.output(TRIG,0)

         while GPIO.input(ECHO) == 0:
               pass
         start = time.time()

         while GPIO.input(ECHO) == 1:
          pass

         stop = time.time()

         diff = stop-start

         x1= diff*17000
         
         GPIO.output(TRIG,1)
         time.sleep(0.00001)
         GPIO.output(TRIG,0)

         while GPIO.input(ECHO) == 0:
               pass
         start = time.time()

         while GPIO.input(ECHO) == 1:
          pass

         stop = time.time()

         diff = stop-start

         x2= diff*17000
         
         x=(x1+x2)/2
         GPIO.setup(3,GPIO.OUT)
         GPIO.setup(5,GPIO.OUT)
         GPIO.setup(7,GPIO.OUT)
	 GPIO.setup(8,GPIO.OUT)
	 GPIO.setup(13,GPIO.OUT)
	 GPIO.setup(16,GPIO.OUT)
         GPIO.setup(15,GPIO.OUT)
         GPIO.setup(38,GPIO.IN)
         GPIO.setup(40,GPIO.IN)

         while (x>200):
               GPIO.output(3,0)
               GPIO.output(5,0)
               GPIO.output(7,0)
               GPIO.output(8,0)
               GPIO.output(13,0)
               GPIO.output(16,1)
               GPIO.cleanup(15)
               print("The obstacle is very very far at a distance =",x,"cms")
               break 
         while (x<200 and x>=150):
               GPIO.output(3,1)
               GPIO.output(5,0)
               GPIO.output(7,0)
               GPIO.output(8,0)
               GPIO.output(13,0)
               GPIO.output(16,0)
               GPIO.cleanup(15)
               print("The obstacle is very far at a distance =",x,"cms")
               break        
         while (x<150 and x>=100):
               GPIO.output(3,1)
               GPIO.output(5,1)
               GPIO.output(7,0)
               GPIO.output(8,0)
               GPIO.output(13,0)
               GPIO.output(16,0)
               GPIO.cleanup(15)
               print("The obstacle is very far at a distance =",x,"cms")
               break
         while (x<100 and x>=75):
               GPIO.output(3,1)
               GPIO.output(5,1)
               GPIO.output(7,1)
               GPIO.output(8,0)
               GPIO.output(13,0)
               GPIO.output(16,0)
               GPIO.output(15,1)
               print("The obstacle is far at a distance =",x,"cms")
               break
         while (x<75 and x>=50):
               GPIO.output(3,1)
               GPIO.output(5,1)
               GPIO.output(7,1)
               GPIO.output(8,1)
               GPIO.output(13,0)
               GPIO.output(16,0)
               GPIO.output(15,1)
               print("The obstacle is coming closer and is at a distance =",x,"cms")
               break
         while (x<50 and x>=25):
               GPIO.output(3,1)
               GPIO.output(5,1)
               GPIO.output(7,1)
               GPIO.output(8,1)
               GPIO.output(13,1)
               GPIO.output(16,0)
               GPIO.output(15,1)
               print("The obstacle is very close at a distance =",x,"cms")
               break
         while (x<25):
               GPIO.output(3,1)
               GPIO.output(5,1)
               GPIO.output(7,1)
               GPIO.output(8,1)
               GPIO.output(13,1)
               GPIO.output(16,1)
               GPIO.output(15,0)
               print("!!!! WARNING!!!! the obstacle is about to collide and is at a distance =",x,"cms")
               break
         if GPIO.input(38) == 0:
               GPIO.cleanup(3)
               GPIO.cleanup(5)
               GPIO.cleanup(7)
               GPIO.cleanup(8)
               GPIO.cleanup(13)
               GPIO.cleanup(15)
               GPIO.cleanup(16)
               break
   except KeyboardInterrupt:
        
        GPIO.output(3,0)
        GPIO.output(5,0)
        GPIO.output(7,0)
        GPIO.output(8,0)
        GPIO.output(13,0)
        GPIO.output(16,0)
        GPIO.cleanup(15)

        exit()
