#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pprint import pprint
from itertools import product
import sys

def f(n):

    l = []

    if n == 1:
        return "R"

    # 1:(n-1),...,(n-1):1
    for i in range(1, n):

        left, right = f(n-i), f(i)

        if type(left) is str and type(right) is str:
            #l.append("%s+%s"%(left, right))
            l.append("(%s+%s)"%(left, right))
            l.append("%s*%s"%(left, right))
        else:
            #l.append([left, "+", right])
            l.append(["(", left, "+", right, ")"])
            l.append([left, "*", right])

    return l


def exe(n):
    ans = f(n)
    for a in ans:
        #print(''.join([str(aa) for aa in a]))
        """
        if type(a) is list:
            print("{", end="")
            print(*a, end="")
            print("}")
        else:
            print(a)
        """
        print(a)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = int(input("> "))
    exe(n)
