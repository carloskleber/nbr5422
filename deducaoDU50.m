% deducao DU50
syms a d u50
eq = u50 == 1708 + 532*(a-0.33) + 40.4*(a-0.33)^2 + 269*(d-4) - 9.81*(d-4)^2 + 139*(a-0.33)*(d-4);
sol = solve(eq, d)
simplify(sol)