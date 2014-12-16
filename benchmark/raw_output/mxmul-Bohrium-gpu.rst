
Raw Benchmark Output
====================

Running Matrix Multiplication on Octuplets using Bohrium/GPU
    commit: `#580a7bbc9e806f1abf194c55424e08024db0babb <https://bitbucket.org/bohrium/bohrium/commits/580a7bbc9e806f1abf194c55424e08024db0babb>`_,
    time: 2014-12-16 04:08:51.280922.

    command: ``python benchmark/Python/mxmul.py --size=1000 --bohrium=True``

Run 00
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/mxmul.py - target: bhc, bohrium: True, size: 1000, elapsed-time: 0.002316
        

    stderr::

        pure virtual method called
        terminate called without an active exception
        



Run 01
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/mxmul.py - target: bhc, bohrium: True, size: 1000, elapsed-time: 0.002165
        

    stderr::

        pure virtual method called
        terminate called without an active exception
        



Run 02
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/mxmul.py - target: bhc, bohrium: True, size: 1000, elapsed-time: 0.002529
        

    stderr::

        N/A



