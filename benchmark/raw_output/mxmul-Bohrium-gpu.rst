
Raw Benchmark Output
====================

Running Matrix Multiplication on Octuplets using Bohrium/GPU
    commit: `#10b1512ac636a011c7f5bb54083d6cb268fa1397 <https://bitbucket.org/bohrium/bohrium/commits/10b1512ac636a011c7f5bb54083d6cb268fa1397>`_,
    time: 2015-01-13 04:08:47.337654.

    command: ``python benchmark/Python/mxmul.py --size=1000 --bohrium=True``

Run 00
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/mxmul.py - target: bhc, bohrium: True, size: 1000, elapsed-time: 0.002232
        Options :-I/home/bhbuilder/.local/share/bohrium/include -DFIXED_SIZE
        Options :-I/home/bhbuilder/.local/share/bohrium/include -DFIXED_SIZE
        Options :-I/home/bhbuilder/.local/share/bohrium/include -DFIXED_SIZE
        Options :-I/home/bhbuilder/.local/share/bohrium/include 
        Options :-I/home/bhbuilder/.local/share/bohrium/include 
        Options :-I/home/bhbuilder/.local/share/bohrium/include 
        

    stderr::

        Program build error:
        Program build error:
        Program build error:
        Program build error:
        ------------------- SOURCE -----------------------
        ------------------- SOURCE -----------------------
        #pragma OPENCL EXTENSION cl_khr_fp64 : enable
        #ifdef FIXED_SIZE
        #define ds1 1000
        #define v0s2 1000
        #define v1s2 1000000
        #define ds0 1000
        #define v0s1 1
        #define v1s1 1000
        #define v0s0 0
        #define v1s0 0
        #define N 1000
        #define S 1
        #endif
        __kernel void
        #ifndef FIXED_SIZE
        kernel84a05998f3ca627d
        #else
        kernel84a05998f3ca627d_
        #endif
        (
        	  __global double* out
        	, __global double* in
        #ifndef FIXED_SIZE
        	, const int ds1
        	, const int v0s2
        	, const int v1s2
        	, const int ds0
        	, const int v0s1
        	, const int v1s1
        	, const int v0s0
        	, const int v1s0
        	, const int N
        	, const int S
        #endif
        )
        
        {
        	const size_t gidx = get_global_id(0);
        	if (gidx >= ds0)
        		return;
        	const size_t gidy = get_global_id(1);
        	if (gidy >= ds1)
        		return;
        	size_t element = gidy*v1s2 + gidx*v1s1 + v1s0;
        	double accu = in[element];
        	for (int i = 1; i < N; ++i)
        	{
        		element += S;
        		accu = accu + in[element];
        	}
        	out[gidy*v0s2 + gidx*v0s1 + v0s0] = accu;
        }
        Program build error:
        ------------------- SOURCE -----------------------
        ------------------- SOURCE -----------------------
        ------------------- SOURCE -----------------------
        #pragma OPENCL EXTENSION cl_khr_fp64 : enable
        #ifdef FIXED_SIZE
        #define ds0 1000000
        #define v3s0 0
        #define v3s1 1
        #define v7s0 0
        #define v7s1 1
        #endif
        __kernel __attribute__((work_group_size_hint(128, 1, 1))) void
        #ifndef FIXED_SIZE
        kernel2ef478afd926545a
        #else
        kernel2ef478afd926545a_
        #endif
        (
        	  __global double* a3
        	, __global double* a7
        	, const double s0
        	, const double s1
        	, const double s2
        	, const double s3
        #ifndef FIXED_SIZE
        	, const int ds0
        	, const int v3s0
        	, const int v3s1
        	, const int v7s0
        	, const int v7s1
        #endif
        )
        
        {
        	const size_t gidx = get_global_id(0);
        	if (gidx >= ds0)
        		return;
        	ulong v0;
        	v0 = gidx;
        	double v1;
        	v1 = v0;
        	double v2;
        	v2 = v1 * s0;
        	double v3;
        	v3 = v2 + s1;
        	ulong v4;
        	v4 = gidx;
        	double v5;
        	v5 = v4;
        	double v6;
        	v6 = v5 * s2;
        	double v7;
        	v7 = v6 + s3;
        	a3[gidx*v3s1 + v3s0] = v3;
        	a7[gidx*v7s1 + v7s0] = v7;
        }
        Program build error:
        #pragma OPENCL EXTENSION cl_khr_fp64 : enable
        #ifdef FIXED_SIZE
        #define ds2 1000
        #define ds1 1000
        #define ds0 1000
        #define v0s0 0
        #define v0s3 1000000
        #define v0s2 1000
        #define v0s1 1
        #define v1s0 0
        #define v1s3 1000
        #define v1s2 0
        #define v1s1 1
        #define v2s0 0
        #define v2s3 0
        #define v2s2 1
        #define v2s1 1000
        #endif
        __kernel __attribute__((work_group_size_hint(32, 2, 2))) void
        #ifndef FIXED_SIZE
        kernel7ea44a65f26f54ee
        #else
        kernel7ea44a65f26f54ee_
        #endif
        (
        	  __global double* a0
        	, __global double* a1
        	, __global double* a2
        #ifndef FIXED_SIZE
        	, const int ds2
        	, const int ds1
        	, const int ds0
        	, const int v0s0
        	, const int v0s3
        	, const int v0s2
        	, const int v0s1
        	, const int v1s0
        	, const int v1s3
        	, const int v1s2
        	, const int v1s1
        	, const int v2s0
        	, const int v2s3
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
        	const size_t gidz = get_global_id(2);
        	if (gidz >= ds2)
        		return;
        	double v1 = a1[gidz*v1s3 + gidy*v1s2 + gidx*v1s1 + v1s0];
        	double v2 = a2[gidz*v2s3 + gidy*v2s2 + gidx*v2s1 + v2s0];
        	double v0;
        	v0 = v1 * v2;
        	a0[gidz*v0s3 + gidy*v0s2 + gidx*v0s1 + v0s0] = v0;
        }
        ------------------ SOURCE END --------------------
        ------------------ SOURCE END --------------------
        #pragma OPENCL EXTENSION cl_khr_fp64 : enable
        #ifdef FIXED_SIZE
        #define ds2 1000
        #define ds1 1000
        #define ds0 1000
        #define v0s0 0
        #define v0s3 1000000
        #define v0s2 1000
        #define v0s1 1
        #define v1s0 0
        #define v1s3 1000
        #define v1s2 0
        #define v1s1 1
        #define v2s0 0
        #define v2s3 0
        #define v2s2 1
        #define v2s1 1000
        #endif
        __kernel __attribute__((work_group_size_hint(32, 2, 2))) void
        #ifndef FIXED_SIZE
        kernel7ea44a65f26f54ee
        #else
        kernel7ea44a65f26f54ee_
        #endif
        (
        	  __global double* a0
        	, __global double* a1
        	, __global double* a2
        #ifndef FIXED_SIZE
        	, const int ds2
        	, const int ds1
        	, const int ds0
        	, const int v0s0
        	, const int v0s3
        	, const int v0s2
        	, const int v0s1
        	, const int v1s0
        	, const int v1s3
        	, const int v1s2
        	, const int v1s1
        	, const int v2s0
        	, const int v2s3
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
        	const size_t gidz = get_global_id(2);
        	if (gidz >= ds2)
        		return;
        	double v1 = a1[gidz*v1s3 + gidy*v1s2 + gidx*v1s1 + v1s0];
        	double v2 = a2[gidz*v2s3 + gidy*v2s2 + gidx*v2s1 + v2s0];
        	double v0;
        	v0 = v1 * v2;
        	a0[gidz*v0s3 + gidy*v0s2 + gidx*v0s1 + v0s0] = v0;
        }
        ------------------ SOURCE END --------------------
        ------------------- SOURCE -----------------------
        #pragma OPENCL EXTENSION cl_khr_fp64 : enable
        #ifdef FIXED_SIZE
        #define ds1 1000
        #define v0s2 1000
        #define v1s2 1000000
        #define ds0 1000
        #define v0s1 1
        #define v1s1 1000
        #define v0s0 0
        #define v1s0 0
        #define N 1000
        #define S 1
        #endif
        __kernel void
        #ifndef FIXED_SIZE
        kernel84a05998f3ca627d
        #else
        kernel84a05998f3ca627d_
        #endif
        (
        	  __global double* out
        	, __global double* in
        #ifndef FIXED_SIZE
        	, const int ds1
        	, const int v0s2
        	, const int v1s2
        	, const int ds0
        	, const int v0s1
        	, const int v1s1
        	, const int v0s0
        	, const int v1s0
        	, const int N
        	, const int S
        #endif
        )
        
        {
        	const size_t gidx = get_global_id(0);
        	if (gidx >= ds0)
        		return;
        	const size_t gidy = get_global_id(1);
        	if (gidy >= ds1)
        		return;
        	size_t element = gidy*v1s2 + gidx*v1s1 + v1s0;
        	double accu = in[element];
        	for (int i = 1; i < N; ++i)
        	{
        		element += S;
        		accu = accu + in[element];
        	}
        	out[gidy*v0s2 + gidx*v0s1 + v0s0] = accu;
        }
        ------------------ SOURCE END --------------------
        ------------------ SOURCE END --------------------
        #pragma OPENCL EXTENSION cl_khr_fp64 : enable
        #ifdef FIXED_SIZE
        #define ds0 1000000
        #define v3s0 0
        #define v3s1 1
        #define v7s0 0
        #define v7s1 1
        #endif
        __kernel __attribute__((work_group_size_hint(128, 1, 1))) void
        #ifndef FIXED_SIZE
        kernel2ef478afd926545a
        #else
        kernel2ef478afd926545a_
        #endif
        (
        	  __global double* a3
        	, __global double* a7
        	, const double s0
        	, const double s1
        	, const double s2
        	, const double s3
        #ifndef FIXED_SIZE
        	, const int ds0
        	, const int v3s0
        	, const int v3s1
        	, const int v7s0
        	, const int v7s1
        #endif
        )
        
        {
        	const size_t gidx = get_global_id(0);
        	if (gidx >= ds0)
        		return;
        	ulong v0;
        	v0 = gidx;
        	double v1;
        	v1 = v0;
        	double v2;
        	v2 = v1 * s0;
        	double v3;
        	v3 = v2 + s1;
        	ulong v4;
        	v4 = gidx;
        	double v5;
        	v5 = v4;
        	double v6;
        	v6 = v5 * s2;
        	double v7;
        	v7 = v6 + s3;
        	a3[gidx*v3s1 + v3s0] = v3;
        	a7[gidx*v7s1 + v7s0] = v7;
        }
        ------------------ SOURCE END --------------------
        



Run 01
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/mxmul.py - target: bhc, bohrium: True, size: 1000, elapsed-time: 0.002392
        

    stderr::

        N/A



Run 02
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/mxmul.py - target: bhc, bohrium: True, size: 1000, elapsed-time: 0.002344
        

    stderr::

        N/A



