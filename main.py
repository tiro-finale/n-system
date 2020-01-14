#!/usr/bin/env python3
from pprint import pprint
from itertools import product
import sys

"""
n=1
R

n=2
(R+R) -> (f(1) + f(1))
 R*R  ->  f(1) * f(1)

n=3
R+R+R   -> f(2) + f(1) or f(1) + f(2)
(R+R)*R -> f(2) * f(1)
R*R*R   -> f(2) * f(1) or f(2) * f(1)
R*R+R   -> f(2) + f(1)

n=4
  (R*R+R)*R -> (f(3)) * f(1)
    R*R*R+R -> f(3) + f(1)
    R*R+R*R -> f(3) * f(1)
    R*R+R+R -> f(3) + f(1)
  (R+R)*R*R -> f(3) * f(1)
(R+R)*(R+R) -> f(2) * f(2)
  R+R*(R+R) -> f(1) + f(3)
    R*R*R*R -> f(3) * f(1) or f(1) * f(3)
  (R+R+R)*R -> (f(3)) * f(1)
    R+R+R+R -> f(3) + f(1)
"""

def f(n):

    l = []

    if n == 1:
        return "R"

    # 1:(n-1),...,(n-1):1
    for i in range(1, n):

        left, right = f(n-i), f(i)

        if type(left) is str and type(right) is str:
            l.append("%s+%s"%(left, right))
            l.append("(%s+%s)"%(left, right))
            l.append("%s*%s"%(left, right))
        else:
            l.append([left, "+", right])
            l.append(["(", left, "+", right, ")"])
            l.append([left, "*", right])

    return l


def xprint(data):
    for d in data:
        if type(d) is str:
            print(d, end="")
        elif type(d) is list:
            xprint(d)

    print("")

def exe(n):
    ans = f(n)
    for a in ans:
        #print(''.join([str(aa) for aa in a]))
        print(a)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = int(input("> "))
    exe(n)
