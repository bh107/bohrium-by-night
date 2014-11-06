
Python Test Suite
=================

Running suites/numpytest.py on Octuplets
    commit: `#fbb4f51971191402fc71c34310eae44732ee978f <https://bitbucket.org/bohrium/bohrium/commits/fbb4f51971191402fc71c34310eae44732ee978f>`_,
    time: 2014-11-06 04:02:02.248349.

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
  ImportError: No module named array_create
  
