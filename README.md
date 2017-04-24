# WIP
# funcall
UFCS for Python.  

An implementaion of [UFCS(Uniform function call syntax)](https://en.wikipedia.org/wiki/Uniform_Function_Call_Syntax) for Python. This package allows any function to be called using the syntax for member accessing. An object wrapped the `funcall.obj` function becomes to accept any function as its own member. The object is converted to a `funcall.ChainableObject`, but it behaves as expected.
```python
from funcall import obj

x = obj(5).range.sum
# This is equivalent to;
# x = sum(range(5))

y = x + 5
# x is a ChainableObject, but behaves as int.
```
## Installation
`funcall` has no dipendencies.
```bash
$ sudo pip install funcall
```
## Usage
### ChainableObject.map, filter, reduce
Implementations as methods of builtiin-functions. Arguments passed to them should be callable objects.  
```python
from funcall import obj

obj('pen pineapple apple pen').split.map(str.capitalize)
# This is equivalent to;
map(str.capitalize, 'pen pinapple apple pen'.split())
```
### ChainableObject.call
A method which calls function passed as an argument. This is useful when using anonymous functions or functions bound to different namespaces.
```python
from funcall import obj

obj('pen pineapple apple pen').split.call('-'.join)
# This is equivalent to;
'-'.join('pen pineapple apple pen'.split())

import numpy as np

obj(5).call(np.arange)
# This is equivalent to;
np.arange(5)
# obj(5).np.arange does'nt work...
```

