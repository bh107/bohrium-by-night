
Raw Benchmark Output
====================

Running N-Body on Octuplets using Bohrium/GPU
    commit: `#ab2423965300f898abbf676d8643a6f9cf6f92db <https://bitbucket.org/bohrium/bohrium/commits/ab2423965300f898abbf676d8643a6f9cf6f92db>`_,
    time: 2015-01-19 04:08:33.242880.

    command: ``python benchmark/Python/nbody.py --size=1000*100 --bohrium=True``

Run 00
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/nbody.py - target: bhc, bohrium: True, size: 1000*100, elapsed-time: 15.774665
        

    stderr::

        N/A



Run 01
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/nbody.py - target: bhc, bohrium: True, size: 1000*100, elapsed-time: 15.761712
        

    stderr::

        N/A



Run 02
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/nbody.py - target: bhc, bohrium: True, size: 1000*100, elapsed-time: 15.750763
        

    stderr::

        N/A



