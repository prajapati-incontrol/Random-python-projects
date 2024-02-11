import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation

# setting up the time vector
t_end = 12 # s
dt = 0.02 # s
t = np.arange(0,t_end+dt,dt)

# setting up the altitude vector: Earth
y_i = 100 # m
g_e = -9.8 # m/s^2
y_fall = y_i + 0.5*g_e*t**2 # m
y_fall = y_fall *( y_fall >= 0)
y_dot = g_e*t # m/s

# setting up the altitude vector : Mars
g_m = -3.7
y_mfall = y_i + 0.5*g_m*t**2 # m
y_mfall = y_mfall * (y_mfall >= 0)
y_mdot = g_m*t

# setting up the altitude vector : Moon
g_mu = -1.6
y_mufall = y_i + 0.5*g_mu*t**2 # m
y_mufall = y_mufall * (y_mufall >= 0)
y_mudot = g_mu*t

# defining the circle
r_circ = 5 # m

# defining circle class
def get_circle(radius):
    ang = np.arange(0,361,1)
    x_circ = r_circ*np.cos(ang*np.pi/180)
    y_circ = r_circ*np.sin(ang*np.pi/180)
    return x_circ, y_circ

x_circ, y_circ = get_circle(r_circ)

# to suppress scientific notations in using print()
# np.set_printoptions(suppress = True)
# print(x_circ, y_circ)

########################################## BEGIN ANIMATION #######################################################
frames_amount = len(t)
w_ratio = 1.2
y_f= -10 # [m]
dy= 10 # [m]



def update_plot(num):
    if y_fall[num] >= r_circ:
        spehere_Earth.set_data(x_circ, y_circ + y_fall[num])
        l_e.set_data(t[0:num],y_fall[0:num])
        v_e.set_data(t[0:num], y_dot[0:num])
        
    
    if y_mfall[num] >= r_circ:
        ele_mars.set_data(x_circ, y_circ + y_mfall[num])
        l_m.set_data(t[0:num], y_mfall[0:num])
        v_m.set_data(t[0:num], y_mdot[0:num])
        
    if y_mufall[num] >= r_circ:
        ele_moon.set_data(x_circ, y_circ + y_mufall[num])
        l_mu.set_data(t[0:num], y_mufall[0:num])
        v_mu.set_data(t[0:num], y_mudot[0:num])
        
    # whenever returning 1 object, write "object,""
    return spehere_Earth, l_e, ele_mars, ele_moon, l_m, l_mu, v_mu, \
        v_m, v_e



# Figure Object
fig = plt.figure(figsize = (16,9), dpi = 120, facecolor=(0.9,0.9,0.9))
gs = gridspec.GridSpec(3,4)

# Earth Subplot objects
ax0 = fig.add_subplot(gs[:,0], facecolor = (1,1,1))
spehere_Earth,=ax0.plot([],[],'k',linewidth=3)
land_Earth = ax0.plot([-r_circ*w_ratio,r_circ*w_ratio],[-6,-6],linewidth = 37)
plt.xlim(-r_circ*w_ratio, r_circ*w_ratio)
plt.ylim(y_f,y_i+dy)
plt.title("On Earth")
plt.xticks(np.arange(-r_circ, r_circ+1, r_circ))
plt.yticks(np.arange(y_f,y_i+2*dy,dy))

# Mars subplot objects
ax1 = fig.add_subplot(gs[:,1], facecolor = (1,1,1))
ele_mars, =  ax1.plot([],[],'k',linewidth = 3)
land_mars = ax1.plot([-r_circ*w_ratio,r_circ*w_ratio],[-6,-6],color = 'orange',linewidth = 37)
plt.xlim(-r_circ*w_ratio, r_circ*w_ratio)
plt.ylim(y_f,y_i+dy)
plt.title("On Mars")
plt.xticks(np.arange(-r_circ, r_circ+1, r_circ))
plt.yticks(np.arange(y_f,y_i+2*dy,dy))

# Moon subplot objects
ax2 = fig.add_subplot(gs[:,2], facecolor = (1,1,1))
ele_moon, =  ax2.plot([],[],'k',linewidth = 3)
land_moon = ax2.plot([-r_circ*w_ratio,r_circ*w_ratio],[-6,-6], color = (0.9,0.9,0.9) ,linewidth = 37)
plt.xlim(-r_circ*w_ratio, r_circ*w_ratio)
plt.ylim(y_f,y_i+dy)
plt.title("On Moon")
plt.xticks(np.arange(-r_circ, r_circ+1, r_circ))
plt.yticks(np.arange(y_f,y_i+2*dy,dy))

# Create position function
ax3 = fig.add_subplot(gs[0,3], facecolor = (1,1,1))
l_e, = ax3.plot([],[],'',linewidth = 3)
l_m, = ax3.plot([],[],'orange',linewidth = 3)
l_mu, = ax3.plot([],[],'gray',linewidth = 3)
plt.xlim(0,t_end)
plt.ylim(0,y_i+10)
plt.title("Position")
plt.xlabel("Time (s)")
plt.ylabel("Altitude (m)")

# Create velocity function
ax4 = fig.add_subplot(gs[2,3], facecolor = (1,1,1))
v_e, = ax4.plot([],[],'',linewidth = 3)
v_m, = ax4.plot([],[],'orange', linewidth = 3)
v_mu, = ax4.plot([],[],'gray',linewidth = 3)
plt.xlim(0,t_end)
plt.ylim(y_dot[-1], 0)
plt.title("Velocity", size = 12)
plt.xlabel("Time (s)")
plt.ylabel("Altitude (m)")



anime = animation.FuncAnimation(fig, update_plot, frames = frames_amount, interval = 20, repeat = True, blit = True)
plt.show()
