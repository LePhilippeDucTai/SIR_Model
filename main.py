import SIR_Model as sm

if __name__ == "__main__":
    parameters = {'alpha' : 0.02, 'beta': 0.005, 'lambd' : 4, 'T' : 100, 'dt' : 0.01}
    M = sm.SIRModel(parameters)
    M.initialize(s0 = 100, i0 = 1)
    M.compute()
    M.plotcurves()