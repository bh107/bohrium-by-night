
Raw Benchmark Output
====================

Running Lattice Boltzmann D2Q9 on Octuplets using Bohrium/GPU
    commit: `#10b1512ac636a011c7f5bb54083d6cb268fa1397 <https://bitbucket.org/bohrium/bohrium/commits/10b1512ac636a011c7f5bb54083d6cb268fa1397>`_,
    time: 2015-01-13 04:08:47.337654.

    command: ``python benchmark/Python/lattice_boltzmann_D2Q9.py --size=1000*1000*10 --bohrium=True``

Run 00
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        Options :-I/home/bhbuilder/.local/share/bohrium/include -DFIXED_SIZE
        Options :-I/home/bhbuilder/.local/share/bohrium/include 
        

    stderr::

        Traceback (most recent call last):
          File "benchmark/Python/lattice_boltzmann_D2Q9.py", line 230, in <module>
            main()
          File "benchmark/Python/lattice_boltzmann_D2Q9.py", line 196, in main
            state = cylinder(H, W, obstacle=False)
          File "benchmark/Python/lattice_boltzmann_D2Q9.py", line 42, in cylinder
            t_3d    = np.asarray(t)[:, np.newaxis, np.newaxis]
        AttributeError: 'module' object has no attribute 'asarray'
        Program build error:
        Program build error:
        ------------------- SOURCE -----------------------
        #ifdef FIXED_SIZE
        #define ds0 998
        #define v3s0 0
        #define v3s1 1
        #endif
        __kernel __attribute__((work_group_size_hint(128, 1, 1))) void
        #ifndef FIXED_SIZE
        kernela4acd29f66fb6412
        #else
        kernela4acd29f66fb6412_
        #endif
        (
        	  __global long* a3
        	, const long s0
        	, const long s1
        #ifndef FIXED_SIZE
        	, const int ds0
        	, const int v3s0
        	, const int v3s1
        #endif
        )
        
        {
        	const size_t gidx = get_global_id(0);
        	if (gidx >= ds0)
        		return;
        	ulong v0;
        	v0 = gidx;
        	long v1;
        	v1 = v0;
        	long v2;
        	v2 = v1 * s0;
        	long v3;
        	v3 = v2 + s1;
        	a3[gidx*v3s1 + v3s0] = v3;
        }
        ------------------ SOURCE END --------------------
        ------------------- SOURCE -----------------------
        #ifdef FIXED_SIZE
        #define ds0 998
        #define v3s0 0
        #define v3s1 1
        #endif
        __kernel __attribute__((work_group_size_hint(128, 1, 1))) void
        #ifndef FIXED_SIZE
        kernela4acd29f66fb6412
        #else
        kernela4acd29f66fb6412_
        #endif
        (
        	  __global long* a3
        	, const long s0
        	, const long s1
        #ifndef FIXED_SIZE
        	, const int ds0
        	, const int v3s0
        	, const int v3s1
        #endif
        )
        
        {
        	const size_t gidx = get_global_id(0);
        	if (gidx >= ds0)
        		return;
        	ulong v0;
        	v0 = gidx;
        	long v1;
        	v1 = v0;
        	long v2;
        	v2 = v1 * s0;
        	long v3;
        	v3 = v2 + s1;
        	a3[gidx*v3s1 + v3s0] = v3;
        }
        ------------------ SOURCE END --------------------
        



Run 01
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        

    stderr::

        Traceback (most recent call last):
          File "benchmark/Python/lattice_boltzmann_D2Q9.py", line 230, in <module>
            main()
          File "benchmark/Python/lattice_boltzmann_D2Q9.py", line 196, in main
            state = cylinder(H, W, obstacle=False)
          File "benchmark/Python/lattice_boltzmann_D2Q9.py", line 42, in cylinder
            t_3d    = np.asarray(t)[:, np.newaxis, np.newaxis]
        AttributeError: 'module' object has no attribute 'asarray'
        pure virtual method called
        terminate called without an active exception
        



Run 02
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        

    stderr::

        Traceback (most recent call last):
          File "benchmark/Python/lattice_boltzmann_D2Q9.py", line 230, in <module>
            main()
          File "benchmark/Python/lattice_boltzmann_D2Q9.py", line 196, in main
            state = cylinder(H, W, obstacle=False)
          File "benchmark/Python/lattice_boltzmann_D2Q9.py", line 42, in cylinder
            t_3d    = np.asarray(t)[:, np.newaxis, np.newaxis]
        AttributeError: 'module' object has no attribute 'asarray'
        pure virtual method called
        terminate called without an active exception
        



