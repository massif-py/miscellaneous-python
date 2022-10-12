#! python3
import pprint
print('A ✕ B ✕ C'.center(11))
print('————————————')
a = input('η(A) = ')
A = []
if a.isdecimal():
    for u in range(int(a)):
        A.append(u)
else:
    while True:
        a = input('η(A) = ')
        if a.isdecimal():
            for u1 in range(int(a)):
                A.append(u1)
            break
        else:
            None
b = input('η(B) = ')
B = []
if b.isdecimal():
    for v in range(int(b)):
        B.append(v)
else:
    while True:
        b = input('η(B) = ')
        if b.isdecimal():
            for v1 in range(int(b)):
                B.append(v1)
            break
        else:
            None
c = input('η(C) = ')
C = []
if c.isdecimal():
    for w in range(int(c)):
        C.append(w)
else:
    while True:
        c = input('η(C) = ')
        if c.isdecimal():
            for w1 in range(int(c)):
                C.append(w1)
            break
        else:
            None
A_B = []
for i in range(len(A)):
    for j in range(len(B)):
        A_B += [str(A[i]) + ', ' + str(B[j])]
A_B_C = []
for x in range(len(A_B)):
    for y in range(len(C)):
        A_B_C += ['(' + A_B[x] + ', ' + str(C[y]) + ')']
pprint.pprint(A_B_C)
print('η(A ✕ B ✕ C) = ', len(A_B_C))

