
Raw Benchmark Output
====================

Running Monte Carlo Pi on Octuplets using Bohrium/GPU
    commit: `#0bd1688e19d0dc8dc039822a0b29ab2e51c76102 <https://bitbucket.org/bohrium/bohrium/commits/0bd1688e19d0dc8dc039822a0b29ab2e51c76102>`_,
    time: 2015-01-11 04:07:12.114344.

    command: ``python benchmark/Python/mc.py --size=10000000*100 --bohrium=True``

Run 00
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/mc.py - target: bhc, bohrium: True, size: 10000000*100, elapsed-time: 9.073405
        

    stderr::

        N/A



Run 01
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/mc.py - target: bhc, bohrium: True, size: 10000000*100, elapsed-time: 8.455209
        

    stderr::

        N/A



Run 02
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/mc.py - target: bhc, bohrium: True, size: 10000000*100, elapsed-time: 8.343094
        

    stderr::

        N/A



