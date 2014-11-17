
Python Test Suite
=================

Running suites/numpytest.py on Octuplets
    commit: `#01b6230bfd1cac67164bc5a3590d03d7400588a0 <https://bitbucket.org/bohrium/bohrium/commits/01b6230bfd1cac67164bc5a3590d03d7400588a0>`_,
    time: 2014-11-17 04:01:24.824935.

The CPU results::

  
  Traceback (most recent call last):
    File "test/numpy/numpytest.py", line 19, in <module>
      import bohrium as bh
    File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/__init__.py", line 11, in <module>
      from .array_create import *
  ImportError: No module named array_create
  
The GPU results::

  
  Traceback (most recent call last):
    File "test/numpy/numpytest.py", line 19, in <module>
      import bohrium as bh
    File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/__init__.py", line 11, in <module>
      from .array_create import *
  ImportError: No module named array_create
  
