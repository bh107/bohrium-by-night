
Raw Benchmark Output
====================

Running Convolution 3D on Octuplets using Bohrium/GPU
    commit: `#87974a097720c3bf944f8d7b93c8752e16ec3c6d <https://bitbucket.org/bohrium/bohrium/commits/87974a097720c3bf944f8d7b93c8752e16ec3c6d>`_,
    time: 2014-12-30 04:07:07.845036.

    command: ``python benchmark/Python/convolve_3d.py --size=100 --bohrium=True``

Run 00
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        

    stderr::

        benchmark/Python/convolve_3d.py:24: RuntimeWarning: Encountering an operation not supported by Bohrium. It will be handled by the original NumPy.
          totalsum += kernel[filterZ + kernelrad, filterY + kernelrad, filterX + kernelrad]
        



Run 01
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        

    stderr::

        benchmark/Python/convolve_3d.py:24: RuntimeWarning: Encountering an operation not supported by Bohrium. It will be handled by the original NumPy.
          totalsum += kernel[filterZ + kernelrad, filterY + kernelrad, filterX + kernelrad]
        



Run 02
~~~~~~
    stdout::

        [Info] [GPU] Kernel type: both
        [Info] [GPU] Compile type: async.
        [Info] [GPU] Work group sizes: 1D[128], 2D[32, 4], 3D[32, 2, 2]
        

    stderr::

        benchmark/Python/convolve_3d.py:24: RuntimeWarning: Encountering an operation not supported by Bohrium. It will be handled by the original NumPy.
          totalsum += kernel[filterZ + kernelrad, filterY + kernelrad, filterX + kernelrad]
        



