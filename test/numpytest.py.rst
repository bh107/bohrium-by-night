
Python Test Suite
=================

Running suites/numpytest.py on Octuplets
    commit: `#84083907fa6c76d7ab7e01356cd1607b0dc4bcc2 <https://bitbucket.org/bohrium/bohrium/commits/84083907fa6c76d7ab7e01356cd1607b0dc4bcc2>`_,
    time: 2014-11-04 04:02:10.200830.

The CPU results::

  
  Traceback (most recent call last):
    File "test/numpy/numpytest.py", line 18, in <module>
      import bohrium as bh
    File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/__init__.py", line 1, in <module>
      from .array_create import *
  ImportError: No module named array_create
  
The GPU results::

  
  Traceback (most recent call last):
    File "test/numpy/numpytest.py", line 18, in <module>
      import bohrium as bh
    File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/__init__.py", line 1, in <module>
      from .array_create import *
    File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/array_create.py", line 7, in <module>
      from . import ndarray
    File "ndarray.pyx", line 23, in init ndarray (/home/bhbuilder/bohrium/build/bridge/bhpy/ndarray.c:4901)
    File "_util.pyx", line 24, in init _util (/home/bhbuilder/bohrium/build/bridge/bhpy/_util.c:2446)
  ImportError: cannot import name _info
  
