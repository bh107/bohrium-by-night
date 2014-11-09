
Raw Benchmark Output
====================

Running Jacobi Stencil on Octuplets using Bohrium/GPU
    commit: `#fbb4f51971191402fc71c34310eae44732ee978f <https://bitbucket.org/bohrium/bohrium/commits/fbb4f51971191402fc71c34310eae44732ee978f>`_,
    time: 2014-11-09 04:04:03.190753.

    command: ``python benchmark/Python/jacobi_stencil.py --size=100*100*10 --bohrium=True``

Run 00
~~~~~~
    stdout::

        benchmark/Python/jacobi_stencil.py - target: bhc, bohrium: True, size: 100*100*10, elapsed-time: 0.038919
        Options :-DFIXED_SIZE
        Options :
        Options :
        Options :-DFIXED_SIZE
        Options :
        Options :-DFIXED_SIZE
        Options :
        Options :-DFIXED_SIZE
        

    stderr::

        Program build error:
        Program build error:
        Program build error:
        ------------------- SOURCE -----------------------
        Program build error:
        ------------------- SOURCE -----------------------
        Program build error:
        ------------------- SOURCE -----------------------
        #pragma OPENCL EXTENSION cl_khr_fp64 : enable
        #ifdef FIXED_SIZE
        #define ds1 102
        #define ds0 102
        #define v0s0 0
        #define v0s2 102
        #define v0s1 1
        #endif
        __kernel void
        #ifndef FIXED_SIZE
        kernel365b626006b1c7ad
        #else
        kernel365b626006b1c7ad_
        #endif
        (
        	  __global double* a0
        	, const double s0
        #ifndef FIXED_SIZE
        	, const int ds1
        	, const int ds0
        	, const int v0s0
        	, const int v0s2
        	, const int v0s1
        #endif
        )
        
        {
        	const size_t gidx = get_global_id(0);
        	if (gidx >= ds0)
        		return;
        	const size_t gidy = get_global_id(1);
        	if (gidy >= ds1)
        		return;
        	double v0;
        	v0 = s0;
        	a0[gidy*v0s2 + gidx*v0s1 + v0s0] = v0;
        }
        #pragma OPENCL EXTENSION cl_khr_fp64 : enable
        #ifdef FIXED_SIZE
        #define ds1 102
        #define ds0 102
        #define v0s0 0
        #define v0s2 102
        #define v0s1 1
        #endif
        __kernel void
        #ifndef FIXED_SIZE
        kernel365b626006b1c7ad
        #else
        kernel365b626006b1c7ad_
        #endif
        (
        	  __global double* a0
        	, const double s0
        #ifndef FIXED_SIZE
        	, const int ds1
        	, const int ds0
        	, const int v0s0
        	, const int v0s2
        	, const int v0s1
        #endif
        )
        
        {
        	const size_t gidx = get_global_id(0);
        	if (gidx >= ds0)
        		return;
        	const size_t gidy = get_global_id(1);
        	if (gidy >= ds1)
        		return;
        	double v0;
        	v0 = s0;
        	a0[gidy*v0s2 + gidx*v0s1 + v0s0] = v0;
        }
        ------------------ SOURCE END --------------------
        ------------------- SOURCE -----------------------
        #pragma OPENCL EXTENSION cl_khr_fp64 : enable
        #ifdef FIXED_SIZE
        #define ds1 100
        #define ds0 100
        #define v1s0 103
        #define v1s2 102
        #define v1s1 1
        #define v2s0 1
        #define v2s2 102
        #define v2s1 1
        #define v4s0 104
        #define v4s2 102
        #define v4s1 1
        #define v6s0 102
        #define v6s2 102
        #define v6s1 1
        #define v8s0 205
        #define v8s2 102
        #define v8s1 1
        #define v9s0 0
        #define v9s2 100
        #define v9s1 1
        #endif
        __kernel void
        #ifndef FIXED_SIZE
        kernel132302237b5829b0
        #else
        kernel132302237b5829b0_
        #endif
        (
        	  __global double* a1
        	, __global double* a5
        	, const double s0
        #ifndef FIXED_SIZE
        	, const int ds1
        	, const int ds0
        	, const int v1s0
        	, const int v1s2
        	, const int v1s1
        	, const int v2s0
        	, const int v2s2
        	, const int v2s1
        	, const int v4s0
        	, const int v4s2
        	, const int v4s1
        	, const int v6s0
        	, const int v6s2
        	, const int v6s1
        	, const int v8s0
        	, const int v8s2
        	, const int v8s1
        	, const int v9s0
        	, const int v9s2
        	, const int v9s1
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
        	double v2 = a1[gidy*v2s2 + gidx*v2s1 + v2s0];
        	double v4 = a1[gidy*v4s2 + gidx*v4s1 + v4s0];
        	double v6 = a1[gidy*v6s2 + gidx*v6s1 + v6s0];
        	double v8 = a1[gidy*v8s2 + gidx*v8s1 + v8s0];
        	double v0;
        	v0 = v1 + v2;
        	double v3;
        	v3 = v0 + v4;
        	double v5;
        	v5 = v3 + v6;
        	double v7;
        	v7 = v5 + v8;
        	double v9;
        	v9 = s0 * v7;
        	a5[gidy*v9s2 + gidx*v9s1 + v9s0] = v9;
        }
        ------------------ SOURCE END --------------------
        ------------------ SOURCE END --------------------
        ------------------- SOURCE -----------------------
        #pragma OPENCL EXTENSION cl_khr_fp64 : enable
        #ifdef FIXED_SIZE
        #define ds1 100
        #define ds0 100
        #define v0s0 103
        #define v0s2 102
        #define v0s1 1
        #define v1s0 0
        #define v1s2 100
        #define v1s1 1
        #endif
        __kernel void
        #ifndef FIXED_SIZE
        kernela2073dbc7e118bac
        #else
        kernela2073dbc7e118bac_
        #endif
        (
        	  __global double* a0
        	, __global double* a1
        #ifndef FIXED_SIZE
        	, const int ds1
        	, const int ds0
        	, const int v0s0
        	, const int v0s2
        	, const int v0s1
        	, const int v1s0
        	, const int v1s2
        	, const int v1s1
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
        	double v0;
        	v0 = v1;
        	a0[gidy*v0s2 + gidx*v0s1 + v0s0] = v0;
        }
        ------------------ SOURCE END --------------------
        Program build error:
        Program build error:
        ------------------- SOURCE -----------------------
        ------------------- SOURCE -----------------------
        #pragma OPENCL EXTENSION cl_khr_fp64 : enable
        #ifdef FIXED_SIZE
        #define ds1 100
        #define ds0 100
        #define v1s0 103
        #define v1s2 102
        #define v1s1 1
        #define v2s0 1
        #define v2s2 102
        #define v2s1 1
        #define v4s0 104
        #define v4s2 102
        #define v4s1 1
        #define v6s0 102
        #define v6s2 102
        #define v6s1 1
        #define v8s0 205
        #define v8s2 102
        #define v8s1 1
        #define v9s0 0
        #define v9s2 100
        #define v9s1 1
        #endif
        __kernel void
        #ifndef FIXED_SIZE
        kernel132302237b5829b0
        #else
        kernel132302237b5829b0_
        #endif
        (
        	  __global double* a1
        	, __global double* a5
        	, const double s0
        #ifndef FIXED_SIZE
        	, const int ds1
        	, const int ds0
        	, const int v1s0
        	, const int v1s2
        	, const int v1s1
        	, const int v2s0
        	, const int v2s2
        	, const int v2s1
        	, const int v4s0
        	, const int v4s2
        	, const int v4s1
        	, const int v6s0
        	, const int v6s2
        	, const int v6s1
        	, const int v8s0
        	, const int v8s2
        	, const int v8s1
        	, const int v9s0
        	, const int v9s2
        	, const int v9s1
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
        	double v2 = a1[gidy*v2s2 + gidx*v2s1 + v2s0];
        	double v4 = a1[gidy*v4s2 + gidx*v4s1 + v4s0];
        	double v6 = a1[gidy*v6s2 + gidx*v6s1 + v6s0];
        	double v8 = a1[gidy*v8s2 + gidx*v8s1 + v8s0];
        	double v0;
        	v0 = v1 + v2;
        	double v3;
        	v3 = v0 + v4;
        	double v5;
        	v5 = v3 + v6;
        	double v7;
        	v7 = v5 + v8;
        	double v9;
        	v9 = s0 * v7;
        	a5[gidy*v9s2 + gidx*v9s1 + v9s0] = v9;
        }
        ------------------ SOURCE END --------------------
        #pragma OPENCL EXTENSION cl_khr_fp64 : enable
        #ifdef FIXED_SIZE
        #define ds1 100
        #define ds0 100
        #define v0s0 103
        #define v0s2 102
        #define v0s1 1
        #define v1s0 0
        #define v1s2 100
        #define v1s1 1
        #endif
        __kernel void
        #ifndef FIXED_SIZE
        kernela2073dbc7e118bac
        #else
        kernela2073dbc7e118bac_
        #endif
        (
        	  __global double* a0
        	, __global double* a1
        #ifndef FIXED_SIZE
        	, const int ds1
        	, const int ds0
        	, const int v0s0
        	, const int v0s2
        	, const int v0s1
        	, const int v1s0
        	, const int v1s2
        	, const int v1s1
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
        	double v0;
        	v0 = v1;
        	a0[gidy*v0s2 + gidx*v0s1 + v0s0] = v0;
        }
        #pragma OPENCL EXTENSION cl_khr_fp64 : enable
        #ifdef FIXED_SIZE
        #define ds0 102
        #define v0s0 0
        #define v0s1 102
        #define v1s0 101
        #define v1s1 102
        #endif
        __kernel void
        #ifndef FIXED_SIZE
        kernel1d2fa358fdab3a69
        #else
        kernel1d2fa358fdab3a69_
        #endif
        (
        	  __global double* a0
        	, const double s0
        	, const double s1
        #ifndef FIXED_SIZE
        	, const int ds0
        	, const int v0s0
        	, const int v0s1
        	, const int v1s0
        	, const int v1s1
        #endif
        )
        
        {
        	const size_t gidx = get_global_id(0);
        	if (gidx >= ds0)
        		return;
        	double v0;
        	v0 = s0;
        	double v1;
        	v1 = s1;
        	a0[gidx*v0s1 + v0s0] = v0;
        	a0[gidx*v1s1 + v1s0] = v1;
        }
        ------------------ SOURCE END --------------------
        ------------------ SOURCE END --------------------
        terminate called after throwing an instance of 'cl::Error'
        Program build error:
        terminate called recursively
        ------------------- SOURCE -----------------------
        #pragma OPENCL EXTENSION cl_khr_fp64 : enable
        #ifdef FIXED_SIZE
        #define ds0 102
        #define v0s0 0
        #define v0s1 102
        #define v1s0 101
        #define v1s1 102
        #endif
        __kernel void
        #ifndef FIXED_SIZE
        kernel1d2fa358fdab3a69
        #else
        kernel1d2fa358fdab3a69_
        #endif
        (
        	  __global double* a0
        	, const double s0
        	, const double s1
        #ifndef FIXED_SIZE
        	, const int ds0
        	, const int v0s0
        	, const int v0s1
        	, const int v1s0
        	, const int v1s1
        #endif
        )
        
        {
        	const size_t gidx = get_global_id(0);
        	if (gidx >= ds0)
        		return;
        	double v0;
        	v0 = s0;
        	double v1;
        	v1 = s1;
        	a0[gidx*v0s1 + v0s0] = v0;
        	a0[gidx*v1s1 + v1s0] = v1;
        }
        ------------------ SOURCE END --------------------
        terminate called recursively
          what():  clGetProgramBuildInfo
        



