
Raw Benchmark Output
====================

Running Heat Equation on Octuplets using Bohrium/GPU
    commit: `#62cc53b60eae0a14bef165e853c7017ace4411e8 <https://bitbucket.org/bohrium/bohrium/commits/62cc53b60eae0a14bef165e853c7017ace4411e8>`_,
    time: 2014-12-17 04:08:14.835360.

    command: ``python benchmark/Python/heat_equation.py --size=3000*3000*100 --bohrium=True``

Run 00
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/heat_equation.py - target: bhc, bohrium: True, size: 3000*3000*100, elapsed-time: 3.726445
        

    stderr::

        N/A



Run 01
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/heat_equation.py - target: bhc, bohrium: True, size: 3000*3000*100, elapsed-time: 3.710655
        

    stderr::

        N/A



Run 02
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/heat_equation.py - target: bhc, bohrium: True, size: 3000*3000*100, elapsed-time: 3.797713
        

    stderr::

        N/A



