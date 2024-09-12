import math

def getCylinderVolume(radius, height) :
    volume = math.pi * (radius ** 2) * height
    return volume

x = getCylinderVolume(10, 12)
y = getCylinderVolume(2, 6)
print(round(x,4))
print(round(y,4))
print(int(x))

def getNumberOfSlices(radius, height, volumeOfSlice) :
    volume = getCylinderVolume(radius, height)
    numberOfSlices = volume / volumeOfSlice
    return int(numberOfSlices)

numberOfSlices1 = getNumberOfSlices(10, 10, 100)
print(numberOfSlices1)