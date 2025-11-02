import numpy as np
def find_period(L0,L1):
   
   for L in range(L0,L1+1,1):
   
       g = 9.81 #m/s^2
       T = 2 * np.pi * np.sqrt(L/g) #in seconds
       print("When L = %4.1f m, T = %2.1f s" % (L,T))

   T0 = 2 * np.pi * np.sqrt(L0/g) #in s
   T1 = 2 * np.pi * np.sqrt(L1/g) #in s
   
   return T0,T1