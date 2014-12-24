
Raw Benchmark Output
====================

Running Heat Equation on Octuplets using Bohrium/GPU
    commit: `#901c71bad23e6603afe61daa6330aaa6603550aa <https://bitbucket.org/bohrium/bohrium/commits/901c71bad23e6603afe61daa6330aaa6603550aa>`_,
    time: 2014-12-24 04:06:55.602771.

    command: ``python benchmark/Python/heat_equation.py --size=3000*3000*100 --bohrium=True``

Run 00
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/heat_equation.py - target: bhc, bohrium: True, size: 3000*3000*100, elapsed-time: 3.485269
        

    stderr::

        N/A



Run 01
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/heat_equation.py - target: bhc, bohrium: True, size: 3000*3000*100, elapsed-time: 3.690878
        

    stderr::

        N/A



Run 02
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/heat_equation.py - target: bhc, bohrium: True, size: 3000*3000*100, elapsed-time: 3.644473
        

    stderr::

        N/A



