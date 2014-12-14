
Python Test Suite
=================

Running suites/numpytest.py on Octuplets
    commit: `#547326e20b909705a32277094af038672acc2e6f <https://bitbucket.org/bohrium/bohrium/commits/547326e20b909705a32277094af038672acc2e6f>`_,
    time: 2014-12-14 12:02:36.301211.

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
  Exception: Benchmark error[Program build error:
  ------------------- SOURCE -----------------------
  #pragma OPENCL EXTENSION cl_khr_fp64 : enable
  #ifdef FIXED_SIZE
  #define ds1 32
  #define ds0 32
  #define v1s0 0
  #define v1s2 34
  #define v1s1 1
  #define v3s0 1
  #define v3s2 34
  #define v3s1 1
  #define v5s0 2
  #define v5s2 34
  #define v5s1 1
  #define v7s0 34
  #define v7s2 34
  #define v7s1 1
  #define v9s0 35
  #define v9s2 34
  #define v9s1 1
  #define v11s0 36
  #define v11s2 34
  #define v11s1 1
  #define v13s0 68
  #define v13s2 34
  #define v13s1 1
  #define v15s0 69
  #define v15s2 34
  #define v15s1 1
  #define v17s0 70
  #define v17s2 34
  #define v17s1 1
  #define v18s0 0
  #define v18s2 32
  #define v18s1 1
  #endif
  __kernel __attribute__((work_group_size_hint(32, 4, 1))) void
  #ifndef FIXED_SIZE
  kernelc256298b62664beb
  #else
  kernelc256298b62664beb_
  #endif
  (
  	  __global double* a1
  	, __global double* a10
  	, const double s0
  	, const double s1
  #ifndef FIXED_SIZE
  	, const int ds1
  	, const int ds0
  	, const int v1s0
  	, const int v1s2
  	, const int v1s1
  	, const int v3s0
  	, const int v3s2
  	, const int v3s1
  	, const int v5s0
  	, const int v5s2
  	, const int v5s1
  	, const int v7s0
  	, const int v7s2
  	, const int v7s1
  	, const int v9s0
  	, const int v9s2
  	, const int v9s1
  	, const int v11s0
  	, const int v11s2
  	, const int v11s1
  	, const int v13s0
  	, const int v13s2
  	, const int v13s1
  	, const int v15s0
  	, const int v15s2
  	, const int v15s1
  	, const int v17s0
  	, const int v17s2
  	, const int v17s1
  	, const int v18s0
  	, const int v18s2
  	, const int v18s1
  #endif
  )
  
  {
  	const size_t gidx = get_global_id(0);
  	if (gidx >= ds0)
  		return;
  	const size_t gidy = get_global_id(1);
  	if (gidy >= ds1)
  		return;
  	double v1 = a1[gidy*v1s2 + gidx*v1s1 + v1s0];
  	double v3 = a1[gidy*v3s2 + gidx*v3s1 + v3s0];
  	double v5 = a1[gidy*v5s2 + gidx*v5s1 + v5s0];
  	double v7 = a1[gidy*v7s2 + gidx*v7s1 + v7s0];
  	double v9 = a1[gidy*v9s2 + gidx*v9s1 + v9s0];
  	double v11 = a1[gidy*v11s2 + gidx*v11s1 + v11s0];
  	double v13 = a1[gidy*v13s2 + gidx*v13s1 + v13s0];
  	double v15 = a1[gidy*v15s2 + gidx*v15s1 + v15s0];
  	double v17 = a1[gidy*v17s2 + gidx*v17s1 + v17s0];
  	double v0;
  	v0 = s0 + v1;
  	double v2;
  	v2 = v0 + v3;
  	double v4;
  	v4 = v2 + v5;
  	double v6;
  	v6 = v4 + v7;
  	double v8;
  	v8 = v6 + v9;
  	double v10;
  	v10 = v8 + v11;
  	double v12;
  	v12 = v10 + v13;
  	double v14;
  	v14 = v12 + v15;
  	double v16;
  	v16 = v14 + v17;
  	double v18;
  	v18 = v16 * s1;
  	a10[gidy*v18s2 + gidx*v18s1 + v18s0] = v18;
  }
  ------------------ SOURCE END --------------------
  ]
  
