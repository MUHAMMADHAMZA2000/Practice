import math
x = math.sqrt(64)
print (x)

y = math.sqrt(125)
print (y)

import math
x = math.ceil(91.4)
y = math.floor(91.4)
print(x) 
print(y)

import datetime
x = datetime.datetime.now()
print  (x)

import datetime
x = datetime.datetime.now()
print (x.year)
print(x.strftime("%A"))

import datetime
x = datetime.datetime(2000,12,22)
print (x)

 # declary a function
def int ():
    print ("my name is hamza. i father name is fida muhammad. i am 23 years old. i qualification is DAE Elt. i have completed apprenticeship program as ASISTANT ENGINEER from K-ELECTRIC. ") 
int ()

def evenodd( x ) :     
 if ( 26  % 2  == 0 ) :
         print ("even")
 else:
             print("odd")
# driver code  
evenodd ( 2 )
evenodd ( 3 )



#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 100000)

plt.hist(x, 100)
plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()


#  default arguments
def myfun( x,y = 67 ):
    print("x: ", y )
    print("y: ", y )
# drive code 
myfun ( 18 )




x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)


a = 4
A = "Sally"

print(a)
print(A)


fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)



thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)




import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])


import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))








