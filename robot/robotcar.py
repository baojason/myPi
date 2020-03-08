#!/usr/bin/python
'''
L298N           RPi GPIO        RPi Pin

ENA             GPIO13 (PMW1)   33
IN1             GPIO5           29
IN2             GPIO6           31
IN3             GPIO14          8
IN4             GPIO15          10
ENB             GPIO18 (PWM0)   12

'''
import RPi.GPIO as IO
from time import sleep

IO.setwarnings(False)   #do not show any warnings
IO.setmode(IO.BOARD)    #we are programming the GPIO by BCM pin numbers. (PIN33 as 'GPIO13')

ENA = 33
IN1 = 29
IN2 = 31
IN3 = 8
IN4 = 10
ENB = 12

class myCar:
    def __init__(self, ena, in1, in2, in3, in4, enb, hz = 50):
        self.ena = ena
        self.in1 = in1
        self.in2 = in2
        self.in3 = in3
        self.in4 = in4
        self.enb = enb
        self.hz = hz

        IO.setup(self.ena,IO.OUT)    #initialize GPIO13 as an output.
        IO.setup(self.in1,IO.OUT)
        IO.setup(self.in2,IO.OUT)
        IO.setup(self.in3,IO.OUT)
        IO.setup(self.in4,IO.OUT)
        IO.setup(self.enb,IO.OUT)    #initialize GPIO18 as an output.

        IO.output(self.in1, False)   #Turn off all motors
        IO.output(self.in2, False)
        IO.output(self.in3, False)
        IO.output(self.in4, False)

        self.pwma = IO.PWM(self.ena, self.hz)   #set pin self.ena as PWM output, with self.hz frequency
        self.pwma.start(0)                      #generate PWM signal with 0% duty cycle
        self.pwmb = IO.PWM(self.enb, self.hz)   #set pin self.enb as PWM output, with self.hz frequency
        self.pwmb.start(0)                      #generate PWM signal with 0% duty cycle

        self.dir = {
            "stop" : 0b0000,
            "fwrdLeft" : 0b0001,
            "bwrdLeft" : 0b0010,
            "stop1" : 0b0011,
            "bwrdRight" : 0b0100,
            "clockwise" : 0b0101,
            "backward" : 0b0110,
            "bwrdRight1" : 0b0111,
            "fwrdRight" : 0b1000,
            "forward" : 0b1001,
            "counterclock" : 0b1010,
            "fwrdRight1" : 0b1011,
            "stop2" : 0b1100,
            "fwrdLeft1" : 0b1101,
            "bwrdLeft1" : 0b1110,
            "stop3" : 0b1111
        }

    def __setDirection(self, dir):
        dircode = self.dir[dir]
        dir1 = (dircode & 0b1000) != 0
        dir2 = (dircode & 0b0100) != 0
        dir3 = (dircode & 0b0010) != 0
        dir4 = (dircode & 0b0001) != 0
        IO.output(self.in1, dir1)
        IO.output(self.in2, dir2)
        IO.output(self.in3, dir3)
        IO.output(self.in4, dir4)

    def stop(self):
        self.pwma.stop()
        self.pwmb.stop()

    def forward(self, speed, duration):
        self.__setDirection("forward")
        self.pwma.start(speed)
        self.pwmb.start(speed)
        sleep(duration)
        self.stop()

    def backward(self, speed, duration):
        self.__setDirection("backward")
        self.pwma.start(speed)
        self.pwmb.start(speed)
        sleep(duration)
        self.stop()

    def fwrdLeft(self, speed, duration):
        self.__setDirection("fwrdLeft")
        self.pwma.start(speed)
        self.pwmb.start(speed)
        sleep(duration)
        self.stop()

    def fwrdRight(self, speed, duration):
        self.__setDirection("fwrdRight")
        self.pwma.start(speed)
        self.pwmb.start(speed)
        sleep(duration)
        self.stop()

    def bwrdLeft(self, speed, duration):
        self.__setDirection("bwrdLeft")
        self.pwma.start(speed)
        self.pwmb.start(speed)
        sleep(duration)
        self.stop()

    def bwrdRight(self, speed, duration):
        self.__setDirection("bwrdRight")
        self.pwma.start(speed)
        self.pwmb.start(speed)
        sleep(duration)
        self.stop()


if __name__=='__main__':
    robotCar = myCar(ENA, IN1, IN2, IN3, IN4, ENB)
    robotCar.forward(100, 1)
    sleep(1)
    robotCar.backward(50, 1)
    sleep(1)
    robotCar.fwrdLeft(50, 1)
    sleep(1)
    robotCar.fwrdRight(50, 1)
    sleep(1)
    robotCar.bwrdLeft(50, 1)
    sleep(1)
    robotCar.bwrdRight(50, 1)
    sleep(1)

'''
try:
    while 1:                #execute loop forever

        for x in notes:
            p.ChangeFrequency(x)
            time.sleep(0.1)

        for x in range (hz, hz+500):
            p.ChangeFrequency(x)
            time.sleep(0.1)
        for x in range (50):        #execute loop for 50 times, x being incremented from 0 to 49.
            p.ChangeDutyCycle(x)    #change duty cycle for varying the brightness of LED.
            time.sleep(0.1)         #sleep for 100m second

        for x in range (50):        #execute loop for 50 times, x being incremented from 0 to 49.
            p.ChangeDutyCycle(50-x) #change duty cycle for changing the brightness of LED.
            time.sleep(0.1)         #sleep for 100m second
except KeyboardInterrupt:
    p.stop()
    IO.cleanup()
'''
