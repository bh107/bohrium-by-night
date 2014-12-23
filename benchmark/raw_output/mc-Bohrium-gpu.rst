
Raw Benchmark Output
====================

Running Monte Carlo Pi on Octuplets using Bohrium/GPU
    commit: `#8682240b5c176d5732105d16028fb961cf771c7f <https://bitbucket.org/bohrium/bohrium/commits/8682240b5c176d5732105d16028fb961cf771c7f>`_,
    time: 2014-12-23 04:06:56.503910.

    command: ``python benchmark/Python/mc.py --size=10000000*100 --bohrium=True``

Run 00
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/mc.py - target: bhc, bohrium: True, size: 10000000*100, elapsed-time: 8.331764
        

    stderr::

        N/A



Run 01
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/mc.py - target: bhc, bohrium: True, size: 10000000*100, elapsed-time: 8.298643
        

    stderr::

        N/A



Run 02
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/mc.py - target: bhc, bohrium: True, size: 10000000*100, elapsed-time: 8.345863
        

    stderr::

        N/A



