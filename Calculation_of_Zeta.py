import numpy as np

w0 = 2 * np.pi * 2.7728*10**3
zeta1= 0.92388
zeta2= 0.38268
R = 10000


def C(w0, zeta, R):
    tau1 = 1/(w0*zeta)
    tau2 = 1/(w0**2*tau1)
    
    c1 = tau1/R
    c2 = tau2/R

    return c1, c2

C1, C2 = C(w0, zeta1, R)
C3, C4 = C(w0, zeta2, R)

print(f'{C1} \n {C2} \n {C3} \n {C4}')
