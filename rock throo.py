import numpy as np
import matplotlib as mlt
import matplotlib.pyplot as plt
import math

InitialVelocity = float(input("Enter a velocity in m/s: "))
InitialHeight = float(input("Enter a starting height in metres: "))
InitialAngle = float(input("Enter an angle in degrees upwards from horizontal: "))
InitialVelocityX = (math.cos(math.radians(InitialAngle)))*InitialVelocity
InitialVelocityY = (math.sin(math.radians(InitialAngle)))*InitialVelocity
#pi = math.pi
#AngleType = input(degree or radians)

EndPoint = max([((-1)*InitialVelocityY + math.sqrt(InitialVelocityY**2 - (4*(-4.9)*InitialHeight))) / (2*(-4.9)), ((-1)*InitialVelocityY - math.sqrt(InitialVelocityY**2 - (4*(-4.9)*InitialHeight))) / (2*(-4.9))])

time = np.arange(0,(EndPoint+.01),0.01)
height = InitialHeight + (math.sin(math.radians(InitialAngle)))*time*InitialVelocity - 4.9*(time**2)

distance = InitialVelocityX*time

def rockthrow():
    fig = plt.figure()

    ax1 = fig.add_subplot(311)
    ax1.set_ylabel("height")
    ax1.set_title("rock thrown")
    ax1.set_xlabel("seconds")
    line, = ax1.plot(time,height,color = "blue")
    
    ax2 = fig.add_subplot(312)
    ax2.set_ylabel("distance")
    ax2.set_xlabel("time")
    ax2.set_title("distance reached")
    line, = ax2.plot(time,distance,color = "blue")
    
    ax3 = fig.add_subplot(313)
    ax3.set_ylabel("height")
    ax3.set_xlabel("distance")
    line, = ax3.plot(distance,height,color = "blue")
	
    plt.show()
	
print("InitialVelocity = " +str(InitialVelocity))
print("Initial Height = " +str(InitialHeight))
print("InitialAngle = " + str(InitialAngle) + " degrees")
print("EndPoint = " +str(EndPoint))

rockthrow()
