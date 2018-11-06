import sys
L = 12, 34, 56
print L
M = L, (1, 2)
print M
print M[0]
empty = ()
print len(empty)
singleton = 'hello',
print len(singleton)
print singleton
basket = {'A', 'B', 12, 0, -12}
basket1 = {'A', 'B', 'C', 'D'}
print basket
R = 'A' in basket
print R
print basket | basket1
print basket & basket1
print basket ^ basket1
print basket - basket1
tel = {"A" : 1234, "B" : 5678}
print tel
tel["C"] = 9009
print tel
print list(tel.keys())
print sorted(tel.keys())
M = dict({"A" : 1, "B" : 2})
print M
N = {x : x ** 2 for x in (1, 2, 4, 6)}
print N
P = dict(ABC = 1, CDE = 2)
print P
Night = {"A" : 1, "B" : 2}
for k, v in Night.items():
    print (k, v)
Q = ["1", "2"]
A = ["A", "B"]
for q, a in zip(Q, A):
    print("YES{1}.".format(q, a))
