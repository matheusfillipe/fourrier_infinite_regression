from reg import *
import random
def func(x):
    #return x**3+2*x+2
    return x**2

X=[]
Y=[]
for i in range(0,5):
    x=random.random()+i-.0001
    X.append(x)
    Y.append(func(x))

formula(X,Y)
#print(X)




