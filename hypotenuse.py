import math

#initial arguments 
a =3 # first angle
b =4 # second angle

#two additional arguments 
c=5 # third angle
d=6 # forth angle

#two additional arguments 
e= 7 # fifth angle
f= 8 # sixth angle

def hypotenuse(a,b):
# I used Pythagoras Therom formula to solve
    hypo_lengtha=math.sqrt(a**2+b**2)
    print(hypo_lengtha)
    hypo_lengthb=math.sqrt (c**2+d**2)
    print(hypo_lengthb)
    hypo_lengthc=math.sqrt(e**2+f**2)
    print(hypo_lengthc)
result=hypotenuse(a,b)