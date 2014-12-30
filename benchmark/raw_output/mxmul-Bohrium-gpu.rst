
Raw Benchmark Output
====================

Running Matrix Multiplication on Octuplets using Bohrium/GPU
    commit: `#87974a097720c3bf944f8d7b93c8752e16ec3c6d <https://bitbucket.org/bohrium/bohrium/commits/87974a097720c3bf944f8d7b93c8752e16ec3c6d>`_,
    time: 2014-12-30 04:07:07.845036.

    command: ``python benchmark/Python/mxmul.py --size=1000 --bohrium=True``

Run 00
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/mxmul.py - target: bhc, bohrium: True, size: 1000, elapsed-time: 0.002245
        Options :-I/home/bhbuilder/.local/share/bohrium/include -DFIXED_SIZE
        

    stderr::

        Program build error:
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
        ------------------ SOURCE END --------------------
        



Run 01
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/mxmul.py - target: bhc, bohrium: True, size: 1000, elapsed-time: 0.002739
        

    stderr::

        pure virtual method called
        terminate called without an active exception
        



Run 02
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/mxmul.py - target: bhc, bohrium: True, size: 1000, elapsed-time: 0.002619
        

    stderr::

        pure virtual method called
        terminate called without an active exception
        



