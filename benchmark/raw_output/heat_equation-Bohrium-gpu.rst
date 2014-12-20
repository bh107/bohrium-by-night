
Raw Benchmark Output
====================

Running Heat Equation on Octuplets using Bohrium/GPU
    commit: `#fa32761e3dc4132d8188145007c8189576f85446 <https://bitbucket.org/bohrium/bohrium/commits/fa32761e3dc4132d8188145007c8189576f85446>`_,
    time: 2014-12-20 04:07:36.583962.

    command: ``python benchmark/Python/heat_equation.py --size=3000*3000*100 --bohrium=True``

Run 00
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/heat_equation.py - target: bhc, bohrium: True, size: 3000*3000*100, elapsed-time: 3.785836
        

    stderr::

        N/A



Run 01
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/heat_equation.py - target: bhc, bohrium: True, size: 3000*3000*100, elapsed-time: 3.721040
        

    stderr::

        N/A



Run 02
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        benchmark/Python/heat_equation.py - target: bhc, bohrium: True, size: 3000*3000*100, elapsed-time: 3.845823
        

    stderr::

        N/A



