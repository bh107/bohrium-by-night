
Raw Benchmark Output
====================

Running N-Body on Octuplets using Bohrium/GPU
    commit: `#6103f1ec1b8914f895dfb1b8f89c1ddb92e660e6 <https://bitbucket.org/bohrium/bohrium/commits/6103f1ec1b8914f895dfb1b8f89c1ddb92e660e6>`_,
    time: 2015-01-22 04:07:38.186877.

    command: ``python benchmark/Python/nbody.py --size=1000*100 --bohrium=True``

Run 00
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/nbody.py - target: bhc, bohrium: True, size: 1000*100, elapsed-time: 15.813616
        

    stderr::

        N/A



Run 01
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/nbody.py - target: bhc, bohrium: True, size: 1000*100, elapsed-time: 15.823578
        

    stderr::

        N/A



Run 02
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/nbody.py - target: bhc, bohrium: True, size: 1000*100, elapsed-time: 15.799358
        

    stderr::

        N/A



