# Greatest common divisor using the Euclidean algorithm

def gcd(a, b):
  x, y = a, b
  while y != 0:
    r = x % y
    x, y = y, r  
  return x
  
print gcd(252, 198) # 18