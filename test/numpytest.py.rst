
Python Test Suite
=================

Running suites/numpytest.py on Octuplets
    commit: `#eae832cb99c47396c757e62f24ff9aa492fe95c7 <https://bitbucket.org/bohrium/bohrium/commits/eae832cb99c47396c757e62f24ff9aa492fe95c7>`_,
    time: 2014-11-29 12:01:49.259471.

The CPU results::

  
  Traceback (most recent call last):
    File "test/numpy/numpytest.py", line 19, in <module>
      import bohrium as bh
    File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/__init__.py", line 11, in <module>
      from .array_create import *
    File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/array_create.py", line 7, in <module>
      from . import ndarray
    File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/ndarray.py", line 23, in <module>
      from _util import dtype_equal
    File "/home/bhbuilder/.local/lib/python2.7/site-packages/bohrium/_util.py", line 25, in <module>
      import bhc
  ImportError: No module named bhc
  
The GPU results::

  *** Testing the equivalency of Bohrium-NumPy and NumPy ***
  Testing test_accumulate.py/accumulate/cumprod
  [Info] [GPU] Kernel type: both
  [Info] [GPU] Compile type: async.
  [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
  Testing test_accumulate.py/accumulate/cumsum
  Testing test_ndstencil.py/ndstencil_1D/ndstencil_1D
  
  Traceback (most recent call last):
    File "test/numpy/numpytest.py", line 328, in <module>
      (res2,cmd2) = getattr(cls_inst,mth)(bh_arys)
    File "/home/bhbuilder/bohrium/test/numpy/test_ndstencil.py", line 18, in test_ndstencil_1D
      return self.run(pseudo_arrays)
    File "/home/bhbuilder/bohrium/test/numpy/numpytest.py", line 226, in run
      raise Exception("Benchmark error[%s]" % err)
  Exception: Benchmark error[pure virtual method called
  terminate called without an active exception
  ]
  
