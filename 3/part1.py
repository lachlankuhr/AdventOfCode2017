import math

DATA = 361527
# Used my brain 
# I'm also a mathematics student so it's okay ;) 
sizeRoundDown = int(math.sqrt(DATA)) # it's a sqaure so take the square root to get size
leftOver = DATA - sizeRoundDown*sizeRoundDown # how many squares are left in the outer layer? 
horizontal = (sizeRoundDown - 1) / 2 # remove center and half to get back
vertical = abs(leftOver - (sizeRoundDown - 1)/2) # analogous logic 
totalDistance = horizontal + vertical
print("Horizontal: " + str(horizontal))
print("Vertical: " + str(vertical))
print("Total distance: " + str(totalDistance))