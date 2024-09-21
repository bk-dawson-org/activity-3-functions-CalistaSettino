import math

r = int(input("Enter the side a of a triangle"))
s = int(input("Enter the side b of a triangle"))
t = int(input("Enter the side c of a triangle"))
sigfig = int(input("Enter the number of sigfigs"))

def calculateAngle(r,s,t) :
    '''
    This function calculates and returns the angle R in degrees
    parameters r,s,t : These are the sides of a triangle
    R : This is the angle of a triangle
    '''
    R = math.degrees(math.acos((r**2 - s**2 - t**2)/((-2)*s*t)))
    return R 

def findAngles(r,s,t) :
    '''
    This function displays the angle R, S, or T in degrees
    return: this function returns the angle of a triangle in degrees given sides r, s, and t
    '''
    findAngle = calculateAngle(r,s,t)
    return findAngle 

R = findAngles(r,s,t)
S = findAngles(s,r,t)
T = findAngles(t,s,r)
print(f'The angle R is {R:.{sigfig}g}')
print(f'The angle S is {S:.{sigfig}g}')
print(f'The angle T is {T:.{sigfig}g}') 