import random

def miller_rabin(n):
  if n < 0 or n % 2 == 0:
    raise Exception("Only positive odd integers allowed.")

  k, q = miller_rabin_parameters(n-1)
  a = random.randint(2, n-2)

  if a**q % n == 1:
    return "inconclusive"

  for j in range(k):
    if a**(2**j*q) % n == n - 1:
      return "inconclusive"

  return "composite"

def miller_rabin_parameters(n):
  k = 0
  while n % 2 == 0:
    k += 1
    n /= 2
  q = n
  return k, q
  
print miller_rabin(13)   # Prime
print miller_rabin(17)   # Prime
print miller_rabin(15)   # Not prime
print miller_rabin(887)  # Prime
print miller_rabin(1999) # Prime
print miller_rabin(1785) # Not prime
print miller_rabin(2047) # Not a prime, but returns inconclusive for a = 2.