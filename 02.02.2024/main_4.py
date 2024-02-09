import numpy as np
from matplotlib import pyplot as plt

index = np.arange(5)
Intel = [145, 120, 180, 150, 210]
Nvidia = [180, 140, 200, 170, 230]
AMD = [160, 130, 190, 160, 220]
bw = 0.3
plt.axis([0,5,0,300])
plt.title('FPS test in games', fontsize=20)
plt.bar(index, Intel, bw, color='b')
plt.bar(index+bw, Nvidia, bw, color='g')
plt.bar(index+2*bw, AMD, bw, color='r')
plt.xticks(index+1.5*bw,['Cyberpunk','RDR 2','CS 2','Doom','GTA 5'])
plt.show()
