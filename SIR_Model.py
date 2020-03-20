import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
from scipy.integrate import odeint
class SIRModel:
   def __init__(self, sir_parameters):
      self.alpha = sir_parameters['alpha']
      self.beta = sir_parameters['beta'] 
      self.lambd = sir_parameters['lambd']
      T = sir_parameters['T']
      self.dt = sir_parameters['dt']
      self.times = np.arange(0, T + self.dt, self.dt)
      n_iter = len(self.times)
      self.S = np.zeros(n_iter)
      self.I = np.zeros(n_iter)
      self.R = np.zeros(n_iter)
      self.D = np.zeros(n_iter)
      self.x0 = [0, 0, 0, 0]

   def initialize(self, s0, i0, r0, d0):
      self.x0 = [s0, i0, r0, d0]

   def SIRD(self, x, t):
      s, i, r, d = x
      dSdt =  -self.beta * s * i
      dIdt = self.beta * s * i - (1 / self.lambd + self.alpha) * i
      dRdt = (1. / self.lambd) * i
      dDdt = self.alpha * i
      return [dSdt, dIdt, dRdt, dDdt]

   def SIRD_compute(self):
      self.res = odeint(self.SIRD, self.x0, self.times)

   def plotcurves(self):
      labels = ["Susceptible", "Infected", "Recovered", "Dead"]
      plt.plot(self.times, self.res)
      plt.legend(labels)
      plt.show()

      