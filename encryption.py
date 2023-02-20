p, a, b = 2549, 412, 223
print((4 * a ** 3 + 27 * b ** 2) % p)


def L(a):
    """"return k in {-1, 0, 1} Legendre symbol (a/p)"""
    k = (a ** 1274 % p)  # where 1274=(p-1)/2
    # print("L(a)=",k)
    return k


def E(x):
    """return (y) such that y=(sqrt(x**3=a*x+b))%p """
    y2 = (x ** 3 + a * x + b) % p
    if L(y2) == 1:
        # y=(y2**1828)%p #where 1828=(p+1)/4
        for i in range(2436):
            if (i * i) % p == y2:
                y = i
                return y
    else:
        print("Error L(", y2, ")=", L(y2) - p)
        return None


def check(X):
    if (X[0] == None):
        return True, None
    else:
        return (X[1] ** 2) % p == (X[0] ** 3 + a * X[0] + b) % p


def add(x1, y1, x2, y2):
    """return (X) such that  X=P+Q in E, P=[x1,y1], Q=[x2,y2]"""
    if (x1 == None):
        X = [x2, y2]
        return X
    elif (x2 == None):
        X = [x1, y1]
        return X
    if ((x1 == x2) and (y1 == (-y2) % p)):
        lam = 0
        X = [None, None]
        return X
    elif ((x1 == x2) and (y1 == y2)):
        k = mulinv(p + 2 * y1, p)
        lam = ((3 * x1 ** 2 + a) * k) % p
    else:
        k = mulinv(p + (x2 - x1), p)
        lam = ((y2 - y1) * k) % p
    x3 = (lam ** 2 - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p
    X = [x3, y3]
    return X


def xgcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0


def mulinv(a, b):
    """return x such that (x * a) % b == 1"""
    g, x, _ = xgcd(a, b)
    if g == 1:
        return x % b


G = []
G.append(9)
G.append(E(G[0]))
print("G=", G, "check -", check(G))
M = G
for i in range(10000):
    M = add(M[0], M[1], G[0], G[1])
    if (M[1] == (-G[1]) % p):
        print("n=", i)
        break
na = 145
nb = 113
Pa = G
for i in range(na):
    Pa = add(Pa[0], Pa[1], G[0], G[1])
print("Pa=", Pa, "check -", check(Pa))
Pb = G
for i in range(nb):
    Pb = add(Pb[0], Pb[1], G[0], G[1])
print("Pb=", Pb, "check -", check(Pb))
Ka = Pb
for i in range(na):
    Ka = add(Ka[0], Ka[1], Pb[0], Pb[1])
Kb = Pa
for i in range(nb):
    Kb = add(Kb[0], Kb[1], Pa[0], Pa[1])
print(Ka == Kb, "K=", Ka)

Pm = [513]
Pm.append(E(Pm[0]))
print("Pm=", Pm, "check -", check(Pm))

import random

k = random.randint(0, p - 1)
k = Kb[0]
Cm = []
Cm.append(G)
for i in range(k):
    Cm[0] = add(Cm[0][0], Cm[0][1], G[0], G[1])
Cm.append(Pa)
for i in range(k):
    Cm[1] = add(Cm[1][0], Cm[1][1], Pa[0], Pa[1])
Cm[1] = add(Pm[0], Pm[1], Cm[1][0], Cm[1][1])
print("Cm=", Cm)
nakG = Cm[0]
for i in range(na):
    nakG = add(nakG[0], nakG[1], Cm[0][0], Cm[0][1])
A = add(Cm[1][0], Cm[1][1], nakG[0], (-nakG[1]) % p)
print(A)
