
Raw Benchmark Output
====================

Running Jacobi Stencil on Octuplets using Bohrium/GPU
    commit: `#0bd1688e19d0dc8dc039822a0b29ab2e51c76102 <https://bitbucket.org/bohrium/bohrium/commits/0bd1688e19d0dc8dc039822a0b29ab2e51c76102>`_,
    time: 2015-01-11 04:07:12.114344.

    command: ``python benchmark/Python/jacobi_stencil.py --size=3000*3000*100 --bohrium=True``

Run 00
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/jacobi_stencil.py - target: bhc, bohrium: True, size: 3000*3000*100, elapsed-time: 0.382576
        Options :-I/home/bhbuilder/.local/share/bohrium/include 
        Options :-I/home/bhbuilder/.local/share/bohrium/include Options :-I/home/bhbuilder/.local/share/bohrium/include -DFIXED_SIZE
        
        Options :-I/home/bhbuilder/.local/share/bohrium/include -DFIXED_SIZE
        Options :-I/home/bhbuilder/.local/share/bohrium/include 
        

    stderr::

        Program build error:
        ------------------- SOURCE -----------------------
        #pragma OPENCL EXTENSION cl_khr_fp64 : enable
        #ifdef FIXED_SIZE
        #define ds1 3000
        #define ds0 3000
        #define v1s0 3003
        #define v1s2 3002
        #define v1s1 1
        #define v2s0 1
        #define v2s2 3002
        #define v2s1 1
        #define v4s0 3004
        #define v4s2 3002
        #define v4s1 1
        #define v5s0 0
        #define v5s2 3000
        #define v5s1 1
        #define v6s0 3002
        #define v6s2 3002
        #define v6s1 1
        #define v7s0 0
        #define v7s2 3000
        #define v7s1 1
        #define v8s0 6005
        #define v8s2 3002
        #define v8s1 1
        #endif
        __kernel __attribute__((work_group_size_hint(32, 4, 1))) void
        #ifndef FIXED_SIZE
        kernelb38a8d0182ad6625
        #else
        kernelb38a8d0182ad6625_
        #endif
        (
        	  __global double* a1
        	, __global double* a3
        	, __global double* a4
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
        	, const int v5s0
        	, const int v5s2
        	, const int v5s1
        	, const int v6s0
        	, const int v6s2
        	, const int v6s1
        	, const int v7s0
        	, const int v7s2
        	, const int v7s1
        	, const int v8s0
        	, const int v8s2
        	, const int v8s1
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
        	a3[gidy*v5s2 + gidx*v5s1 + v5s0] = v5;
        	a4[gidy*v7s2 + gidx*v7s1 + v7s0] = v7;
        }
        Program build error:
        Program build error:
        ------------------- SOURCE -----------------------
        ------------------- SOURCE -----------------------
        #pragma OPENCL EXTENSION cl_khr_fp64 : enable
        #ifdef FIXED_SIZE
        #define ds1 3000
        #define ds0 3000
        #define v1s0 0
        #define v1s2 3000
        #define v1s1 1
        #define v2s0 3003
        #define v2s2 3002
        #define v2s1 1
        #endif
        __kernel __attribute__((work_group_size_hint(32, 4, 1))) void
        #ifndef FIXED_SIZE
        kerneld196159f1ae4934c
        #else
        kerneld196159f1ae4934c_
        #endif
        (
        	  __global double* a1
        	, __global double* a2
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
        	v0 = s0 * v1;
        	double v2;
        	v2 = v0;
        	a2[gidy*v2s2 + gidx*v2s1 + v2s0] = v2;
        }
        ------------------ SOURCE END --------------------
        #pragma OPENCL EXTENSION cl_khr_fp64 : enable
        #ifdef FIXED_SIZE
        #define ds1 3000
        #define ds0 3000
        #define v1s0 0
        #define v1s2 3000
        #define v1s1 1
        #define v2s0 3003
        #define v2s2 3002
        #define v2s1 1
        #endif
        __kernel __attribute__((work_group_size_hint(32, 4, 1))) void
        #ifndef FIXED_SIZE
        kerneld196159f1ae4934c
        #else
        kerneld196159f1ae4934c_
        #endif
        (
        	  __global double* a1
        	, __global double* a2
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
        	v0 = s0 * v1;
        	double v2;
        	v2 = v0;
        	a2[gidy*v2s2 + gidx*v2s1 + v2s0] = v2;
        }
        Program build error:
        ------------------ SOURCE END --------------------
        ------------------ SOURCE END --------------------
        Program build error:
        ------------------- SOURCE -----------------------
        #pragma OPENCL EXTENSION cl_khr_fp64 : enable
        #ifdef FIXED_SIZE
        #define ds1 3000
        #define ds0 3000
        #define v0s0 3003
        #define v0s2 3002
        #define v0s1 1
        #define v1s0 0
        #define v1s2 3000
        #define v1s1 1
        #endif
        __kernel __attribute__((work_group_size_hint(32, 4, 1))) void
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
        Program build error:
        



Run 01
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/jacobi_stencil.py - target: bhc, bohrium: True, size: 3000*3000*100, elapsed-time: 0.381134
        

    stderr::

        pure virtual method called
        terminate called without an active exception
        



Run 02
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/jacobi_stencil.py - target: bhc, bohrium: True, size: 3000*3000*100, elapsed-time: 0.383218
        

    stderr::

        pure virtual method called
        terminate called without an active exception
        



