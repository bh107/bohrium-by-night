
Python Test Suite
=================

Running suites/numpytest.py on Octuplets
    commit: `#88335e0b0a721a97d5d4977fc8a3d842f4626957 <https://bitbucket.org/bohrium/bohrium/commits/88335e0b0a721a97d5d4977fc8a3d842f4626957>`_,
    time: 2014-09-18 13:44:36.068063.

The CPU results::

  
  Traceback (most recent call last):
    File "test/numpy/numpytest.py", line 18, in <module>
      import bohrium as bh
    File "/home/madsbk/.local/lib/python2.7/site-packages/bohrium/__init__.py", line 1, in <module>
      from array_create import *
    File "/home/madsbk/.local/lib/python2.7/site-packages/bohrium/array_create.py", line 7, in <module>
      import ndarray
    File "/home/madsbk/.local/lib/python2.7/site-packages/bohrium/ndarray.py", line 23, in <module>
      from _util import dtype_equal
    File "/home/madsbk/.local/lib/python2.7/site-packages/bohrium/_util.py", line 25, in <module>
      import bhc
    File "/home/madsbk/.local/lib/python2.7/site-packages/bohrium/bhc.py", line 28, in <module>
      _bhc = swig_import_helper()
    File "/home/madsbk/.local/lib/python2.7/site-packages/bohrium/bhc.py", line 24, in swig_import_helper
      _mod = imp.load_module('_bhc', fp, pathname, description)
  ImportError: /home/madsbk/.local/lib/python2.7/site-packages/bohrium/_bhc.so: undefined symbol: _Py_RefTotal
  
The GPU results::

  
  Traceback (most recent call last):
    File "test/numpy/numpytest.py", line 18, in <module>
      import bohrium as bh
    File "/home/madsbk/.local/lib/python2.7/site-packages/bohrium/__init__.py", line 1, in <module>
      from array_create import *
    File "/home/madsbk/.local/lib/python2.7/site-packages/bohrium/array_create.py", line 7, in <module>
      import ndarray
    File "/home/madsbk/.local/lib/python2.7/site-packages/bohrium/ndarray.py", line 23, in <module>
      from _util import dtype_equal
    File "/home/madsbk/.local/lib/python2.7/site-packages/bohrium/_util.py", line 25, in <module>
      import bhc
    File "/home/madsbk/.local/lib/python2.7/site-packages/bohrium/bhc.py", line 28, in <module>
      _bhc = swig_import_helper()
    File "/home/madsbk/.local/lib/python2.7/site-packages/bohrium/bhc.py", line 24, in swig_import_helper
      _mod = imp.load_module('_bhc', fp, pathname, description)
  ImportError: /home/madsbk/.local/lib/python2.7/site-packages/bohrium/_bhc.so: undefined symbol: _Py_RefTotal
  
