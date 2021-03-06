# n system
This script is written in Python3.

# Usage

```
$ ./main.py 3
```

or

```
$ ./main.py
> 3
```

# Recusion algorithm

```
n=1
R

n=2
(R+R) ->  f(1) + f(1)
 R*R  ->  f(1) * f(1)

n=3
R+R+R   -> f(2) + f(1) or f(1) + f(2)
(R+R)*R -> f(2) * f(1)
R*R*R   -> f(2) * f(1) or f(2) * f(1)
R*R+R   -> f(2) + f(1)

n=4
  (R*R+R)*R -> f(3) * f(1)
    R*R*R+R -> f(3) + f(1)
    R*R+R*R -> f(3) * f(1)
    R*R+R+R -> f(3) + f(1)
  (R+R)*R*R -> f(3) * f(1)
(R+R)*(R+R) -> f(2) * f(2)
  R+R*(R+R) -> f(1) + f(3)
    R*R*R*R -> f(3) * f(1)
  (R+R+R)*R -> f(3) * f(1)
    R+R+R+R -> f(3) + f(1)
    
Therefore, 
f(n-1) + f(1)
f(n-1) * f(1)
f(n-2) + f(2)
f(n-2) * f(2)
f(n-3) + f(3)
f(n-3) * f(3)
to
f(cell(n/2)) + f(floor(n/2))
f(cell(n/2)) * f(floor(n/2))

```
