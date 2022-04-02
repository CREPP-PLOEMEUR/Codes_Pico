from machine import Pin
import utime


broches = [
    Pin(10,Pin.OUT),#IN1 p5
    Pin(11,Pin.OUT),#IN2 p4
    Pin(12,Pin.OUT),#IN3 p3
    Pin(13,Pin.OUT),#IN4 p2
    ]

moteur1 = Pin(9, Pin.OUT)  # p6  14
moteur2 = Pin(14, Pin.OUT)  # p7  15

moteur1(1)  # moteur 1 marche, 0  arrêt
moteur2(1)  # moteur 2 marche, 0  arrêt

full_step_sequence = [
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1]
    ]
print("Hello World")

while True:
    for step in full_step_sequence:
        print("step= ", step, " --> ")
        for i in range(len(broches)):
            broches[i].value(step[i])
            utime.sleep(0.001)
            
            print("i=", i,"/",len(broches),": ", broches[i],".",i, end="")
            print(" =", step[i])
