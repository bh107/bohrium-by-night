
Raw Benchmark Output
====================

Running Gauss Elimination on Octuplets using Bohrium/GPU
    commit: `#a7036bb012cf1d24764010f2ec1c4618ad4321d3 <https://bitbucket.org/bohrium/bohrium/commits/a7036bb012cf1d24764010f2ec1c4618ad4321d3>`_,
    time: 2015-01-08 04:11:08.542788.

    command: ``python benchmark/Python/gauss.py --size=1000 --bohrium=True``

Run 00
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/gauss.py - target: bhc, bohrium: True, size: 1000, elapsed-time: 4.498696
        

    stderr::

        N/A



Run 01
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/gauss.py - target: bhc, bohrium: True, size: 1000, elapsed-time: 4.588186
        

    stderr::

        pure virtual method called
        terminate called without an active exception
        



Run 02
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/gauss.py - target: bhc, bohrium: True, size: 1000, elapsed-time: 4.483043
        

    stderr::

        N/A



