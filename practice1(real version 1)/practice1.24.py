
a = 12          
b = 7.5        
c = 4j          

print(type(a))
print(type(b))
print(type(c))


x = 100
y = -45
z = 987654321

print(type(x))
print(type(y))
print(type(z))



m = 2.75
n = -0.33
k = 8.0

print(type(m))
print(type(n))
print(type(k))



p = 3.4e2
q = 6E3
r = -1.2e4

print(type(p))
print(type(q))
print(type(r))



u = 1 + 7j
v = 9j
w = -2 + 4j

print(type(u))
print(type(v))
print(type(w))



num_int = 6
num_float = 9.8

a = float(num_int)     # int -> float
b = int(num_float)     # float -> int
c = complex(num_int)   # int -> complex

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


import random

print(random.randrange(10, 20))
