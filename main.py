#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def f(n):

    l = []

    if n == 1:
        return "R"

    # 1:(n-1),...,(n-1):1
    for i in range(1, n):

        lefts, rights = f(n-i), f(i)

        for left in lefts:
            for right in rights:
                l.append("(%s+%s)"%(left, right))
                l.append("%s*%s"%(left, right))

    return l


if __name__ == "__main__":

    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = int(input("> "))

    ans = f(n)
    for a in ans:
        print(a)
