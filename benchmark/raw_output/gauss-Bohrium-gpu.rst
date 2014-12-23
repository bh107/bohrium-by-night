
Raw Benchmark Output
====================

Running Gauss Elimination on Octuplets using Bohrium/GPU
    commit: `#8682240b5c176d5732105d16028fb961cf771c7f <https://bitbucket.org/bohrium/bohrium/commits/8682240b5c176d5732105d16028fb961cf771c7f>`_,
    time: 2014-12-23 04:06:56.503910.

    command: ``python benchmark/Python/gauss.py --size=1000 --bohrium=True``

Run 00
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/gauss.py - target: bhc, bohrium: True, size: 1000, elapsed-time: 4.538652
        

    stderr::

        pure virtual method called
        terminate called without an active exception
        



Run 01
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/gauss.py - target: bhc, bohrium: True, size: 1000, elapsed-time: 4.720068
        

    stderr::

        N/A



Run 02
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/gauss.py - target: bhc, bohrium: True, size: 1000, elapsed-time: 4.492807
        

    stderr::

        N/A



