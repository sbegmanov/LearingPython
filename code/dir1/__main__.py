print('Executing dir1.__main__.py')

import mod
print('Executing dir1.__main__.py:', mod.var.upper())

from . import mod
print('Executing dir1.__main__.py:', mod.var.upper())

import dir1.mod
print('Executing dir1.__main__.py:', dir1.mod.var.upper())

from dir1 import *
print('Executing dir1.__main__.py:', mod.var.upper())