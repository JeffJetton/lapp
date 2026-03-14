# LAPP: Linear Algebra Pretty-Printer

* The `lapp.py` python file contains just a single outer function called `pprint()`
* `pprint()` works a lot like the regular `print()` function, except that any [NumPy](https://numpy.org) vectors and matrices are displayed in a manner closer to their traditional mathematics representation


### Examples of Use

**Basic Printing**


```
from lapp import *
import numpy as np

example_vector = np.array([2, 4, 6, 0, 1])
example_matrix = np.array([[8, 6, 7], [5, 3, 0], [9, -1, 0]])

print('How they look using print():\n')
print(example_vector)
print()
print(example_matrix)

print('\nUsing pprint():\n')
pprint(example_vector)
print()
pprint(example_matrix)
```

Output:

```
How they look using print():

[2 4 6 0 1]

[[ 8  6  7]
 [ 5  3  0]
 [ 9 -1  0]]

Using pprint():

⎡ 2 ⎤
⎢ 4 ⎥
⎢ 6 ⎥
⎢ 0 ⎥
⎣ 1 ⎦

⎡ 8   6  7 ⎤
⎢ 5   3  0 ⎥
⎣ 9  -1  0 ⎦
```

**Printing Multiple Items in a Row**

* Multiple items may be passed, separated by commas.
* Any items that aren't vectors or matrices are printed along the middle line (if an odd number of total rows) or the line below the middle point (if an even number of rows).
* This includes any newline ('\n') characters, so you'll probably want to avoid passing those expect as the final argument of items that print as only on or two printed rows.
* Unlike regular `print()`, items are normally not automatically printed with a space character between them. Any padding you want should be explictly included in your strings.
* The exception is when no vectors or matrices are passed at all, in which case the entire set of arguments is passed to the regular `print()` function, just as if you called it directly.

```
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
pprint('Vector addition... ', v1, ' + ', v2, ' = ', v1 + v2, '  ...is fun!')
print('\n\n')

v = np.array([0.5, -1, 2.5])
m = np.array([[2, 4, 6], [0, 1, -3]])
pprint(m, v, ' = ', m @ v)
print('\n')

v = np.array([-3, 4])
m = np.array([[1, -1], [0, 1]])
pprint(m, v, ' =   ',
       v[0], m[:,0], ' + ', v[1], m[:,1], ' =   ',
       v[0] * m[:,0], ' + ', v[1] * m[:,1], ' =   ',
       m @ v, '\n')
```

Output:

```
                   ⎡ 1 ⎤   ⎡ 4 ⎤   ⎡ 5 ⎤            
Vector addition... ⎢ 2 ⎥ + ⎢ 5 ⎥ = ⎢ 7 ⎥  ...is fun!
                   ⎣ 3 ⎦   ⎣ 6 ⎦   ⎣ 9 ⎦            



⎡ 2  4   6 ⎤⎡  0.5 ⎤   ⎡ 12.0 ⎤
⎣ 0  1  -3 ⎦⎢ -1.0 ⎥ = ⎣ -8.5 ⎦
            ⎣  2.5 ⎦           



⎡ 1  -1 ⎤⎡ -3 ⎤       ⎡ 1 ⎤    ⎡ -1 ⎤     ⎡ -3 ⎤   ⎡ -4 ⎤     ⎡ -7 ⎤
⎣ 0   1 ⎦⎣  4 ⎦ =   -3⎣ 0 ⎦ + 4⎣  1 ⎦ =   ⎣  0 ⎦ + ⎣  4 ⎦ =   ⎣  4 ⎦
 
```

