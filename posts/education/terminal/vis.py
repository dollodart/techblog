import matplotlib.pyplot as plt
import numpy as np

"""
Visualizes an arbitrary sequence of steps and
spikes which would define an input.
"""
np.random.seed(21301900)
y = np.zeros(100)
h = 0
hstep = 0.01
for _ in range(3):
    i1 = np.random.randint(0, 100)
    i2 = np.random.randint(0, 100)
    i3 = np.random.randint(0, 100)
    if i1 > i2:
        i1, i2 = i2, i1
    y2 = y.copy()
    y2[i1:i2] = 1
    y3 = y.copy()
    y3[i3] = 1
    h += hstep
    plt.plot(y2 + h, '-')
    h += hstep
    plt.plot(y3 + h, '-')

plt.xlabel('Time (arb. units)')
plt.ylabel('On/Off')

plt.xticks([])
plt.yticks([0,1],['Off','On'])
plt.savefig('arbitrary-keyseq.png')
plt.show()
