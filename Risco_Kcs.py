# -*- coding: utf-8 -*-
"""
Created on Thu May  2 13:28:06 2019

@author: arthurlr
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def RISCO (Kcs, Ngaps, sig, sig_S):
    
    #SOBRETENSÕES:
    V50 = 1                   #valor médio (pu)
    V2  = V50*(1+2.05*sig_S)  #máxima estatística 2% (pu)
    
    #SUPORTABILIDADE:
    U90 = Kcs*V2            #tensão com 90% de probabilidade de descarga (pu)
    U50 = U90/(1-1.28*sig)  #tensão com 50% de probabilidade de descarga (pu)
    
    #VETORES:
    umin = V50*(1-5*sig_S)
    umax = U50*(1+5*sigma)
    du = 0.001
    u = np.arange(umin, umax, du)
    sob = norm.pdf(u,V50,V50*sig_S)
    sup = norm.cdf(u,U50,U50*sig)
    
#    #PLOT CURVAS DE PROBABILIDADE:
#    plt.figure(1)
#    plt.plot(u,sob)
#    plt.plot(u,sup)
    
    ris = sob*(1-(1-sup)**Ngaps)
    return(sum(ris) * du)



K = np.arange(1,1.70,0.01)            # coeficiente estatístico: Kcs = U90/V2
DP   = [0.03, 0.06]                   # desvio-padrão das sobretensões   (pu do valor médio)
DP_S = [0.05, 0.10, 0.15]             # desvio-padrão da suportabilidade (pu do valor médio)
N  = [1,10,20,50,100,200,500,1000]    # número de gaps em paralelo
ls = ['-',':','-.','--','-',':','-.','--']

R = np.zeros((len(K), len(N), len(DP), len(DP_S)))
for i,Kcs in enumerate(K):
    for j,Ngaps in enumerate(N):
        for m,sigma in enumerate(DP):
            for n,sigma_S in enumerate(DP_S):
                R[i,j,m,n] = RISCO(Kcs, Ngaps, sigma, sigma_S)


#eixo y de 10-3 a 10-1:
plots, axes = plt.subplots(nrows=len(DP), ncols=len(DP_S), figsize=(10,10))
plots.gca().set_prop_cycle(None)
for m in range(len(DP)):
    for n in range(len(DP_S)):
        axes[m,n].set_xticks(np.arange(1.05,1.50,0.05))
axes[0,0].set_xlim(1.06,1.22)
axes[0,1].set_xlim(1.12,1.32)
axes[0,2].set_xlim(1.16,1.40)
axes[1,0].set_xlim(1.10,1.32)
axes[1,1].set_xlim(1.12,1.40)
axes[1,2].set_xlim(1.16,1.50)
for m in range(len(DP)):
    axes[m,0].set_ylabel(r'Risco de Falha, $\sigma_{fl} = $'+str(100*DP[m])+'%')
    for n in range(len(DP_S)):
        axes[m,n].yaxis.grid(True, which='major', linewidth=2)
        axes[m,n].xaxis.grid(True, which='major', linestyle='-', linewidth=2)
        axes[m,n].xaxis.grid(True, which='minor', linestyle='--')
        axes[m,n].set_xticks(np.arange(axes[m,n].get_xlim()[0],axes[m,n].get_xlim()[1],0.01), minor=True)
        # axes[m,n].set_xlim([K[0],K[-1]])
        axes[m,n].set_ylim([0.001,.1])
        axes[m,n].set_xlabel(r'$K_{CS}=U_{90}/V_2$, $\sigma_{Sfl} = $'+str(100*DP_S[n])+'%')
        for j in range(len(N)):
            axes[m,n].semilogy(K,R[:,j,m,n],ls[j])
        axes[m,n].legend(N)
        
    

#eixo y de 10-5 a 10-1:
plots2, axes2 = plt.subplots(nrows=len(DP), ncols=len(DP_S), figsize=(10,10))
plots2.gca().set_prop_cycle(None)
for m in range(len(DP)):
    for n in range(len(DP_S)):
        axes2[m,n].set_xticks(np.arange(1.05,1.70,0.05))
axes2[0,0].set_xlim(1.04,1.30)
axes2[0,1].set_xlim(1.12,1.40)
axes2[0,2].set_xlim(1.14,1.52)
axes2[1,0].set_xlim(1.10,1.40)
axes2[1,1].set_xlim(1.12,1.50)
axes2[1,2].set_xlim(1.16,1.62)
for m in range(len(DP)):
    axes2[m,0].set_ylabel(r'Risco de Falha, $\sigma_{fl} = $'+str(100*DP[m])+'%')
    for n in range(len(DP_S)):
        axes2[m,n].yaxis.grid(True, which='major', linewidth=2)
        axes2[m,n].xaxis.grid(True, which='major', linestyle='-', linewidth=2)
        axes2[m,n].xaxis.grid(True, which='minor', linestyle='--')
        axes2[m,n].set_xticks(np.arange(axes2[m,n].get_xlim()[0],axes2[m,n].get_xlim()[1],0.01), minor=True)
        # axes2[m,n].set_xlim([K[0],K[-1]])
        axes2[m,n].set_ylim([0.00001,.1])
        axes2[m,n].set_xlabel(r'$K_{CS}=U_{90}/V_2$, $\sigma_{Sfl} = $'+str(100*DP_S[n])+'%')
        for j in range(len(N)):
            axes2[m,n].semilogy(K,R[:,j,m,n],ls[j])
        axes2[m,n].legend(N)



#eixo y de 10-4 a 10-1:
plots3, axes3 = plt.subplots(nrows=len(DP), ncols=len(DP_S), figsize=(10,10))
plots3.gca().set_prop_cycle(None)
for m in range(len(DP)):
    for n in range(len(DP_S)):
        axes3[m,n].set_xticks(np.arange(1.05,1.70,0.05))
axes3[0,0].set_xlim(1.04,1.30)
axes3[0,1].set_xlim(1.12,1.40)
axes3[0,2].set_xlim(1.14,1.52)
axes3[1,0].set_xlim(1.10,1.40)
axes3[1,1].set_xlim(1.12,1.50)
axes3[1,2].set_xlim(1.16,1.62)
for m in range(len(DP)):
    axes3[m,0].set_ylabel(r'Risco de Falha, $\sigma_{fl} = $'+str(100*DP[m])+'%')
    for n in range(len(DP_S)):
        axes3[m,n].yaxis.grid(True, which='major', linewidth=2)
        axes3[m,n].xaxis.grid(True, which='major', linestyle='-', linewidth=2)
        axes3[m,n].xaxis.grid(True, which='minor', linestyle='--')
        axes3[m,n].set_xticks(np.arange(axes3[m,n].get_xlim()[0],axes3[m,n].get_xlim()[1],0.01), minor=True)
        # axes3[m,n].set_xlim([K[0],K[-1]])
        axes3[m,n].set_ylim([0.0001,.1])
        axes3[m,n].set_xlabel(r'$K_{CS}=U_{90}/V_2$, $\sigma_{Sfl} = $'+str(100*DP_S[n])+'%')
        for j in range(len(N)):
            axes3[m,n].semilogy(K,R[:,j,m,n],ls[j])
        axes3[m,n].legend(N)


#eixo y de 10-6 a 10-1:
plots4, axes4 = plt.subplots(nrows=len(DP), ncols=len(DP_S), figsize=(20,15))
plots4.gca().set_prop_cycle(None)
for m in range(len(DP)):
    for n in range(len(DP_S)):
        axes4[m,n].set_xticks(np.arange(1.05,1.70,0.05))
axes4[0,0].set_xlim(1.06,1.30)
axes4[0,1].set_xlim(1.12,1.48)
axes4[0,2].set_xlim(1.14,1.58)
axes4[1,0].set_xlim(1.10,1.52)
axes4[1,1].set_xlim(1.12,1.58)
axes4[1,2].set_xlim(1.16,1.72)
for m in range(len(DP)):
    axes4[m,0].set_ylabel(r'Risco de Falha, $\sigma_{fl} = $'+str(100*DP[m])+'%')
    for n in range(len(DP_S)):
        axes4[m,n].yaxis.grid(True, which='major', linewidth=2)
        axes4[m,n].xaxis.grid(True, which='major', linestyle='-', linewidth=2)
        axes4[m,n].xaxis.grid(True, which='minor', linestyle='--')
        axes4[m,n].set_xticks(np.arange(axes4[m,n].get_xlim()[0],axes4[m,n].get_xlim()[1],0.01), minor=True)
        # axes4[m,n].set_xlim([K[0],K[-1]])
        axes4[m,n].set_ylim([0.000001,0.1])
        axes4[m,n].set_xlabel(r'$K_{CS}=U_{90}/V_2$, $\sigma_{Sfl} = $'+str(100*DP_S[n])+'%')
        for j in range(len(N)):
            axes4[m,n].semilogy(K,R[:,j,m,n],ls[j])
        axes4[m,n].legend(N)
plots4.savefig('plotNBR')


#eixo y de 10-6 a 10-4:
plots5, axes5 = plt.subplots(nrows=len(DP), ncols=len(DP_S), figsize=(10,10))
plots5.gca().set_prop_cycle(None)
for m in range(len(DP)):
    for n in range(len(DP_S)):
        axes5[m,n].set_xticks(np.arange(1.05,1.70,0.05))
axes5[0,0].set_xlim(1.14,1.30)
axes5[0,1].set_xlim(1.22,1.48)
axes5[0,2].set_xlim(1.24,1.58)
axes5[1,0].set_xlim(1.22,1.52)
axes5[1,1].set_xlim(1.26,1.58)
axes5[1,2].set_xlim(1.36,1.72)
for m in range(len(DP)):
    axes5[m,0].set_ylabel(r'Risco de Falha, $\sigma_{fl} = $'+str(100*DP[m])+'%')
    for n in range(len(DP_S)):
        axes5[m,n].yaxis.grid(True, which='major', linewidth=2)
        axes5[m,n].xaxis.grid(True, which='major', linestyle='-', linewidth=2)
        axes5[m,n].xaxis.grid(True, which='minor', linestyle='--')
        axes5[m,n].set_xticks(np.arange(axes5[m,n].get_xlim()[0],axes5[m,n].get_xlim()[1],0.01), minor=True)
        # axes5[m,n].set_xlim([K[0],K[-1]])
        axes5[m,n].set_ylim([0.000001,0.0001])
        axes5[m,n].set_xlabel(r'$K_{CS}=U_{90}/V_2$, $\sigma_{Sfl} = $'+str(100*DP_S[n])+'%')
        for j in range(len(N)):
            axes5[m,n].semilogy(K,R[:,j,m,n],ls[j])
        axes5[m,n].legend(N)