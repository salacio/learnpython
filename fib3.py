from sympy import *
from sympy.abc import (n,)
fib = (GoldenRatio ** n - (1 - GoldenRatio) ** n) / sqrt(5)
f = lambda n_: fib.subs([(n, n_)])
