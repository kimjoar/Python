# Solves a^b mod n using the method of repeated squaring
# Because bin(b) returns "0b..." we must remove 2 from the length to get the 
# range, and jump past the two first bits when checking.
def modular_exponentiation(a,b,n):
  d, b = 1, bin(b)

  for i in range(len(b)-2):
    d = (d*d) % n
    if int(b[i+2]) == 1:
      d = (d*a) % n

  return d

print modular_exponentiation(7,560,561)        # 1
print modular_exponentiation(3,892,7)          # 4
print modular_exponentiation(16383,1207,7)     # 3
print modular_exponentiation(16383,16777216,7) # 4