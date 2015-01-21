
Raw Benchmark Output
====================

Running LU Factorization on Octuplets using Bohrium/GPU
    commit: `#5658bbbd87d6fa5dc2935e0e14b2df428b928a42 <https://bitbucket.org/bohrium/bohrium/commits/5658bbbd87d6fa5dc2935e0e14b2df428b928a42>`_,
    time: 2015-01-21 04:08:08.480016.

    command: ``python benchmark/Python/lu.py --size=1000 --bohrium=True``

Run 00
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/lu.py - target: bhc, bohrium: True, size: 1000, elapsed-time: 4.100237
        

    stderr::

        N/A



Run 01
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/lu.py - target: bhc, bohrium: True, size: 1000, elapsed-time: 4.062910
        

    stderr::

        N/A



Run 02
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/lu.py - target: bhc, bohrium: True, size: 1000, elapsed-time: 4.089222
        

    stderr::

        N/A



