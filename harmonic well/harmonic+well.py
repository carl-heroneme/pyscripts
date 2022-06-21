
# coding: utf-8

# In[ ]:


import numpy as np
import scipy as sp


# In[ ]:


#input parameters

#Kb in epsilon/degK
k = .0083472
#epsilon
E = 1
#degK
t = 100
#beta
B = 1/(k*t)
x1 = -1.14
x2 = 1.5
kforce = 1

def R(d,e):
    r = d - e
    return abs(r)

def pot(a,b,c):
    return 4*E*((3.405/a)**12-(3.405/a)**6)+0.5*kforce*b**2+0.5*kforce*c**2   

def prob(f,g):
    return 2.71828**(-B*(f-g))

n = int(input('Number of iterations: '))


# In[ ]:


from random import uniform
px1 = []
px2 = []
rl = []
el = []

for i in range(n):
    px1.append(x1)
    px2.append(x2)
    print('x1,x2: ' + str(x1) + ' ' + str(x2))
    
    r0 = R(x1, x2)
    rl.append(r0)
    print('R: ' + str(r0))
    
    e0 = pot(r0, x1, x2)
    el.append(e0)
    print('E: ' + str(e0))
    
    chooser = uniform(0,1)
    move = uniform(-0.5, 0.5)
    print('dx: ' + str(move))
    
    if chooser < 0.5:
        t1 = x1 + move
        rn = R(t1, x2)
        en = pot(rn, t1, x2)
        if en <= e0:
            x1 = t1
        elif prob(en, e0) > uniform(0,1):
            x1 = t1
           
    else:
        t2 = x2 + move
        rn = R(x1, t2)
        en = pot(rn, x1, t2)
        if en <= e0:
            x2 = t2
        elif prob(en, e0) > uniform(0,1):
            x2 = t2
#print(px1)
print('Average Pos x1:' + str(np.mean(px1)))
#print(px2)
print('Average Pos x2:' + str(np.mean(px2)))
#print(rl)
print('Average R: ' + str(np.mean(rl)))
#print(el)
print('Average E: ' + str(np.mean(el)))

