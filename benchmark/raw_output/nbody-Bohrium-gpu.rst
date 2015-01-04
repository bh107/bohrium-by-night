
Raw Benchmark Output
====================

Running N-Body on Octuplets using Bohrium/GPU
    commit: `#9a335eff7345f8d38f189f0b0f7a2f5d5c0e86a2 <https://bitbucket.org/bohrium/bohrium/commits/9a335eff7345f8d38f189f0b0f7a2f5d5c0e86a2>`_,
    time: 2015-01-04 04:07:06.265830.

    command: ``python benchmark/Python/nbody.py --size=1000*100 --bohrium=True``

Run 00
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/nbody.py - target: bhc, bohrium: True, size: 1000*100, elapsed-time: 16.027252
        

    stderr::

        N/A



Run 01
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/nbody.py - target: bhc, bohrium: True, size: 1000*100, elapsed-time: 15.805619
        

    stderr::

        N/A



Run 02
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/nbody.py - target: bhc, bohrium: True, size: 1000*100, elapsed-time: 15.853707
        

    stderr::

        N/A



