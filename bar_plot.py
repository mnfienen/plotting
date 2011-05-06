import numpy as np
import matplotlib.pylab as plt

indat = np.genfromtxt('infiltration.dat',dtype = None,names=True)
indat['Standard_Method'][indat['Standard_Method']==-9999] = np.nan
indat['Double_Ring'][indat['Double_Ring']==-9999] = np.nan


plt.close('all')

fig,(ax,ax2) = plt.subplots(2, 1, sharex=True)

width = 0.5
inds = np.arange(len(indat['Standard_Method']))
ax2.bar(inds,indat['Standard_Method'],width,color='red')
ax2.bar(inds+width,indat['Double_Ring'],width,color='blue')
plt.legend(['Standard Method','Double Ring'])
ax.bar(inds,indat['Standard_Method'],width,color='red')
ax.bar(inds+width,indat['Double_Ring'],width,color='blue')
ax.xaxis.tick_bottom()

ax2.set_ylim(-1,20)
ax.set_ylim(40,60)
ax2.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.xticks(inds)
xtickNames = ax2.set_xticklabels(indat['land_use'])
plt.setp(xtickNames, rotation=25, fontsize=8)

ax.xaxis.set_visible(False)
plt.savefig('barchart.eps')

plt.show()