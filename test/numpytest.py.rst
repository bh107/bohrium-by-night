
Python Test Suite
=================

Running suites/numpytest.py on Octuplets
    commit: `#fbb4f51971191402fc71c34310eae44732ee978f <https://bitbucket.org/bohrium/bohrium/commits/fbb4f51971191402fc71c34310eae44732ee978f>`_,
    time: 2014-11-09 04:01:19.265155.

The CPU results::

  *** Testing the equivalency of Bohrium-NumPy and NumPy ***
  Testing test_accumulate.py/accumulate/cumprod
  Testing test_accumulate.py/accumulate/cumsum
  Testing test_ndstencil.py/ndstencil_1D/ndstencil_1D
  Testing test_ndstencil.py/ndstencil_2D/ndstencil_2D
  Testing test_ndstencil.py/ndstencil_3D/ndstencil_3D
  Testing test_ndstencil.py/ndstencil_4D/ndstencil_4D
  Testing test_benchmarks.py/black_scholes/black_scholes
  Testing test_benchmarks.py/gameoflife/gameoflife
  Testing test_benchmarks.py/gauss/gauss
  Testing test_benchmarks.py/gauss_20x20/gauss_20x20
  Testing test_benchmarks.py/heat_equation/heat_equation
  Testing test_benchmarks.py/jacobi_fixed/jacobi_fixed
  Testing test_benchmarks.py/jacobi_module/jacobi_module
  We need to implement numpy.norm() for test_jacobi() to work
  Testing test_benchmarks.py/jacobi_solve/jacobi_solve
  Testing test_benchmarks.py/jacobi_stencil/jacobi_stencil
  Testing test_benchmarks.py/knn/knn
  Testing test_benchmarks.py/knn_naive/knn_naive
  Testing test_benchmarks.py/lu/lu
  Testing test_benchmarks.py/mxmul/mxmul
  Testing test_benchmarks.py/point27/point27
  Testing test_benchmarks.py/shallow_water/shallow_water
  Testing test_benchmarks.py/snakes_and_ladders/snakes_and_ladders
  
  Traceback (most recent call last):
    File "test/numpy/numpytest.py", line 311, in <module>
      (res2,cmd2) = getattr(cls_inst,mth)(bh_arys)
    File "/home/bhbuilder/bohrium/test/numpy/test_benchmarks.py", line 369, in test_snakes_and_ladders
      return self.run(pseudo_arrays)
    File "/home/bhbuilder/bohrium/test/numpy/numpytest.py", line 223, in run
      raise Exception("Benchmark error [stdout:%s,stderr:%s]" % (out, err))
  Exception: Benchmark error [stdout:,stderr:python: <stdin>:43: KRN_4038254239379796925721904974253386899415: Assertion `a0_first != ((void *)0)' failed.
  ]
  
The GPU results::

  *** Testing the equivalency of Bohrium-NumPy and NumPy ***
  Testing test_accumulate.py/accumulate/cumprod
  Testing test_accumulate.py/accumulate/cumsum
  Testing test_ndstencil.py/ndstencil_1D/ndstencil_1D
  
  Traceback (most recent call last):
    File "test/numpy/numpytest.py", line 311, in <module>
      (res2,cmd2) = getattr(cls_inst,mth)(bh_arys)
    File "/home/bhbuilder/bohrium/test/numpy/test_ndstencil.py", line 18, in test_ndstencil_1D
      return self.run(pseudo_arrays)
    File "/home/bhbuilder/bohrium/test/numpy/numpytest.py", line 225, in run
      raise Exception("Benchmark error[%s]" % err)
  Exception: Benchmark error[pure virtual method called
  terminate called without an active exception
  ]
  
