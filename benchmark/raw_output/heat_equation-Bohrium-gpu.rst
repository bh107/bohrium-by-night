
Raw Benchmark Output
====================

Running Heat Equation on Octuplets using Bohrium/GPU
    commit: `#0bd1688e19d0dc8dc039822a0b29ab2e51c76102 <https://bitbucket.org/bohrium/bohrium/commits/0bd1688e19d0dc8dc039822a0b29ab2e51c76102>`_,
    time: 2015-01-11 04:07:12.114344.

    command: ``python benchmark/Python/heat_equation.py --size=3000*3000*100 --bohrium=True``

Run 00
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/heat_equation.py - target: bhc, bohrium: True, size: 3000*3000*100, elapsed-time: 3.762676
        

    stderr::

        N/A



Run 01
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/heat_equation.py - target: bhc, bohrium: True, size: 3000*3000*100, elapsed-time: 3.700467
        

    stderr::

        N/A



Run 02
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/heat_equation.py - target: bhc, bohrium: True, size: 3000*3000*100, elapsed-time: 3.778952
        

    stderr::

        N/A



