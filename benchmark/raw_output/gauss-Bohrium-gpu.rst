
Raw Benchmark Output
====================

Running Gauss Elimination on Octuplets using Bohrium/GPU
    commit: `#eae832cb99c47396c757e62f24ff9aa492fe95c7 <https://bitbucket.org/bohrium/bohrium/commits/eae832cb99c47396c757e62f24ff9aa492fe95c7>`_,
    time: 2014-12-06 12:05:47.376138.

    command: ``python benchmark/Python/gauss.py --size=1000 --bohrium=True``

Run 00
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/gauss.py - target: bhc, bohrium: True, size: 1000, elapsed-time: 4.278290
        

    stderr::

        N/A



Run 01
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/gauss.py - target: bhc, bohrium: True, size: 1000, elapsed-time: 4.467922
        

    stderr::

        N/A



Run 02
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/gauss.py - target: bhc, bohrium: True, size: 1000, elapsed-time: 4.496868
        

    stderr::

        N/A



