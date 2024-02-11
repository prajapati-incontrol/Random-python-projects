# Model a sample on a sine wave

import matplotlib.pyplot as plt 
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np


plt.style.use('dark_background')

#### SETUP ####
t = np.arange(5)

x = np.linspace(0, 20, 201)



#### ANIMATION ####
frames_amount = int(len(t))

fig = plt.figure(figsize = (4,3), dpi = 120, facecolor = (0.8,0.8,0.8))

# we need just 1 plot
gs = gridspec.GridSpec(1,1)

#### Wave animation ####
ax0 = fig.add_subplot(gs[0,:], facecolor = (0.9,0.9,0.9))
plt.grid(True)
plt.xlim(0,10)
plt.ylim(-2,2)

# initialize 
sine_wave = ax0.plot([],[],'o', linewidth = 1)[0]
sample = ax0.plot([],[],'rx',linewidth = 0.5)[0]

def update_plot(num):
    y = np.sin(x + t[num])
    sine_wave.set_data(x, y)
    sample.set_data(x[10], y[10])
    return sine_wave, sample 

update_plot
anime = animation.FuncAnimation(fig, update_plot, frames = frames_amount, interval = 200, 
                                repeat = True, blit = False)
plt.show()




