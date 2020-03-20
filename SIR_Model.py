import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
class SIRModel:
   def __init__(self, sir_parameters):
      self.beta = sir_parameters['beta'] 
      self.lambd = sir_parameters['lambd']
      T = sir_parameters['T']
      self.dt = sir_parameters['dt']
      self.times = np.arange(0, T + self.dt, self.dt)
      n_iter = len(self.times)
      self.S = np.zeros(n_iter)
      self.I = np.zeros(n_iter)
      self.R = np.zeros(n_iter)

   def initialize(self, s0, i0, r0):
      self.S[0] = s0
      self.I[0] = i0
      self.R[0] = r0

   def Survival(self, s, i):
      return -self.beta * s * i * self.dt + s

   def Infected(self, s, i) :
      return self.beta * s * i * self.dt - (1 / self.lambd) * i * self.dt + i

   def Recovered(self, i, r) :
      return (1 / self.lambd) * i * self.dt + r

   def compute(self) :
      for i in range(len(self.times) - 1):
         self.S[i + 1] = self.Survival(self.S[i], self.I[i])
         self.I[i + 1] = self.Infected(self.S[i], self.I[i])
         self.R[i + 1] = self.Recovered(self.I[i], self.R[i])

   def plotcurves(self):
      plt.plot(self.times, self.S, label = 'Survival')
      plt.plot(self.times, self.I)
      plt.plot(self.times, self.R)
      plt.show()
      