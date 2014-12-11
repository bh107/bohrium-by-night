
Raw Benchmark Output
====================

Running Jacobi Stencil on Octuplets using Bohrium/GPU
    commit: `#eae832cb99c47396c757e62f24ff9aa492fe95c7 <https://bitbucket.org/bohrium/bohrium/commits/eae832cb99c47396c757e62f24ff9aa492fe95c7>`_,
    time: 2014-12-11 12:09:19.761457.

    command: ``python benchmark/Python/jacobi_stencil.py --size=3000*3000*100 --bohrium=True``

Run 00
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/jacobi_stencil.py - target: bhc, bohrium: True, size: 3000*3000*100, elapsed-time: 0.385261
        Options :-I/home/bhbuilder/.local/share/bohrium/include 
        Options :-I/home/bhbuilder/.local/share/bohrium/include 
        Options :-I/home/bhbuilder/.local/share/bohrium/include -DFIXED_SIZE
        

    stderr::

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
        Program build error:
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
        Program build error:
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
        Program build error:
        



Run 01
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/jacobi_stencil.py - target: bhc, bohrium: True, size: 3000*3000*100, elapsed-time: 0.381841
        

    stderr::

        pure virtual method called
        terminate called without an active exception
        



Run 02
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/jacobi_stencil.py - target: bhc, bohrium: True, size: 3000*3000*100, elapsed-time: 0.382537
        

    stderr::

        pure virtual method called
        terminate called without an active exception
        



