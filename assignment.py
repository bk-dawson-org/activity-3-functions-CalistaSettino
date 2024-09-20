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
    This function displays the angles R, S, and T in degrees
    parameters R, S, T: These are the angles of a triangle
    return: this function returns the angles R, S and T in degrees
    '''
    findAngle = calculateAngle(r,s,t)
    return findAngle 

R = findAngles(r,s,t)
S = findAngles(s,r,t)
T = findAngles(t,s,r)
print(f'The angle R is {R:.{sigfig}g}')
print(f'The angle S is {S:.{sigfig}g}')
print(f'The angle T is {T:.{sigfig}g}') 