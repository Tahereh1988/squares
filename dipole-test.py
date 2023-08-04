#!/usr/bin/python3

from dipole import dipole

# magnetic dipole moment in A*m**2
mx=0
my=0
mz=1

# location of the dipole
x0=0
y0=0
z0=0

# initialize the dipole with this magnetic moment and location
d=dipole(x0,y0,z0,mx,my,mz)

# what's the field produced by this dipole at some location?
x=1
y=0
z=0

print(d.bx(x,y,z),d.by(x,y,z),d.bz(x,y,z),d.b(x,y,z))

d.random(1.2)

xd=[]
yd=[]
zd=[]
mx=[]
my=[]
mz=[]
for i in range(10000):
    d.random(1.2)
    xd.append(d.xd)
    yd.append(d.yd)
    zd.append(d.zd)
    mx.append(d.mx)
    my.append(d.my)
    mz.append(d.mz)
    print(d.xd,d.yd,d.zd,d.bx(x,y,z),d.by(x,y,z),d.bz(x,y,z))

import matplotlib.pyplot as plt

fig=plt.figure()
ax=fig.add_subplot(1,2,1,projection='3d')
ax2=fig.add_subplot(1,2,2,projection='3d')
ax.scatter(xd,yd,zd,marker='.')
ax2.scatter(mx,my,mz,marker='.')
plt.show()

d.set(1.2,0,0,mx[-1],my[-1],mz[-1])
print('Final d')
print(d.xd,d.yd,d.zd,d.bx(x,y,z),d.by(x,y,z),d.bz(x,y,z))
    
d.set(-1.2,0,0,mx[-1],my[-1],mz[-1])
print('Final d')
print(d.xd,d.yd,d.zd,d.bx(x,y,z),d.by(x,y,z),d.bz(x,y,z))
    
