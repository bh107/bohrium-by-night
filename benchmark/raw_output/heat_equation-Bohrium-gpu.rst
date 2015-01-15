
Raw Benchmark Output
====================

Running Heat Equation on Octuplets using Bohrium/GPU
    commit: `#35b8627558e1e4dce220ee17fae487c1c3cbd33c <https://bitbucket.org/bohrium/bohrium/commits/35b8627558e1e4dce220ee17fae487c1c3cbd33c>`_,
    time: 2015-01-15 04:09:13.857642.

    command: ``python benchmark/Python/heat_equation.py --size=3000*3000*100 --bohrium=True``

Run 00
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/heat_equation.py - target: bhc, bohrium: True, size: 3000*3000*100, elapsed-time: 3.539184
        

    stderr::

        N/A



Run 01
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/heat_equation.py - target: bhc, bohrium: True, size: 3000*3000*100, elapsed-time: 3.658666
        

    stderr::

        N/A



Run 02
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/heat_equation.py - target: bhc, bohrium: True, size: 3000*3000*100, elapsed-time: 3.865563
        

    stderr::

        N/A



