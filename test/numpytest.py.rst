
Python Test Suite
=================

Running suites/numpytest.py on Octuplets
    commit: `#eae832cb99c47396c757e62f24ff9aa492fe95c7 <https://bitbucket.org/bohrium/bohrium/commits/eae832cb99c47396c757e62f24ff9aa492fe95c7>`_,
    time: 2014-12-06 12:01:45.397469.

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
  Testing test_benchmarks.py/sor/sor
  Testing test_benchmarks.py/synth/synth
  Testing test_benchmarks.py/wireworld/wireworld
  Testing test_types.py/different_inputs/typecast
  Testing test_primitives.py/bh_opcodes/ufunc
  Testing test_array_create.py/array_create/zeros
  Testing test_views.py/diagonal/diagonal
  Testing test_views.py/flatten/flatten
  Testing test_views.py/transpose/transpose
  Testing test_matmul.py/matmul/dot
  Testing test_matmul.py/matmul/matmul
  Testing test_sor.py/sor/sor
  Testing test_specials.py/doubletranspose/doubletranspose
  Testing test_specials.py/largedim/largedim
  Testing test_specials.py/overlapping/add
  Testing test_specials.py/overlapping/identity
  Testing test_reduce.py/reduce/reduce
  Testing test_reduce.py/reduce1D/reduce
  Testing test_reduce.py/reduce_bool/boolean
  Testing test_reduce.py/reduce_sum/add_reduce
  Testing test_reduce.py/reduce_sum/sum
  ************************ Finish ************************
  
  
The GPU results::

  *** Testing the equivalency of Bohrium-NumPy and NumPy ***
  Testing test_accumulate.py/accumulate/cumprod
  [Info] [GPU] Kernel type: both
  [Info] [GPU] Compile type: async.
  [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
  Testing test_accumulate.py/accumulate/cumsum
  Testing test_ndstencil.py/ndstencil_1D/ndstencil_1D
  Testing test_ndstencil.py/ndstencil_2D/ndstencil_2D
  
  Traceback (most recent call last):
    File "test/numpy/numpytest.py", line 328, in <module>
      (res2,cmd2) = getattr(cls_inst,mth)(bh_arys)
    File "/home/bhbuilder/bohrium/test/numpy/test_ndstencil.py", line 34, in test_ndstencil_2D
      return self.run(pseudo_arrays)
    File "/home/bhbuilder/bohrium/test/numpy/numpytest.py", line 226, in run
      raise Exception("Benchmark error[%s]" % err)
  Exception: Benchmark error[pure virtual method called
  terminate called without an active exception
  ]
  
