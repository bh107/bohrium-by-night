
Raw Benchmark Output
====================

Running Convolution 3D on Octuplets using Bohrium/CPU
    commit: `#9a335eff7345f8d38f189f0b0f7a2f5d5c0e86a2 <https://bitbucket.org/bohrium/bohrium/commits/9a335eff7345f8d38f189f0b0f7a2f5d5c0e86a2>`_,
    time: 2015-01-01 04:07:09.586552.

    command: ``python benchmark/Python/convolve_3d.py --size=100 --bohrium=True``

Run 00
~~~~~~
    stdout::

        N/A

    stderr::

        benchmark/Python/convolve_3d.py:24: RuntimeWarning: Encountering an operation not supported by Bohrium. It will be handled by the original NumPy.
          totalsum += kernel[filterZ + kernelrad, filterY + kernelrad, filterX + kernelrad]
        



Run 01
~~~~~~
    stdout::

        N/A

    stderr::

        benchmark/Python/convolve_3d.py:24: RuntimeWarning: Encountering an operation not supported by Bohrium. It will be handled by the original NumPy.
          totalsum += kernel[filterZ + kernelrad, filterY + kernelrad, filterX + kernelrad]
        



Run 02
~~~~~~
    stdout::

        N/A

    stderr::

        benchmark/Python/convolve_3d.py:24: RuntimeWarning: Encountering an operation not supported by Bohrium. It will be handled by the original NumPy.
          totalsum += kernel[filterZ + kernelrad, filterY + kernelrad, filterX + kernelrad]
        



