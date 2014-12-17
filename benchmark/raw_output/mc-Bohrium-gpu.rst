
Raw Benchmark Output
====================

Running Monte Carlo Pi on Octuplets using Bohrium/GPU
    commit: `#62cc53b60eae0a14bef165e853c7017ace4411e8 <https://bitbucket.org/bohrium/bohrium/commits/62cc53b60eae0a14bef165e853c7017ace4411e8>`_,
    time: 2014-12-17 04:08:14.835360.

    command: ``python benchmark/Python/mc.py --size=10000000*100 --bohrium=True``

Run 00
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/mc.py - target: bhc, bohrium: True, size: 10000000*100, elapsed-time: 8.322460
        

    stderr::

        N/A



Run 01
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/mc.py - target: bhc, bohrium: True, size: 10000000*100, elapsed-time: 8.297555
        

    stderr::

        N/A



Run 02
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/mc.py - target: bhc, bohrium: True, size: 10000000*100, elapsed-time: 8.352352
        

    stderr::

        N/A



