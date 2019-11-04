import math
import random
name='11';a=-10;f=8;c=3;b=8.6901;arr=[1,2,3,4,5,6,7,89,77]
#multilining
s=a+b+\
+c\
+f
#print(s)

#power of function
'''r=a**c
print(r)'''

#type conversion
'''p=float(f)
g=int(b)
namint=int(name,2)#binary to decimal
intcomp=complex(6)#int to complex number
intbool=bool(-90)
print(intbool)
print(namint)
print(intcomp)
print(p)
print(g)'''

#inbuilt functions
'''absa=abs(a)
#print(absa)
power=pow(a,2)
#print(power)
mini=min(arr)
#print(mini)
maxa=max(arr)
#print(maxa)
div=divmod(500,3)
#print(div)
binaru=bin(15)
octu=oct(10)
hexu=hex(15)
#print('binary is ',binaru,'\noctal is : ',octu,'\nhexadecimal is :',hexu)
roundoff=round(b,2)
print(roundoff)'''

#LIBRARY FUNCTIONS

#  A. //simple maths
#print(math.pi,'\n',math.e)
rootf=math.sqrt(f)
#print(rootf)
factf=math.factorial(f)
#print(factf)
fabsf=math.fabs(b)
#print(fabsf)
natlog=math.log(10)#natural
#print(natlog)
logbten=math.log10(10)#logbase10
#print(logbten)
etopow=math.exp(3)#e raise to the power
#print(etopow)
trunc=math.trunc(b)
#print(trunc)
ceil=math.ceil(b)
floor=math.floor(b)
#print('ceil smallest int >=: ',ceil,'\nfloor greatest integer <= ',floor)
modf=math.modf(b)
#print(modf)


#B.  trigonometric math

deg=math.degrees(6)
#print(deg)
rad=math.radians(90)
#print(rad)
angle=1.5707963267948966
tan=math.tan(angle);sin=math.sin(angle);cos=math.cos(angle)
#print('tan(90):',tan,'\nsin(90):',sin,'\ncos(90):',cos)
#cosh,sinh,tanh,acos,asin,atan are also available //hypot(x,y)=sqrt(x*x+y*y)
#print(random.random())#between 0 and 1
#print(random.randint(2,10))#between 2 and 10

random.seed(13)
#print(random.randint(0,100))
random.seed(12)
#print(random.randint(0,100))
random.seed(12)
#print(random.randint(0,100))
