
Raw Benchmark Output
====================

Running Convolution 3D on Octuplets using Bohrium/GPU
    commit: `#bbe0e6d6a7b38272dfd5d5ad2f2be99bb2292f4c <https://bitbucket.org/bohrium/bohrium/commits/bbe0e6d6a7b38272dfd5d5ad2f2be99bb2292f4c>`_,
    time: 2014-10-08 04:06:00.880923.

    command: ``python benchmark/Python/convolve_3d.py --size=5 --bohrium=True``

Run 00
~~~~~~
    stdout::

        N/A

    stderr::

        benchmark/Python/convolve_3d.py:23: RuntimeWarning: Encountering an operation not supported by Bohrium. It will be handled by the original NumPy.
          totalsum += kernel[filterZ + kernelrad, filterY + kernelrad, filterX + kernelrad]
        



