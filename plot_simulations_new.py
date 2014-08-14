# -*- coding: utf-8 -*-
"""
Created on Sun Aug  3 17:19:11 2014

@author: anmol
"""

import matplotlib.pyplot as plt
import cPickle as pickle
import numpy as np
import math
data_riskaversion_2shocks = pickle.load( open( 'dataSimulation_ra_2shocks.dat', "rb" ) )    
data_ql_2shocks = pickle.load( open( 'dataSimulation_ql.dat', "rb" ) )    



xHist_riskaversion_2shocks,_,_,tauHist_riskaversion_2shocks,bHist_riskaversion_2shocks,para_ra_2shocks=data_riskaversion_2shocks
xHist_ql_2shocks,_,_,tauHist_ql_2shocks,bHist_ql_2shocks,para_ql_2shocks=data_ql_2shocks

t=1
T=3000
freq=3000
plot_seq=np.array(map(math.modf,(np.linspace(t,T,freq))),dtype='int')[:,1]


f,(ax1,ax2,ax3) =plt.subplots(3,1,sharex='col')

lines_taxes=ax1.plot(np.vstack((tauHist_ql_2shocks[plot_seq],tauHist_riskaversion_2shocks[plot_seq])).T)
lines_debt=ax2.plot(np.vstack((bHist_ql_2shocks[plot_seq],bHist_riskaversion_2shocks[plot_seq])).T)
lines_x=ax3.plot(np.vstack((xHist_ql_2shocks[plot_seq],xHist_riskaversion_2shocks[plot_seq])).T)

    
plt.setp(lines_taxes[1],color='k',linewidth=2)
plt.setp(lines_taxes[0],color='k',linewidth=2,linestyle='--')


plt.setp(lines_debt[1],color='k',linewidth=2)
plt.setp(lines_debt[0],color='k',linewidth=2,linestyle='--')

plt.setp(lines_x[1],color='k',linewidth=2)
plt.setp(lines_x[0],color='k',linewidth=2,linestyle='--')


ax3.legend(['QL','RA 2shocks','x'],loc='upper center', bbox_to_anchor=(0.5, -0.2),
          fancybox=True, shadow=True, ncol=3)

    
ax1.set_title(r'tax rate')
ax2.set_title(r'debt')
ax3.set_title(r'x')



plt.xlabel('t')    
plt.savefig('policy_long_sample.png',dpi=300)
   

