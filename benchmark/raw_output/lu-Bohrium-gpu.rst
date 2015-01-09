
Raw Benchmark Output
====================

Running LU Factorization on Octuplets using Bohrium/GPU
    commit: `#c436af93e00e145dbbcf25e745526cf140b170f8 <https://bitbucket.org/bohrium/bohrium/commits/c436af93e00e145dbbcf25e745526cf140b170f8>`_,
    time: 2015-01-09 04:07:43.400357.

    command: ``python benchmark/Python/lu.py --size=1000 --bohrium=True``

Run 00
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/lu.py - target: bhc, bohrium: True, size: 1000, elapsed-time: 4.094616
        

    stderr::

        N/A



Run 01
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/lu.py - target: bhc, bohrium: True, size: 1000, elapsed-time: 4.071389
        

    stderr::

        N/A



Run 02
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/lu.py - target: bhc, bohrium: True, size: 1000, elapsed-time: 4.139674
        

    stderr::

        N/A



