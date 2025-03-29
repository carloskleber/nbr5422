# HIW - Estudo de modelos _High Intensity Wind_


## Referências

1. ASCE. Guidelines for electrical transmisison line structurl loading, ASCE manuals and reports on engineering practice No. 74, 4th ed., 2020.
1. H. Aboshosha. Response of transmission line conductors under downburst wind. Ph.D. thesis, The University of Western Ontario, Canada, 2014. https://ir.lib.uwo.ca/etd/2237/

## Lista de variáveis
* $R_y^F$ - Vetor de reação $y$ considerando sem deslocamento
* $f_x$ - Vetor de carga desbalanceado na direação $x$
* $\mathbf{K}_{yz}$ - Matriz de rigidez
* $v$ - Comprimento da cadeia de isoladores
* $\mathbf{d}_x$ - Vetor de deslocamento do condutor na direção $x$
* $L_x$ - Comprimento do vão
* $M_{igK}$ - Momento de primeira ordem em torno do eixo $i$ no ponto $K$, induzido por um carregamento $g_j(s)$

## Amortecimento aerodinâmico do condutor sob downburst (Chapter 4)

$$
\begin{align}
dF & = \frac{1}{2} \rho C_d D V_{ns} (n,t)^2 + \rho C_d D V_c (n,t) V_{ns} (n,t) \\
dF_{air} & = \rho C_d D V_c (n,t) V_{ns0} (t) \varphi_V (n) \\
f_{airmod} & = \int_0^1 dF_{air} \, L \, \phi_y(n) \, dn \nonumber \\
& = \rho \, C_d \, D \, L \, V_{ns0} (t) \, V_{cmod} \int_0^1 \phi_v (n) \, \phi_y^2 (n) \, dn \\
F_{viscous} & = 4 \pi f \, \zeta_{airDb} \, V_{cmod} \, m^{*} \\
m^{*} & = m \, L \int_0^1 \phi^2 (n) \, dn
\end{align}
$$

## Efeito dinâmico (Chapter 5)

$$
\begin{align}
R_y & = R_y^F + \mathbf{K}_{yz} \mathbf{d}_y \\
R_z & = R_z^F + \mathbf{K}_{yz} \mathbf{d}_z \\
d_x^{i+1} & = d_x^i + \mathbf{K}_x^i \mathbf{f}_x^i \\
R_x & = d_x \cdot \frac{R_{res}}{v} \\
d_y & = v \cdot \frac{R_y}{R_{res}} \\
d_z & = v-v \cdot \frac{R_z}{R_{res}} \\
R_{res} & = \sqrt{R_x^2 + R_y^2 + R_z^2}
\end{align}
$$

## Parâmetros "HIW" (Appendix A)

$$
\mathbf{R}_y^F = \begin{bmatrix} \frac{M_{zgyA1}}{L_x} \\ \frac{M_{zgyB1} + M_{zgyA2}}{L_x} \\ \frac{M_{zgyB2} + M_{zgyA3}}{L_x} \\ \vdots \\ \frac{M_{zgyBNd-2} + M_{zgyANd-1}}{L_x} \\ \frac{M_{zgyBNd-1}}{L_x} \end{bmatrix}
$$

$$
C_n = L_0 b_n a_n \left[ 2(L_x +dx_{N+1} -dx_N)^2 \left( \frac{L_0 b_n}{L_x+dx_{N+1}-dx_N}-1\right)^{3/2}\right]^{-1}
$$

## Parâmetros "Downburst" (Appendix B)

$$
\begin{bmatrix}
\frac{T_1}{L_x} & -\frac{T_1}{L_x} \\
-\frac{T_1}{L_x} & \frac{T_1}{L_x} + \frac{T_2}{L_x}
\end{bmatrix}
$$

$$
C_n = L_0\frac{1}{\sqrt{2}}\sqrt{\int_0^1 Q_{yn} (s)^{*2} ds+\frac{W^2 L_x^2}{12}+2\frac{T_n}{L_x} \left[(dy_{N+1} -dy_N) \int_0^1 Q_{yn} (s)^* ds\right]} \left[ 2(L_x + dx_{N+1}-dx_N)^2 \left( \frac{L_0}{L_x-dx_{N+1}-dx_N}\right)^{3/2} \right]^{-1}
$$