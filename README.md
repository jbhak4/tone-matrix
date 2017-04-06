# tone-matrix
Tone Matrix is built in Python 3. It can be used as a command-line script,
building a tone matrix when provided with an ordered pitch-class set.
```
> ToneMatrix.py 7 2 1 9 0 8
<7, 2, 1, 9, 0, 8>
<0, 7, 6, 2, 5, 1>
<1, 8, 7, 3, 6, 2>
<5, 0, E, 7, T, 6>
<2, 9, 8, 4, 7, 3>
<6, 1, 0, 8, E, 7>
```

The arguments must be integers, for example:
```
> ToneMatrix.py 10 11 4 5 3 6
<T, E, 4, 5, 3, 6>
<9, T, 3, 4, 2, 5>
<4, 5, T, E, 9, 0>
<3, 4, 9, T, 8, E>
<5, 6, E, 0, T, 1>
<2, 3, 8, 9, 7, T>
```

Tone Matrix can also be used as a Python library.
```python3
from ToneMatrix import ToneMatrix as tone_matrix
tm = tone_matrix([7, 2, 1, 9, 0, 8, 10, 11, 4, 5, 3, 6])
print(tm.P(7))
print(tm.P(0))
print(tm.I(0))
print(tm.R(0))
print(tm.RI(0))
```
```
<7, 2, 1, 9, 0, 8, T, E, 4, 5, 3, 6>
<0, 7, 6, 2, 5, 1, 3, 4, 9, T, 8, E>
<0, 5, 6, T, 7, E, 9, 8, 3, 2, 4, 1>
<E, 8, T, 9, 4, 3, 1, 5, 2, 6, 7, 0>
<1, 4, 2, 3, 8, 9, E, 7, T, 6, 5, 0>
```

