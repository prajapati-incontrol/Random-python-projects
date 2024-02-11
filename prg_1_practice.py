import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

############################ SETUP DATA ################################
t0 = 0
dt = 0.005
tend = 2
t = np.arange(t0,tend+dt,dt)
a = 800

# X array 
x = 800*t # linear distribution

# Y array 
altitude = 2 #[km]
y = altitude*np.ones(len(t))


####################### ANIMATION ############################
frames_amount = int(len(t)) # total 401 frames

# at every interval of 20 frames, if you want to have a dot do this:
# we want dots to appear as this matrix: 
# dots = [0 0 ...19 zeros...x[20] x[20] x[20] ... 19 x[20]s... x[40]...x[60]...]
dot = np.zeros(frames_amount)
n = 20 # at 20 intervals
for i in range(0,frames_amount):
    if i == n:
        dot[i] = x[i]
        n += 20
    else:
        dot[i] = x[n-20]

# defining the figure dpi = dots per inch
fig = plt.figure(figsize = (16,9), dpi = 120, facecolor = (0.8, 0.8, 0.8))

# we will need 2 X 2 subplots
gs = gridspec.GridSpec(2,2)

######### Flight Trajectory #################

# step 1 declare the subplot: 1st row & all cols and obtain the figure handle
ax0 = fig.add_subplot(gs[0,:], facecolor = (0.9,0.9,0.9))

# initialize the plane trajectory line
plane_trajectory = ax0.plot([],[],'r:o',linewidth = 1)[0]
ver_line1 = ax0.plot([],[],'k:o',linewidth = 1)[0]

# plot the skyscrapers
scraper_1 = ax0.plot([100,100],[0,1.0],'k',linewidth = 7)
scraper_2  = ax0.plot([300, 300],[0, 1.0],'k',linewidth = 7)
scraper_3 = ax0.plot([700,700],[0,0.7],'k',linewidth = 7)
scraper_4 = ax0.plot([900,900],[0,0.9],'k',linewidth = 20)
scraper_5 = ax0.plot([1300,1300],[0,1.0],'k',linewidth = 20)

# declaring the plot handles of the aircraft
fuselage = ax0.plot([],[],'k',linewidth = 5)[0]
wing_1 = ax0.plot([],[],'k',linewidth = 3)[0]
wing_2 = ax0.plot([],[],'k',linewidth = 3)[0]
tail_1 = ax0.plot([],[],'k',linewidth = 2)[0]
tail_2 = ax0.plot([],[],'k',linewidth = 2)[0]

# make the indicator boxes 
# box_object = dict(boxstyle, bgcolor, bordercolor, borderlinewidth)
box_obj = dict(boxstyle = 'square', fc = (0.9,0.9,0.9), ec = 'g', lw = 1)
stopwatch0 = ax0.text(1400, 0.25, ' ', size = 15, color = 'g', bbox = box_obj)

box_obj2 = dict(boxstyle = 'square', fc = (0.9,0.9,0.9), ec = 'r', lw = 1)
distwatch = ax0.text(1400, 0.85, ' ', size = 15, color = 'r', bbox = box_obj2)

plt.xlim(x[0], x[-1])
plt.ylim(0, y[0]+1)
plt.xticks(np.arange(0,(x[-1] + 1), x[-1]/4), size = 10)
plt.yticks(np.arange(0,y[-1]+2,y[-1]/y[-1]), size = 10)

plt.xlabel('x-distance [km]', fontsize = 10)
plt.ylabel('y-distance [km]', fontsize = 10)
plt.title('Airplance Trajecory', fontsize = 12)
plt.grid(True)

##################################### SUBPLOT 2 ###########################
ax2 = fig.add_subplot(gs[1,0], facecolor = [0.9,0.9,0.9])

# declare the line objects
x_dist = ax2.plot([],[],'-b',linewidth = 3, label = 'X = 800*t')[0]
hor_line = ax2.plot([],[],'r:o',linewidth = 1)[0]
ver_line = ax2.plot([],[],'g:o', linewidth = 1)[0]

plt.xlim(t[0],t[-1])
plt.ylim(x[0],x[-1])
plt.xticks(np.arange(t[0], t[-1]+dt, t[-1]/4), size = 10)
plt.yticks(np.arange(x[0], x[-1] + 1, x[-1]/4), size = 10)
plt.xlabel('Time [hrs]', fontsize = 10)
plt.ylabel('Range[km]', fontsize = 10)
plt.title('Range vs Time', fontsize = 10)
plt.grid(True)
plt.legend(loc = 'upper left', fontsize = 'large')

######################################## SUBPLOT 3 ##########################
ax3 = fig.add_subplot(gs[1,1], facecolor = [0.9,0.9,0.9])

# declaring the line objects 
spline, = ax3.plot([], [], '-b',linewidth = 3, label = 'Function \u0394X/\u0394t')
ver3, = ax3.plot([],[],'k:o', linewidth = 1)
div_line, = ax3.plot([0.1,0.3],[1770,1770],'k',linewidth = 1)
numerator = ax3.text(0.1, 1900, ' ', size = 15, color = 'k')
denominator = ax3.text(0.1, 1400, ' ', size = 15, color = 'k')
ans = ax3.text(0.36, 1750, ' ', size = 15, color = 'k')


plt.xlim(t[0], t[-1])
plt.ylim(0, 800*2)
plt.xticks(np.arange(t[0], t[-1]+dt, t[-1]/4), size = 10)
plt.yticks(np.arange(0, 800*2 + 1, 800*2/4), size = 10)
plt.xlabel('Time[hrs]', fontsize = 10)
plt.ylabel('Speed [km/hr]', fontsize = 10)
plt.title('Speed vs Time', fontsize = 10)
plt.grid(True)
plt.legend(loc = 'upper left', fontsize = 'large')



############################ ANIMATION CORE ###########################
def update_plot(num):
    ################## For Subplot 1 ####################
    print(num)
    plane_trajectory.set_data(dot[0:num], y[0:num])
    fuselage.set_data([x[num]-40, x[num]+20], [y[num], y[num]])
    wing_1.set_data([x[num]-20,x[num]],[y[num]+0.3,y[num]])
    wing_2.set_data([x[num]-20,x[num]],[y[num]-0.3,y[num]])
    tail_1.set_data([x[num]-45,x[num]-40],[y[num]-0.1,y[num]])
    tail_2.set_data([x[num]-45,x[num]-40],[y[num]+0.1,y[num]])
    ver_line1.set_data([x[num],x[num]],[0,y[num]])
    
    stopwatch0.set_text(str(round(t[num],1)) + 'hrs')
    distwatch.set_text(str(int(x[num])) + 'km')
    
    ################# For subplot 2 ########################
    x_dist.set_data(t[0:num+1],x[0:num+1])
    hor_line.set_data([t[0],t[num]],[x[num], x[num]])
    ver_line.set_data([t[num],t[num]], [x[0], x[num]])
    
    ################# For subplot 3 ########################
    spline.set_data(t[0:num], 800)
    ver3.set_data([t[num],t[num]], [0, 800])
    if num != 0:
        numerator.set_text(str(int(x[num])))
        denominator.set_text(str(round(t[num],1)))
        ans.set_text(' = ' + str(int(x[num]/t[num])) + 'km/hr')        
    return plane_trajectory, fuselage, wing_1, wing_2, tail_1, tail_2,\
        ver_line1, stopwatch0, distwatch, x_dist, hor_line, ver_line, \
            spline, ver3, numerator, denominator, ans

anime = animation.FuncAnimation(fig, update_plot, frames = frames_amount, 
                                interval = 20, repeat = True, blit = True)

plt.show()