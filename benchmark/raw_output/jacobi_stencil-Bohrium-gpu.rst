
Raw Benchmark Output
====================

Running Jacobi Stencil on Octuplets using Bohrium/GPU
    commit: `#eae832cb99c47396c757e62f24ff9aa492fe95c7 <https://bitbucket.org/bohrium/bohrium/commits/eae832cb99c47396c757e62f24ff9aa492fe95c7>`_,
    time: 2014-12-02 12:06:09.616324.

    command: ``python benchmark/Python/jacobi_stencil.py --size=3000*3000*100 --bohrium=True``

Run 00
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/jacobi_stencil.py - target: bhc, bohrium: True, size: 3000*3000*100, elapsed-time: 0.390254
        

    stderr::

        N/A



Run 01
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/jacobi_stencil.py - target: bhc, bohrium: True, size: 3000*3000*100, elapsed-time: 0.387667
        

    stderr::

        N/A



Run 02
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/jacobi_stencil.py - target: bhc, bohrium: True, size: 3000*3000*100, elapsed-time: 0.387902
        

    stderr::

        N/A



