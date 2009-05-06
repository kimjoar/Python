import math

# Extended greatest common divisor
# Always returns the greatest common divisor of m and b, 
# and returns the multiplicative inverse of b if it exists.
# Returns -1 if there does not exist a multiplicative 
# inverse of b.

def egcd(m, b):
  a1, a2, a3 = 1, 0, m
  b1, b2, b3 = 0, 1, b
  
  while b3 >= 0:
    if b3 == 0:
      return (int(a3), -1)
    
    if b3 == 1:
      return (int(b3), int(b2))
    
    q = math.floor(a3/b3)
  
    t1, t2, t3 = a1 - q*b1, a2 - q*b2, a3 - q*b3
    a1, a2, a3 = b1, b2, b3
    b1, b2, b3 = t1, t2, t3
    
print egcd(1759, 550)
print egcd(15, 3)