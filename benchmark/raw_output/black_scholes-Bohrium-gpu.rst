
Raw Benchmark Output
====================

Running Black Scholes on Octuplets using Bohrium/GPU
    commit: `#87974a097720c3bf944f8d7b93c8752e16ec3c6d <https://bitbucket.org/bohrium/bohrium/commits/87974a097720c3bf944f8d7b93c8752e16ec3c6d>`_,
    time: 2014-12-29 04:07:09.104753.

    command: ``python benchmark/Python/black_scholes.py --size=1000000*100 --bohrium=True``

Run 00
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/black_scholes.py - target: bhc, bohrium: True, size: 1000000*100, elapsed-time: 8.806359
        

    stderr::

        N/A



Run 01
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/black_scholes.py - target: bhc, bohrium: True, size: 1000000*100, elapsed-time: 8.650786
        

    stderr::

        N/A



Run 02
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/black_scholes.py - target: bhc, bohrium: True, size: 1000000*100, elapsed-time: 8.642786
        

    stderr::

        N/A



