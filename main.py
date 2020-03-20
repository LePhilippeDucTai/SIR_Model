import SIR_Model as sm

if __name__ == "__main__":
    parameters = {'beta': 0.001, 'lambd' : 4, 'T' : 28, 'dt' : 0.01}
    M = sm.SIRModel(parameters)
    M.initialize(s0 = 1000, i0 = 10, r0 = 0)
    M.compute()
    M.plotcurves()