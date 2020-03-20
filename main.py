# Python 3.8.2 64-bit

import SIR_Model as sm
if __name__ == "__main__":
    parameters = {'alpha' : 0.02, 'beta': 0.5, 'lambd' : 8, 'T' : 140, 'dt' : 0.01}
    M = sm.SIRModel(parameters)
    M.initialize(s0 = 1., i0 = 1.27 * 10**-6, r0 = 0, d0 = 0)
    M.SIRD_compute()
    M.plotcurves()
