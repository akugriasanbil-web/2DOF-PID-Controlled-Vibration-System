import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp
c=2
m1=6
m2=3
k1=0.9
k2=3
k3=1
y0=([0,6,0,7,0])
t_span=(0,60,)
time_point=np.linspace(0,60,1000)
def system(t,y):
    x1,v1,x2,v2,i=y
    kp=20
    x_desired=10
    error=x_desired-x1
    didt = error
    kd=21
    ki=2
    f=kp*error+ki*i-kd*v1
    dx1dt=v1
    dx2dt=v2
    dv1dt=(-c*(v1-v2)-x1*(k1+k2)+k2*x2+f)/m1
    dv2dt=(-c*(v2-v1)-x2*(k2+k3)+k2*x1)/m2
    return [v1,dv1dt,v2,dv2dt,didt]
sol=solve_ivp(system,t_span,y0,t_eval=time_point)
print(sol)
x1=sol.y[0]
x2=sol.y[2]

print("Final x1 =", x1[-1])
print("Max x1 =", np.max(x1))

fig,axis=plt.subplots()
axis.set_xlim(-5,25)
axis.set_ylim(-5,25)
plt.xlabel("displacement")
plt.title("multi degree of freedom")

masses1,=plt.plot([],[],color="red",marker="o")
masses2,=plt.plot([],[],color="blue",marker="o")
spring1,=plt.plot([],[],color="black")
spring2,=plt.plot([],[],color="brown",linestyle="--")
spring3,=plt.plot([],[],color="green")

def plot(frames):
    position1=0+x1[frames]
    positon2=10+x2[frames]
    masses1.set_data([position1],[0])
    masses2.set_data([positon2],[0])
    spring1.set_data([-5,position1],[0,0])
    spring2.set_data([position1,positon2],[0,0])
    spring3.set_data([positon2, 20], [0, 0])
    return masses1,masses2,spring1,spring2
ani=FuncAnimation(fig,plot,frames=len(time_point),interval=26)
plt.grid()
plt.show()
