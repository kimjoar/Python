# Returns k random numbers mod m based on p and q.
def blumblumshub(k, m, p, q):
  # Haven't added a prime check here. Miller-Rabin can be used, but remember: it is not deterministic.
  if (p % 4 != 3 or q % 4 != 3):
    raise Exception("p and q must be prime numbers and have a remainder of 3 when divided by 4")
  
  n = p * q
  # Should be chosen randomly, fixed suddenly ;)
  s = 101355
  x = s**2 % n

  b = []
  for i in range(k):
    x = x**2 % n
    b.append(x % m)
  
  return b

numbers = blumblumshub(20000, 10, 383, 503)

# Showing how the numbers are spread
h = {}
for i in numbers:
  if h.has_key(i):
    h[i] += 1
  else:
    h[i] = 0

print h