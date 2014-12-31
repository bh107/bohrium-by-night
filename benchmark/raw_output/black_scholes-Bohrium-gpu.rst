
Raw Benchmark Output
====================

Running Black Scholes on Octuplets using Bohrium/GPU
    commit: `#9a335eff7345f8d38f189f0b0f7a2f5d5c0e86a2 <https://bitbucket.org/bohrium/bohrium/commits/9a335eff7345f8d38f189f0b0f7a2f5d5c0e86a2>`_,
    time: 2014-12-31 04:08:42.084770.

    command: ``python benchmark/Python/black_scholes.py --size=1000000*100 --bohrium=True``

Run 00
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/black_scholes.py - target: bhc, bohrium: True, size: 1000000*100, elapsed-time: 8.721537
        

    stderr::

        N/A



Run 01
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/black_scholes.py - target: bhc, bohrium: True, size: 1000000*100, elapsed-time: 9.001456
        

    stderr::

        N/A



Run 02
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/black_scholes.py - target: bhc, bohrium: True, size: 1000000*100, elapsed-time: 8.705551
        

    stderr::

        N/A



