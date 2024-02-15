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

plt.figure(figsize=[8,6])
for j in range(len(N)):
    plt.plot(R[:,j,0,0],K,ls[j])
plt.title(r'$C_{VSfl} = $'+str(int(100*DP_S[0]))+r'%, $C_{Vfl} = $'+str(int(100*DP[0]))+'%')
plt.xscale('log')
plt.yticks(np.arange(1.,1.60,0.05))
plt.yticks(np.arange(1.,1.60,0.01), minor=True)
plt.axis([1e-6,1e-1,1.,1.25])
plt.grid(which='major', color='#AAAAAA')
plt.grid(which='minor', color='#DDDDDD')
plt.ylabel(r'$K_{CS}=U_{90}/V_2$')
plt.xlabel(r'Risco de Falha')
plt.legend(N)
plt.savefig('figura c1 1')

plt.figure(figsize=[8,6])
for j in range(len(N)):
    plt.plot(R[:,j,0,1],K,ls[j])
plt.title(r'$C_{VSfl} = $'+str(int(100*DP_S[1]))+r'%, $C_{Vfl} = $'+str(int(100*DP[0]))+'%')
plt.xscale('log')
plt.yticks(np.arange(1.,1.60,0.05))
plt.yticks(np.arange(1.,1.60,0.01), minor=True)
plt.axis([1e-6,1e-1,1.,1.35])
plt.grid(which='major', color='#AAAAAA')
plt.grid(which='minor', color='#DDDDDD')
plt.ylabel(r'$K_{CS}=U_{90}/V_2$')
plt.xlabel(r'Risco de Falha')
plt.legend(N)
plt.savefig('figura c1 3')

plt.figure(figsize=[8,6])
for j in range(len(N)):
    plt.plot(R[:,j,0,2],K,ls[j])
plt.title(r'$C_{VSfl} = $'+str(int(100*DP_S[2]))+r'%, $C_{Vfl} = $'+str(int(100*DP[0]))+'%')
plt.xscale('log')
plt.yticks(np.arange(1.,1.60,0.05))
plt.yticks(np.arange(1.,1.60,0.01), minor=True)
plt.axis([1e-6,1e-1,1.,1.4])
plt.grid(which='major', color='#AAAAAA')
plt.grid(which='minor', color='#DDDDDD')
plt.ylabel(r'$K_{CS}=U_{90}/V_2$')
plt.xlabel(r'Risco de Falha')
plt.legend(N)
plt.savefig('figura c1 5')

plt.figure(figsize=[8,6])
for j in range(len(N)):
    plt.plot(R[:,j,1,0],K,ls[j])
plt.title(r'$C_{VSfl} = $'+str(int(100*DP_S[0]))+r'%, $C_{Vfl} = $'+str(int(100*DP[1]))+'%')
plt.xscale('log')
plt.yticks(np.arange(1.,1.60,0.05))
plt.yticks(np.arange(1.,1.60,0.01), minor=True)
plt.axis([1e-6,1e-1,1.,1.4])
plt.grid(which='major', color='#AAAAAA')
plt.grid(which='minor', color='#DDDDDD')
plt.ylabel(r'$K_{CS}=U_{90}/V_2$')
plt.xlabel(r'Risco de Falha')
plt.legend(N)
plt.savefig('figura c1 2')

plt.figure(figsize=[8,6])
for j in range(len(N)):
    plt.plot(R[:,j,1,1],K,ls[j])
plt.title(r'$C_{VSfl} = $'+str(int(100*DP_S[1]))+r'%, $C_{Vfl} = $'+str(int(100*DP[1]))+'%')
plt.xscale('log')
plt.yticks(np.arange(1.,1.60,0.05))
plt.yticks(np.arange(1.,1.60,0.01), minor=True)
plt.axis([1e-6,1e-1,1.,1.5])
plt.grid(which='major', color='#AAAAAA')
plt.grid(which='minor', color='#DDDDDD')
plt.ylabel(r'$K_{CS}=U_{90}/V_2$')
plt.xlabel(r'Risco de Falha')
plt.legend(N)
plt.savefig('figura c1 4')

plt.figure(figsize=[8,6])
for j in range(len(N)):
    plt.plot(R[:,j,1,2],K,ls[j])
plt.title(r'$C_{VSfl} = $'+str(int(100*DP_S[2]))+r'%, $C_{Vfl} = $'+str(int(100*DP[1]))+'%')
plt.xscale('log')
plt.yticks(np.arange(1.,1.7,0.05))
plt.yticks(np.arange(1.,1.60,0.01), minor=True)
plt.axis([1e-6,1e-1,1.,1.60])
plt.grid(which='major', color='#AAAAAA')
plt.grid(which='minor', color='#DDDDDD')
plt.ylabel(r'$K_{CS}=U_{90}/V_2$')
plt.xlabel(r'Risco de Falha')
plt.legend(N)
plt.savefig('figura c1 6')
