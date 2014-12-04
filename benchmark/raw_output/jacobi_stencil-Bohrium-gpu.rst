
Raw Benchmark Output
====================

Running Jacobi Stencil on Octuplets using Bohrium/GPU
    commit: `#eae832cb99c47396c757e62f24ff9aa492fe95c7 <https://bitbucket.org/bohrium/bohrium/commits/eae832cb99c47396c757e62f24ff9aa492fe95c7>`_,
    time: 2014-12-04 12:08:24.322788.

    command: ``python benchmark/Python/jacobi_stencil.py --size=3000*3000*100 --bohrium=True``

Run 00
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/jacobi_stencil.py - target: bhc, bohrium: True, size: 3000*3000*100, elapsed-time: 0.402525
        

    stderr::

        pure virtual method called
        terminate called without an active exception
        



Run 01
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/jacobi_stencil.py - target: bhc, bohrium: True, size: 3000*3000*100, elapsed-time: 0.387942
        

    stderr::

        pure virtual method called
        terminate called without an active exception
        



Run 02
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/jacobi_stencil.py - target: bhc, bohrium: True, size: 3000*3000*100, elapsed-time: 0.385760
        

    stderr::

        N/A



