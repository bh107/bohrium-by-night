
Raw Benchmark Output
====================

Running LU Factorization on Octuplets using Bohrium/GPU
    commit: `#75d48aa06a84862c800dd6bca1fbefdfe04db485 <https://bitbucket.org/bohrium/bohrium/commits/75d48aa06a84862c800dd6bca1fbefdfe04db485>`_,
    time: 2014-12-18 04:09:58.091950.

    command: ``python benchmark/Python/lu.py --size=1000 --bohrium=True``

Run 00
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/lu.py - target: bhc, bohrium: True, size: 1000, elapsed-time: 4.121476
        

    stderr::

        N/A



Run 01
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/lu.py - target: bhc, bohrium: True, size: 1000, elapsed-time: 4.076223
        

    stderr::

        N/A



Run 02
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/lu.py - target: bhc, bohrium: True, size: 1000, elapsed-time: 4.108823
        

    stderr::

        N/A



