
Raw Benchmark Output
====================

Running Monte Carlo Pi on Octuplets using Bohrium/GPU
    commit: `#901c71bad23e6603afe61daa6330aaa6603550aa <https://bitbucket.org/bohrium/bohrium/commits/901c71bad23e6603afe61daa6330aaa6603550aa>`_,
    time: 2014-12-27 04:06:56.837065.

    command: ``python benchmark/Python/mc.py --size=10000000*100 --bohrium=True``

Run 00
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/mc.py - target: bhc, bohrium: True, size: 10000000*100, elapsed-time: 8.355553
        

    stderr::

        N/A



Run 01
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/mc.py - target: bhc, bohrium: True, size: 10000000*100, elapsed-time: 8.372436
        

    stderr::

        N/A



Run 02
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/mc.py - target: bhc, bohrium: True, size: 10000000*100, elapsed-time: 8.331099
        

    stderr::

        N/A



