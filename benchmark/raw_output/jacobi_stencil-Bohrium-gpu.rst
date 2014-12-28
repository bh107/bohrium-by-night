
Raw Benchmark Output
====================

Running Jacobi Stencil on Octuplets using Bohrium/GPU
    commit: `#901c71bad23e6603afe61daa6330aaa6603550aa <https://bitbucket.org/bohrium/bohrium/commits/901c71bad23e6603afe61daa6330aaa6603550aa>`_,
    time: 2014-12-28 04:06:33.318049.

    command: ``python benchmark/Python/jacobi_stencil.py --size=3000*3000*100 --bohrium=True``

Run 00
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/jacobi_stencil.py - target: bhc, bohrium: True, size: 3000*3000*100, elapsed-time: 0.385179
        Options :-I/home/bhbuilder/.local/share/bohrium/include 
        Options :-I/home/bhbuilder/.local/share/bohrium/include 
        Options :-I/home/bhbuilder/.local/share/bohrium/include -DFIXED_SIZE
        Options :-I/home/bhbuilder/.local/share/bohrium/include 
        Options :-I/home/bhbuilder/.local/share/bohrium/include -DFIXED_SIZE
        Options :-I/home/bhbuilder/.local/share/bohrium/include -DFIXED_SIZE
        Options :-I/home/bhbuilder/.local/share/bohrium/include -DFIXED_SIZE
        Options :-I/home/bhbuilder/.local/share/bohrium/include 
        Options :-I/home/bhbuilder/.local/share/bohrium/include 
        Options :-I/home/bhbuilder/.local/share/bohrium/include -DFIXED_SIZE
        

    stderr::

        Program build error:
        Program build error:
        ------------------- SOURCE -----------------------
        ------------------- SOURCE -----------------------
        Program build error:
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
        ------------------ SOURCE END --------------------
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
        ------------------ SOURCE END --------------------
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
        ------------------ SOURCE END --------------------
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
        #define v6s0 3002
        #define v6s2 3002
        #define v6s1 1
        #define v8s0 6005
        #define v8s2 3002
        #define v8s1 1
        #define v9s0 0
        #define v9s2 3000
        #define v9s1 1
        #endif
        __kernel __attribute__((work_group_size_hint(32, 4, 1))) void
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
        #define v6s0 3002
        #define v6s2 3002
        #define v6s1 1
        #define v8s0 6005
        #define v8s2 3002
        #define v8s1 1
        #define v9s0 0
        #define v9s2 3000
        #define v9s1 1
        #endif
        __kernel __attribute__((work_group_size_hint(32, 4, 1))) void
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
        terminate called after throwing an instance of 'cl::Error'
        Program build error:
        ------------------- SOURCE -----------------------
        #pragma OPENCL EXTENSION cl_khr_fp64 : enable
        #ifdef FIXED_SIZE
        #define ds1 3002
        #define ds0 3002
        #define v0s0 0
        #define v0s2 3002
        #define v0s1 1
        #endif
        __kernel __attribute__((work_group_size_hint(32, 4, 1))) void
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
        Program build error:
        ------------------- SOURCE -----------------------
        #pragma OPENCL EXTENSION cl_khr_fp64 : enable
        #ifdef FIXED_SIZE
        #define ds0 3002
        #define v0s0 0
        #define v0s1 3002
        #define v1s0 3001
        #define v1s1 3002
        #endif
        __kernel __attribute__((work_group_size_hint(128, 1, 1))) void
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
        



Run 01
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/jacobi_stencil.py - target: bhc, bohrium: True, size: 3000*3000*100, elapsed-time: 0.382605
        

    stderr::

        pure virtual method called
        terminate called without an active exception
        



Run 02
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/jacobi_stencil.py - target: bhc, bohrium: True, size: 3000*3000*100, elapsed-time: 0.382638
        

    stderr::

        pure virtual method called
        terminate called without an active exception
        



