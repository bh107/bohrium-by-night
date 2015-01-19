
Raw Benchmark Output
====================

Running Monte Carlo Pi on Octuplets using Bohrium/GPU
    commit: `#ab2423965300f898abbf676d8643a6f9cf6f92db <https://bitbucket.org/bohrium/bohrium/commits/ab2423965300f898abbf676d8643a6f9cf6f92db>`_,
    time: 2015-01-19 04:08:33.242880.

    command: ``python benchmark/Python/mc.py --size=10000000*100 --bohrium=True``

Run 00
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/mc.py - target: bhc, bohrium: True, size: 10000000*100, elapsed-time: 8.254681
        

    stderr::

        N/A



Run 01
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/mc.py - target: bhc, bohrium: True, size: 10000000*100, elapsed-time: 8.281177
        

    stderr::

        N/A



Run 02
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/mc.py - target: bhc, bohrium: True, size: 10000000*100, elapsed-time: 8.329619
        

    stderr::

        N/A



