
Python Test Suite
=================

Running suites/numpytest.py on Octuplets
    commit: `#bbe0e6d6a7b38272dfd5d5ad2f2be99bb2292f4c <https://bitbucket.org/bohrium/bohrium/commits/bbe0e6d6a7b38272dfd5d5ad2f2be99bb2292f4c>`_,
    time: 2014-10-04 04:00:36.352151.

The CPU results::

  *** Testing the equivalency of Bohrium-NumPy and NumPy ***
  Testing test_accumulate.py/accumulate/cumprod
  Testing test_accumulate.py/accumulate/cumsum
  Testing test_ndstencil.py/ndstencil_1D/ndstencil_1D
  
  Traceback (most recent call last):
    File "test/numpy/numpytest.py", line 293, in <module>
      (res1,cmd1) = getattr(cls_inst,mth)(np_arys)
    File "/home/bhbuilder/bohrium/test/numpy/test_ndstencil.py", line 18, in test_ndstencil_1D
      return self.run(pseudo_arrays)
    File "/home/bhbuilder/bohrium/test/numpy/numpytest.py", line 221, in run
      raise Exception("Benchmark error [stdout:%s,stderr:%s]" % (out, err))
  Exception: Benchmark error [stdout:,stderr:/usr/bin/python: No module named gameoflife
  ]
  
The GPU results::

  *** Testing the equivalency of Bohrium-NumPy and NumPy ***
  Testing test_accumulate.py/accumulate/cumprod
  Testing test_accumulate.py/accumulate/cumsum
  Testing test_ndstencil.py/ndstencil_1D/ndstencil_1D
  
  Traceback (most recent call last):
    File "test/numpy/numpytest.py", line 293, in <module>
      (res1,cmd1) = getattr(cls_inst,mth)(np_arys)
    File "/home/bhbuilder/bohrium/test/numpy/test_ndstencil.py", line 18, in test_ndstencil_1D
      return self.run(pseudo_arrays)
    File "/home/bhbuilder/bohrium/test/numpy/numpytest.py", line 221, in run
      raise Exception("Benchmark error [stdout:%s,stderr:%s]" % (out, err))
  Exception: Benchmark error [stdout:,stderr:/usr/bin/python: No module named gameoflife
  ]
  
