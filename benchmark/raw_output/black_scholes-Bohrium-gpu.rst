
Raw Benchmark Output
====================

Running Black Scholes on Octuplets using Bohrium/GPU
    commit: `#547326e20b909705a32277094af038672acc2e6f <https://bitbucket.org/bohrium/bohrium/commits/547326e20b909705a32277094af038672acc2e6f>`_,
    time: 2014-12-12 12:09:24.841523.

    command: ``python benchmark/Python/black_scholes.py --size=1000000*100 --bohrium=True``

Run 00
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/black_scholes.py - target: bhc, bohrium: True, size: 1000000*100, elapsed-time: 8.504322
        

    stderr::

        N/A



Run 01
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/black_scholes.py - target: bhc, bohrium: True, size: 1000000*100, elapsed-time: 8.555798
        

    stderr::

        N/A



Run 02
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/black_scholes.py - target: bhc, bohrium: True, size: 1000000*100, elapsed-time: 7.607022
        

    stderr::

        N/A



