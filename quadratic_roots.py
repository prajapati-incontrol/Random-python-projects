import numpy as np
import math


def quadraticRoots(a, b, c):
   roots = []
   root1 = 0
   root2 = 0
	   
   #value of b^2 - 4*a*c
   temp = pow(b,2) - 4*a*c
   # if temp < 0 roots are imaginary
   if temp < 0:
       roots.append(-1)
   else:
       #calculate root1 and root2 using formula
       root1 = math.floor((-b + math.sqrt(temp))/(2*a))
       root2 = math.floor((-b - math.sqrt(temp))/(2*a))
       
       roots.append(max(root1, root2))
       roots.append(min(root1, root2))
       
   return roots