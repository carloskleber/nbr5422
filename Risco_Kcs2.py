# -*- coding: utf-8 -*-
"""
Variante da rotina Risco_Kcs, plotando graficos separados

Created on Thu May  2 13:28:06 2019

@author: arthurlr, carloska
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
 
    ris = sob*(1-(1-sup)**Ngaps)
    return(sum(ris) * du)

K = np.arange(1,1.80,0.01)            # coeficiente estatístico: Kcs = U90/V2
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

plt.figure()
for j in range(len(N)):
    plt.plot(K,R[:,j,0,0],ls[j])
plt.yscale('log')
plt.xticks(np.arange(1.,1.60,0.05))
plt.xticks(np.arange(1.,1.60,0.01), minor=True)
plt.axis([1.,1.25,1e-6,1e-1])
plt.grid(which='major', color='#AAAAAA')
plt.grid(which='minor', color='#DDDDDD')
plt.xlabel(r'$K_{CS}=U_{90}/V_2$, $C_{VSfl} = $'+str(int(100*DP_S[0]))+'%')
plt.ylabel(r'Risco de Falha, $C_{Vfl} = $'+str(int(100*DP[0]))+'%')
plt.legend(N)
plt.savefig('plotNBR00')

plt.figure()
for j in range(len(N)):
    plt.plot(K,R[:,j,0,1],ls[j])
plt.yscale('log')
plt.xticks(np.arange(1.,1.60,0.05))
plt.xticks(np.arange(1.,1.60,0.01), minor=True)
plt.axis([1.,1.35,1e-6,1e-1])
plt.grid(which='major', color='#AAAAAA')
plt.grid(which='minor', color='#DDDDDD')
plt.xlabel(r'$K_{CS}=U_{90}/V_2$, $C_{VSfl} = $'+str(int(100*DP_S[1]))+'%')
plt.ylabel(r'Risco de Falha, $C_{Vfl} = $'+str(int(100*DP[0]))+'%')
plt.legend(N)
plt.savefig('plotNBR01')

plt.figure()
for j in range(len(N)):
    plt.plot(K,R[:,j,0,2],ls[j])
plt.yscale('log')
plt.xticks(np.arange(1.,1.60,0.05))
plt.xticks(np.arange(1.,1.60,0.01), minor=True)
plt.axis([1.,1.4,1e-6,1e-1])
plt.grid(which='major', color='#AAAAAA')
plt.grid(which='minor', color='#DDDDDD')
plt.xlabel(r'$K_{CS}=U_{90}/V_2$, $C_{VSfl} = $'+str(int(100*DP_S[2]))+'%')
plt.ylabel(r'Risco de Falha, $C_{Vfl} = $'+str(int(100*DP[0]))+'%')
plt.legend(N)
plt.savefig('plotNBR02')

plt.figure()
for j in range(len(N)):
    plt.plot(K,R[:,j,1,0],ls[j])
plt.yscale('log')
plt.xticks(np.arange(1.,1.60,0.05))
plt.xticks(np.arange(1.,1.60,0.01), minor=True)
plt.axis([1.,1.4,1e-6,1e-1])
plt.grid(which='major', color='#AAAAAA')
plt.grid(which='minor', color='#DDDDDD')
plt.xlabel(r'$K_{CS}=U_{90}/V_2$, $C_{VSfl} = $'+str(int(100*DP_S[0]))+'%')
plt.ylabel(r'Risco de Falha, $C_{Vfl} = $'+str(int(100*DP[1]))+'%')
plt.legend(N)
plt.savefig('plotNBR10')

plt.figure()
for j in range(len(N)):
    plt.plot(K,R[:,j,1,1],ls[j])
plt.yscale('log')
plt.xticks(np.arange(1.,1.60,0.05))
plt.xticks(np.arange(1.,1.60,0.01), minor=True)
plt.axis([1.,1.5,1e-6,1e-1])
plt.grid(which='major', color='#AAAAAA')
plt.grid(which='minor', color='#DDDDDD')
plt.xlabel(r'$K_{CS}=U_{90}/V_2$, $C_{VSfl} = $'+str(int(100*DP_S[1]))+'%')
plt.ylabel(r'Risco de Falha, $C_{Vfl} = $'+str(int(100*DP[1]))+'%')
plt.legend(N)
plt.savefig('plotNBR11')

plt.figure()
for j in range(len(N)):
    plt.plot(K,R[:,j,1,2],ls[j])
plt.yscale('log')
plt.xticks(np.arange(1.,1.7,0.05))
plt.xticks(np.arange(1.,1.60,0.01), minor=True)
plt.axis([1.,1.60,1e-6,1e-1])
plt.grid(which='major', color='#AAAAAA')
plt.grid(which='minor', color='#DDDDDD')
plt.xlabel(r'$K_{CS}=U_{90}/V_2$, $C_{VSfl} = $'+str(int(100*DP_S[2]))+'%')
plt.ylabel(r'Risco de Falha, $C_{Vfl} = $'+str(int(100*DP[1]))+'%')
plt.legend(N)
plt.savefig('plotNBR12')
