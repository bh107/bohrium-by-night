
Python Test Suite
=================

Running suites/numpytest.py on Octuplets
    commit: `#e2eb8cda5af33d49993cdc9c0473aa962908adf4 <https://bitbucket.org/bohrium/bohrium/commits/e2eb8cda5af33d49993cdc9c0473aa962908adf4>`_,
    time: 2014-09-19 14:49:29.645054.

The CPU results::

  
  Traceback (most recent call last):
    File "test/numpy/numpytest.py", line 18, in <module>
      import bohrium as bh
    File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/__init__.py", line 1, in <module>
      from array_create import *
  ImportError: No module named array_create
  
The GPU results::

  
  Traceback (most recent call last):
    File "test/numpy/numpytest.py", line 18, in <module>
      import bohrium as bh
    File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/__init__.py", line 1, in <module>
      from array_create import *
  ImportError: No module named array_create
  
